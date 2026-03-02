# Stimulus Mapping

## Mapping Table

| Condition | Stage/Phase | Stimulus IDs | Participant-Facing Content | Source Paper ID | Evidence (quote/figure/table) | Implementation Mode | Asset References | Notes |
|---|---|---|---|---|---|---|---|---|
| `all_conditions` | `pre_stim_fixation` | `fixation` | Central fixation cross (`+`) before each trial. | `W2150902492` | ANT/Flanker timing structure includes a pre-target fixation stage. | `psychopy_builtin` | `config/*.yaml -> stimuli.fixation` | Single centered text stimulus. |
| `congruent_left` | `flanker_response` | `congruent_left` | `<<<<<` with center arrow pointing left and congruent flankers. | `W2058317558` | Congruent flankers match target direction in canonical Flanker design. | `psychopy_builtin` | `config/*.yaml -> stimuli.congruent_left` | Correct key is `left_key`. |
| `congruent_right` | `flanker_response` | `congruent_right` | `>>>>>` with center arrow pointing right and congruent flankers. | `W2058317558` | Congruent flankers match target direction in canonical Flanker design. | `psychopy_builtin` | `config/*.yaml -> stimuli.congruent_right` | Correct key is `right_key`. |
| `incongruent_left` | `flanker_response` | `incongruent_left` | `>><>>` where center target is left and flankers are opposite. | `W2058317558` | Incongruent flankers conflict with target direction, increasing interference. | `psychopy_builtin` | `config/*.yaml -> stimuli.incongruent_left` | Correct key is `left_key`. |
| `incongruent_right` | `flanker_response` | `incongruent_right` | `<<><<` where center target is right and flankers are opposite. | `W2058317558` | Incongruent flankers conflict with target direction, increasing interference. | `psychopy_builtin` | `config/*.yaml -> stimuli.incongruent_right` | Correct key is `right_key`. |
| `all_conditions` | `inter_trial_interval` | `none (blank frame)` | No explicit stimulus; short blank interval between trials. | `W2150902492` | Inter-trial spacing is a timing-control stage in repeated trial paradigms. | `psychopy_builtin` | `config/*.yaml -> timing.iti_duration` | Implemented via `StimUnit('iti').show(...)` without `.add_stim(...)`. |
| `all_conditions` | `envelope` | `instruction_text`, `block_break`, `good_bye` | Instruction, inter-block summary, and closing message screens. | `W2150902492` | Task framing and key mapping instructions are required for valid participant responses. | `psychopy_builtin` | `config/*.yaml -> stimuli.instruction_text/block_break/good_bye` | Participant-facing text is config-defined and localization-ready. |
