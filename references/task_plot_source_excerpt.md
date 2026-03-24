# 源证据摘录（Flanker Task）

## 输入文件
- README: `E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000004-flanker\README.md`
- Config: `E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000004-flanker\config\config.yaml`
- run_trial: `E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000004-flanker\src\run_trial.py`

## 选定条件
- `congruent_left`
- `congruent_right`
- `incongruent_left`
- `incongruent_right`

## 说明
- 时间线以 `run_trial.py` 中的 `set_trial_context(...)` 调用顺序为主。
- `ITI` 阶段来自 `make_unit(unit_label="iti").show(...)`，属于参与者可见的空白间隔，初版推断容易遗漏，因此在最终规范中手工补回。
