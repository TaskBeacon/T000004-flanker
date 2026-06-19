Use case: infographic-diagram
Asset type: TaskBeacon task flow diagram
Primary request: Create a clean, publication-ready task flow diagram as a timeline collection for the behavioral task described below.

Task: Flanker Task
Construct: attention / cognitive control
Rows/conditions:
- Congruent Left: all arrows point left; center target left; press f
- Congruent Right: all arrows point right; center target right; press j
- Incongruent Left: flankers point right, center target left; press f
- Incongruent Right: flankers point left, center target right; press j

Timeline phases:
- Congruent Left: Fixation (+; 500 ms; no response) -> Flanker (<<<<<; up to 1000 ms; press f) -> ITI (blank; 800-1200 ms)
- Congruent Right: Fixation (+; 500 ms; no response) -> Flanker (>>>>>; up to 1000 ms; press j) -> ITI (blank; 800-1200 ms)
- Incongruent Left: Fixation (+; 500 ms; no response) -> Flanker (>><>>; up to 1000 ms; press f) -> ITI (blank; 800-1200 ms)
- Incongruent Right: Fixation (+; 500 ms; no response) -> Flanker (<<><<; up to 1000 ms; press j) -> ITI (blank; 800-1200 ms)

Visual requirements:
- White background, landscape orientation, crisp dark text, restrained condition accent colors.
- One horizontal row per condition or representative trial type.
- Each row contains exactly 3 participant-screen snapshots connected by a subtle arrow.
- Each screen snapshot shows the visible stimulus, not internal variable names.
- Use gray participant-screen boxes, thin black arrows, consistent row spacing, and subtle row separators.
- Place timing labels under each screen in compact text.
- Place condition labels at the left of each row.
- Use short labels only; avoid paragraphs inside the image.
- Make all text legible at normal document preview size.
- Leave a clean blank header band across the top 15-18% of the image. This band is reserved for a fixed title, `Construct: ...` subtitle, and TaskBeacon logo lockup that will be added after generation.

Accuracy constraints:
- Do not invent phases, stimuli, condition names, keys, rewards, feedback, or timings.
- Do not add people, lab equipment, decorative scenes, logos, or unrelated icons.
- Do not draw the task title, construct subtitle, any logo, watermark, brand mark, or `TaskBeacon` text inside the generated image.
- Draw only the timeline content below the blank header band.
- If a detail is unknown, omit it rather than guessing.
- Preserve these exact terms where used: Congruent Left, Congruent Right, Incongruent Left, Incongruent Right, <<<<<, >>>>>, >><>>, <<><<, f, j, 500 ms, 1000 ms, 800-1200 ms, ITI.
- Show `f` only for left target trials and `j` only for right target trials.

Style:
TaskBeacon scientific infographic style: clean vector-like raster image, organized spacing, gray screen boxes, restrained color accents, and a blank header-safe area.
