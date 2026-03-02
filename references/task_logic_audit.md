# Task Logic Audit: Flanker Task (T000004)

## 1. Paradigm Intent

- Task: Eriksen Flanker Task (`flanker`).
- Primary construct: selective attention and interference control (congruency effect on RT/accuracy).
- Manipulated factors:
  - flanker congruency (`congruent`, `incongruent`)
  - target direction (`left`, `right`).
- Dependent measures:
  - response key (`stimulus_response`)
  - response time (`stimulus_rt`)
  - correctness (`stimulus_hit`)
  - timeout/no-response count.
- Key citations:
  - `W2058317558` (Eriksen & Eriksen, 1974)
  - `W2131582654` (Ridderinkhof et al., 1997)
  - `W2000998192` (Botvinick et al., 2001)
  - `W2150902492` (Fan et al., 2002)

## 2. Block/Trial Workflow

### Block Structure

- Total blocks:
  - human profile: `3`
  - qa/sim profiles: `1`.
- Trials per block:
  - human profile: `60`
  - qa/sim profiles: `16`.
- Randomization/counterbalancing:
  - runtime uses `BlockUnit.generate_conditions()` with 4 condition tokens.
  - within-block trial order is randomized by PsyFlow block seed.
- Condition weight policy:
  - `task.condition_weights` is not defined in configs.
  - weighted generation is not used.
  - generation defaults to even/balanced built-in behavior.
- Condition generation method:
  - built-in `BlockUnit.generate_conditions(...)`.
  - no custom generator.
  - generated trial input passed into `run_trial.py` is one condition token string.
- Runtime-generated trial values (if any):
  - `run_trial.py` splits token into `flanker_type` and `target_direction`.
  - correct key is derived from `target_direction`.
  - no additional random condition fields are generated in `run_trial.py`.

### Trial State Machine

1. `pre_stim_fixation`
   - Onset trigger: `fixation_onset`.
   - Stimuli shown: `fixation`.
   - Valid keys: response keys are included in context metadata, but no response is captured.
   - Timeout behavior: fixed `fixation_duration`.
   - Next state: `flanker_response`.

2. `flanker_response`
   - Onset trigger: `congruent_stim_onset` or `incongruent_stim_onset` (by condition).
   - Stimuli shown: one of `congruent_left`, `congruent_right`, `incongruent_left`, `incongruent_right`.
   - Valid keys: `left_key`, `right_key`.
   - Timeout behavior: response window closes at `stim_duration` if no key response.
   - Next state: `feedback`.

3. `feedback`
   - Onset trigger: one of `feedback_correct_response`, `feedback_incorrect_response`, `feedback_no_response`.
   - Stimuli shown: `correct_feedback`, `incorrect_feedback`, or `no_response_feedback`.
   - Valid keys: none captured in this phase.
   - Timeout behavior: fixed `feedback_duration`.
   - Next state: `inter_trial_interval`.

4. `inter_trial_interval`
   - Onset trigger: none configured.
   - Stimuli shown: blank frame (no explicit visual stimulus).
   - Valid keys: none captured.
   - Timeout behavior: random `iti_duration`.
   - Next state: next trial or block end.

## 3. Condition Semantics

- Condition ID: `congruent_left`
  - Participant-facing meaning: all arrows point left.
  - Concrete stimulus realization: `<<<<<`.
  - Outcome rules: correct response is `left_key`.

- Condition ID: `congruent_right`
  - Participant-facing meaning: all arrows point right.
  - Concrete stimulus realization: `>>>>>`.
  - Outcome rules: correct response is `right_key`.

- Condition ID: `incongruent_left`
  - Participant-facing meaning: center arrow points left, flankers point right.
  - Concrete stimulus realization: `>><>>`.
  - Outcome rules: correct response is `left_key`.

- Condition ID: `incongruent_right`
  - Participant-facing meaning: center arrow points right, flankers point left.
  - Concrete stimulus realization: `<<><<`.
  - Outcome rules: correct response is `right_key`.

