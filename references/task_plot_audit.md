# Task Plot Audit

- generated_at: 2026-03-10T00:17:21
- mode: existing
- task_path: E:\Taskbeacon\T000004-flanker

## 1. Inputs and provenance

- E:\Taskbeacon\T000004-flanker\README.md
- E:\Taskbeacon\T000004-flanker\config\config.yaml
- E:\Taskbeacon\T000004-flanker\src\run_trial.py

## 2. Evidence extracted from README

- Trial-Level Flow table not found; run_trial.py used as primary source.

## 3. Evidence extracted from config/source

- congruent_left: phase=pre stim fixation, deadline_expr=settings.fixation_duration, response_expr=n/a, stim_expr='fixation'
- congruent_left: phase=flanker response, deadline_expr=settings.stim_duration, response_expr=settings.stim_duration, stim_expr=str(condition)
- congruent_right: phase=pre stim fixation, deadline_expr=settings.fixation_duration, response_expr=n/a, stim_expr='fixation'
- congruent_right: phase=flanker response, deadline_expr=settings.stim_duration, response_expr=settings.stim_duration, stim_expr=str(condition)
- incongruent_left: phase=pre stim fixation, deadline_expr=settings.fixation_duration, response_expr=n/a, stim_expr='fixation'
- incongruent_left: phase=flanker response, deadline_expr=settings.stim_duration, response_expr=settings.stim_duration, stim_expr=str(condition)
- incongruent_right: phase=pre stim fixation, deadline_expr=settings.fixation_duration, response_expr=n/a, stim_expr='fixation'
- incongruent_right: phase=flanker response, deadline_expr=settings.stim_duration, response_expr=settings.stim_duration, stim_expr=str(condition)

## 4. Mapping to task_plot_spec

- timeline collection: one representative timeline per unique trial logic
- phase flow inferred from run_trial set_trial_context order and branch predicates
- participant-visible show() phases without set_trial_context are inferred where possible and warned
- duration/response inferred from deadline/capture expressions
- stimulus examples inferred from stim_id + config stimuli
- conditions with equivalent phase/timing logic collapsed and annotated as variants
- root_key: task_plot_spec
- spec_version: 0.2

## 5. Style decision and rationale

- Single timeline-collection view selected by policy: one representative condition per unique timeline logic.

## 6. Rendering parameters and constraints

- output_file: task_flow.png
- dpi: 300
- max_conditions: 4
- screens_per_timeline: 6
- screen_overlap_ratio: 0.1
- screen_slope: 0.08
- screen_slope_deg: 25.0
- screen_aspect_ratio: 1.4545454545454546
- qa_mode: local
- auto_layout_feedback:
  - layout pass 1: crop-only; left=0.011, right=0.039, blank=0.135
- auto_layout_feedback_records:
  - pass: 1
    metrics: {'left_ratio': 0.011, 'right_ratio': 0.0388, 'blank_ratio': 0.1354}

## 7. Output files and checksums

- E:\Taskbeacon\T000004-flanker\references\task_plot_spec.yaml: sha256=013c12bf6c99a320bedd4fc3a0941f6eb05f0e208fc10ee8f936d167f071a3f4
- E:\Taskbeacon\T000004-flanker\references\task_plot_spec.json: sha256=8a70f649cde3c6f6f07220060adb8dce02516402536d5beb5c377cd49ce59b62
- E:\Taskbeacon\T000004-flanker\references\task_plot_source_excerpt.md: sha256=84d2b126c8bbd55e1632e43a0dc46ccd489863e428779de7a7df5b8de722e1a3
- E:\Taskbeacon\T000004-flanker\task_flow.png: sha256=2696c5c954e711107488eb7de1c8eaf89e22f94e0736eaba282d13b01041672a

## 8. Inferred/uncertain items

- collapsed equivalent condition logic into representative timeline: congruent_left, congruent_right, incongruent_left, incongruent_right
