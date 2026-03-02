# Parameter Mapping

## Mapping Table

| Parameter ID | Config Path | Implemented Value | Source Paper ID | Evidence (quote/figure/table) | Decision Type | Notes |
|---|---|---|---|---|---|---|
| `condition_set` | `task.conditions` | `['congruent_left', 'congruent_right', 'incongruent_left', 'incongruent_right']` | `W2058317558` | Core Flanker manipulation compares congruent vs incongruent flankers around a directional target. | `direct` | Two response directions are represented for each congruency class. |
| `trial_volume_human` | `task.total_blocks`, `task.trial_per_block`, `task.total_trials` | `3 x 60 = 180` | `W2150902492` | ANT-style Flanker variants use repeated blocks with enough trials for stable congruency effects. | `adapted` | Current profile is a practical adaptation for EEG-compatible runs. |
| `trial_volume_qa_sim` | `config_qa/task.total_trials`, `config_scripted_sim/task.total_trials`, `config_sampler_sim/task.total_trials` | `16` trials in one block | `W2131582654` | Reduced trial counts are acceptable for development smoke tests, not inferential analysis. | `inferred` | Keep short for CI/runtime checks only. |
| `response_mapping` | `task.left_key`, `task.right_key`, `task.key_list` | `left=f`, `right=j`, keys `['f','j']` | `W2058317558` | Flanker tasks require side-discrimination responses to the target direction. | `inferred` | Hardware key choice is implementation-defined. |
| `fixation_duration` | `timing.fixation_duration` | `0.5` s | `W2150902492` | ANT/Flanker protocols commonly use a brief fixation before target display. | `adapted` | Single fixed value in current configs. |
| `stimulus_deadline` | `timing.stim_duration` | `1.0` s | `W2150902492` | Bounded stimulus/response window is standard for RT and omission capture. | `adapted` | Response collection terminates on key press or timeout. |
| `feedback_duration` | `timing.feedback_duration` | `0.5` s | `W2131582654` | Immediate correctness feedback is a common implementation choice in applied Flanker variants. | `inferred` | Not mandatory in all canonical variants. |
| `iti_duration` | `timing.iti_duration` | random `[0.8, 1.2]` s | `W2150902492` | Jittered trial spacing is used to reduce temporal anticipation in repeated trial designs. | `adapted` | Current implementation uses uniform random draw from the range. |
| `condition_weight_policy` | `task.condition_weights` (absent) | no explicit weights; even/default generation via `BlockUnit.generate_conditions()` | `W2058317558` | Balanced congruent/incongruent exposure is required for interpretable interference metrics. | `inferred` | No custom generator; no weighted schedule configured. |
| `trigger_scheme` | `triggers.map` | fixation/stimulus/response/feedback/block/experiment trigger set | `W2150902492` | Stage-separated trigger coding is needed for synchronized EEG/behavioral analysis. | `inferred` | Feedback has branch-specific codes (`correct`, `incorrect`, `no_response`). |