Participant-facing text/stimulus source:

- Participant-facing text source:
  - config-defined `stimuli.*` in `config/config*.yaml`.
- Why this source is appropriate for auditability:
  - all task-facing wording/symbol strings are externally visible and versioned in config.
- Localization strategy:
  - keep all participant wording in config stimuli and avoid code-side hardcoded text; language variants should be swapped in config files.

## 4. Response and Scoring Rules

- Response mapping:
  - left target direction -> `left_key` (`f`).
  - right target direction -> `right_key` (`j`).
- Response key source:
  - config fields (`task.left_key`, `task.right_key`, `task.key_list`).
- Missing-response policy:
  - no response during `stim_duration` routes to `no_response_feedback`.
- Correctness logic:
  - `capture_response(..., correct_keys=correct_response)` computes `stimulus_hit`.
- Reward/penalty updates:
  - none (accuracy/RT task; no points bank).
- Running metrics:
  - block-level accuracy in `main.py` computed from `stimulus_hit`.

## 5. Stimulus Layout Plan

- Screen name: `pre_stim_fixation`
  - Stimulus IDs shown together: `fixation`
  - Layout anchors (`pos`): default centered text.
  - Size/spacing: height configured (`1.5` in current configs).
  - Readability/overlap checks: single-item screen, no overlap risk.
  - Rationale: central fixation before target onset.

- Screen name: `flanker_response`
  - Stimulus IDs shown together: one flanker text stimulus per trial condition.
  - Layout anchors (`pos`): default centered text.
  - Size/spacing: height configured (`1.5`).
  - Readability/overlap checks: single-item screen, no overlap risk.
  - Rationale: isolate center-arrow judgment under congruent/incongruent context.

- Screen name: `feedback`
  - Stimulus IDs shown together: one of feedback text stimuli.
  - Layout anchors (`pos`): default centered text.
  - Size/spacing: height configured (`1.5`).
  - Readability/overlap checks: single-item screen, no overlap risk.
  - Rationale: immediate performance acknowledgment.

## 6. Trigger Plan

- Experiment-level:
  - `exp_onset=98`, `exp_end=99`.
- Block-level:
  - `block_onset=100`, `block_end=101`.
- Trial phase:
  - `fixation_onset=1`
  - `congruent_stim_onset=10`
  - `incongruent_stim_onset=20`.
- Response events:
  - `left_key_press=30`
  - `right_key_press=31`.
- Feedback branch:
  - `feedback_correct_response=51`
  - `feedback_incorrect_response=52`
  - `feedback_no_response=53`
  - `feedback_onset=60` (declared in config, not currently emitted by `run_trial.py`).

## 7. Architecture Decisions (Auditability)

- `main.py` runtime flow style:
  - simple single mode-aware flow (`human|qa|sim`) with shared setup and block loop.
- `utils.py` used?
  - no task-local `utils.py` is used.
- Custom controller used?
  - no custom controller class; standard `BlockUnit` + `run_trial` flow.
- Why PsyFlow-native path is sufficient:
  - condition token generation and per-trial response capture fit native units directly.
- Legacy/backward-compatibility fallback logic required?
  - none identified.

## 8. Inference Log

- Decision: include explicit feedback stage (`correct/incorrect/no_response`) after response.
  - Why inference was required: canonical Flanker references do not mandate a specific feedback policy in every implementation.
  - Citation-supported rationale: behavior/EEG practical implementations often use immediate performance feedback for participant compliance (`W2131582654`, `W2150902492` context).

- Decision: set human run size to `3 x 60` and QA/sim to `1 x 16`.
  - Why inference was required: selected references establish paradigm logic but not this exact engineering profile.
  - Citation-supported rationale: repeated trial blocks are required for stable congruency contrasts (`W2058317558`, `W2150902492`).

- Decision: no explicit condition weights in config.
  - Why inference was required: no weighted condition protocol is specified in current task design.
  - Citation-supported rationale: balanced congruent/incongruent exposure supports unbiased flanker-effect estimation (`W2058317558`).
