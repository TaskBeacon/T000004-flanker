# Task Plot Brief

## Evidence Sources

- `README.md`
- `main.py`
- `config/config.yaml`
- `src/run_trial.py`

## Header

- Title: Flanker Task
- Construct: attention / cognitive control

## Participant-Visible Flow

- Participants fixate, then respond to the direction of the center arrow in a five-arrow string.
- Correct response is `f` when the center arrow points left and `j` when it points right.
- Congruent trials have flankers pointing the same way as the target.
- Incongruent trials have flankers pointing opposite the target.
- ITI is a blank screen after the response window.

## Rows

- Congruent Left: `<<<<<`, press `f`.
- Congruent Right: `>>>>>`, press `j`.
- Incongruent Left: `>><>>`, center arrow left, press `f`.
- Incongruent Right: `<<><<`, center arrow right, press `j`.

## Timings

- Fixation: 500 ms.
- Flanker response window: up to 1000 ms.
- ITI: 800-1200 ms.

## Rendering Notes

- Use four horizontal rows with three snapshots each: fixation, flanker target, ITI.
- The generated raw image must contain only timeline content below a blank header band.
- The final title, `Construct: attention / cognitive control` subtitle, and TaskBeacon logo are added by post-processing.
