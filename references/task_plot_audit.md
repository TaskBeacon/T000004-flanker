# 任务流程图审计

- generated_at: 2026-03-23T22:57:08
- mode: existing
- task_path: E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000004-flanker

## 1. 输入与来源

- E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000004-flanker\README.md
- E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000004-flanker\config\config.yaml
- E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000004-flanker\src\run_trial.py

## 2. 从 README 提取的证据

- README 没有单独的 Trial-Level Flow 表，因此以 `run_trial.py` 作为主证据源。
- README 的 `Task Flow` 预览仅用于确认任务目录中的图已被更新。

## 3. 从 config/source 提取的证据

- congruent_left: phase=pre stim fixation, deadline_expr=settings.fixation_duration, response_expr=n/a, stim_expr='fixation'
- congruent_left: phase=flanker response, deadline_expr=settings.stim_duration, response_expr=settings.stim_duration, stim_expr=str(condition)
- congruent_right: phase=pre stim fixation, deadline_expr=settings.fixation_duration, response_expr=n/a, stim_expr='fixation'
- congruent_right: phase=flanker response, deadline_expr=settings.stim_duration, response_expr=settings.stim_duration, stim_expr=str(condition)
- incongruent_left: phase=pre stim fixation, deadline_expr=settings.fixation_duration, response_expr=n/a, stim_expr='fixation'
- incongruent_left: phase=flanker response, deadline_expr=settings.stim_duration, response_expr=settings.stim_duration, stim_expr=str(condition)
- incongruent_right: phase=pre stim fixation, deadline_expr=settings.fixation_duration, response_expr=n/a, stim_expr='fixation'
- incongruent_right: phase=flanker response, deadline_expr=settings.stim_duration, response_expr=settings.stim_duration, stim_expr=str(condition)
- iti: phase=inter trial interval, duration_expr=settings.iti_duration, context=show() without set_trial_context(...)

## 3b. 说明

- `run_trial.py` 里 `make_unit(unit_label="iti").show(...)` 没有 `set_trial_context(...)`，初版推断漏掉了这一段参与者可见的空白间隔。
- 最终规范已把 `ITI` 补回到每条时间线，和 `config/config.yaml` 中的 `iti_duration` 保持一致。
- 代码中没有复杂分支，因此没有未解析的 if-test 警告。

## 4. 映射到 task_plot_spec

- timeline collection: one representative timeline per unique trial logic
- phase flow inferred from run_trial set_trial_context order and branch predicates
- participant-visible show() phases without set_trial_context are inferred where possible and warned
- duration/response inferred from deadline/capture expressions
- stimulus examples inferred from stim_id + config stimuli
- conditions with equivalent phase/timing logic collapsed and annotated as variants
- root_key: task_plot_spec
- spec_version: 0.2

## 5. 样式决策与理由

- 采用 4 条时间线，分别对应 `congruent_left`、`congruent_right`、`incongruent_left`、`incongruent_right`，便于直接比较四种具体刺激文本。
- 阶段标签明确写成 `Fixation`、`Flanker Response`、`ITI`，避免过度压缩导致语义不清。
- `ITI` 使用文本注释作为最后手段，因为该阶段本身没有可视刺激。

## 6. 渲染参数与约束

- output_file: task_flow.png
- dpi: 300
- max_conditions: 4
- screens_per_timeline: 3
- screen_overlap_ratio: 0.1
- screen_slope: 0.08
- screen_slope_deg: 25.0
- screen_aspect_ratio: 1.4545454545454546
- qa_mode: local
- auto_layout_feedback:
  - layout pass 1: no adjustment needed; left=0.055, right=0.055, blank=0.162
- auto_layout_feedback_records:
  - pass: 1
    metrics: {'left_ratio': 0.0549, 'right_ratio': 0.0549, 'blank_ratio': 0.1615}
    vision_model: None
    issues: []
    adjustments: {}

## 7. 输出文件与校验和

- E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000004-flanker\references\task_plot_spec.yaml: sha256=f7dfe4a086977ad5d8a7963a1191c9dfb556cda57a1206e40b5a418d45ef2543
- E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000004-flanker\references\task_plot_spec.json: sha256=75fb33a8b6b91c7a607db5e4c9eb56012c0eb696dbab6f2c57f608c31af8685d
- E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000004-flanker\references\task_plot_source_excerpt.md: sha256=be9abd9b8a48b0042f2043de062ce15314ec3666f7ebf36463dcc2e8e5a2ef72
- E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000004-flanker\task_flow.png: sha256=7c6f0b0f12e9760a9f8f6511878c2d76941fa91cd96045f507b6a868b0ad735b

## 8. 推断/不确定项

- `ITI` 阶段是从 `show()` 调用中补回的，属于最终修正项，不再视为不确定。
- 其余流程与时间、响应窗口均可直接由 `run_trial.py` 和 `config/config.yaml` 解释。
