# Task Plot Review

Review checklist source: `E:/Taskbeacon/skills/task-plot/references/review_checklist.md`.

## Evidence Match

- Pass: task name matches `Flanker Task`.
- Pass: rows match congruent/incongruent left/right conditions.
- Pass: phase order matches `src/run_trial.py`: fixation, flanker response window, ITI.
- Pass: timing labels match config: 500 ms fixation, up to 1000 ms flanker response, 800-1200 ms ITI.
- Pass: response mapping is correct: `f` for left target trials and `j` for right target trials.

## Visual Quality

- Pass: fixed title and `Construct: attention / cognitive control` subtitle are centered in the header.
- Pass: fixed TaskBeacon logo lockup is borderless in the top-right corner and does not overlap content.
- Pass: arrow strings are readable for congruent and incongruent conditions.
- Pass: text is readable and no generated extra title, subtitle, logo, watermark, people, or devices are present.
- Pass: `references/task_plot_timeline_raw.png` preserves the generated timeline before header/logo post-processing.

## README Embed

- Pass: `README.md` contains `## 2. Task Flow`.
- Pass: the first image under `## 2. Task Flow` is exactly `![Task Flow](task_flow.png)`.
- Pass: final image is saved at the task root as `task_flow.png`.
