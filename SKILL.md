---
name: photo-material-intervention
version: 1.3.0
author: Pilipala9919
homepage: https://github.com/Pilipala9919/photo-material-intervention
license: CC-BY-4.0
description: Diagnose a real photograph and choose the smallest effective treatment—hold, photographic edit, cleanup, narrative transformation, or source-specific material intervention—according to its subject, scene, emotional asset, visual problem, fidelity risk, and publishing goal. Use when a user wants a strong photo treatment without preset filters, especially for people, architecture, landscape, street scenes, objects, cultural heritage, or social-media concepts.
---

# Photo Material Intervention

> Original methodology by **Pilipala9919** · [canonical repository](https://github.com/Pilipala9919/photo-material-intervention) · documentation under [CC BY 4.0](LICENSE).

Decide **what this photograph needs before deciding how it should look**. The goal is not to add art. The goal is to strengthen the photograph's subject, feeling, story, or visual event with the least unnecessary invention.

## Non-negotiable rule

Never add a filter, paper, ink, frame, drawing, portal, glow, or other device merely because the image contains an empty area or recognizable object. A treatment is valid only when it reveals or intensifies a relationship already present in the source.

## Fast workflow

### 1. Diagnose once

Read [diagnostic router](references/diagnostic-router.md). Identify only:

- **subject** — the person, relationship, place, action, object, or atmosphere that matters;
- **asset** — emotion, gesture, structure, weather, light, texture, use, memory, or coincidence;
- **problem** — technical weakness, distraction, obstruction, weak hierarchy, absent tension, or none;
- **risk** — identity, text, architecture, cultural evidence, hidden geometry, or object count;
- **goal** — faithful photograph, personal memory, art image, or social reach.

Show the user a compact diagnosis and select exactly one route:

- `HOLD` — no edit is justified;
- `PHOTO_EDIT` — tonal, color, crop, perspective, or hierarchy correction only;
- `CLEANUP` — remove one genuine distraction or obstruction;
- `NARRATIVE_TRANSFORM` — create one source-derived event that changes how the scene is read;
- `MATERIAL_TRANSFORM` — use one physical medium because the photographed surface or condition naturally causes it;
- `ASK` — one focused question is necessary for safety or subject choice.

Do not perform a preparation pass unless a technical defect actually prevents the subject from reading.

### 2. Pass the meaning and reach gate

Before any generative edit, answer:

1. What is already worth looking at?
2. What single visible event will make it more meaningful or surprising?
3. Why does that event belong to this exact photograph?
4. Why would someone stop, feel, wonder, or share?

For social-reach work, all four answers must be concrete. If question 3 or 4 has no convincing answer, choose `HOLD` or `PHOTO_EDIT`. Do not generate a decorative concept to fill the gap.

A static scene is not automatically a transformation candidate. Architecture without human use, temporal contrast, weather tension, unusual scale, or a source-native action is usually documentary photography—not a canvas for an attached art object.

### 3. Execute the selected route

#### `HOLD`

Explain in one sentence why restraint protects the image. Do not create a concept image.

#### `PHOTO_EDIT`

Use non-generative or tightly locked corrections. Preserve identity, text, object count, geometry, weather, and meaningful imperfections. Stop after one accepted edit.

#### `CLEANUP`

Read [obstruction removal](references/obstruction-removal.md). Remove only an element with high obstruction cost and low narrative value. Use one clean-base generation, inspect reconstruction, and stop unless the user also requested transformation. Never hide reconstruction under style.

#### `NARRATIVE_TRANSFORM`

Change one relationship rather than the whole style. Valid mechanisms include light revealing a subject, weather erasing or exposing distance, a reflection disagreeing with reality, motion leaving source-shaped evidence, scale becoming legible, or foreground and background exchanging information. Preserve at least one strong photographic anchor.

#### `MATERIAL_TRANSFORM`

Read [medium selection](references/medium-selection.md) and [prompt compiler](references/prompt-compiler.md). Use only when a real source condition physically motivates a process: rain can transfer, fog can erase, sunlight can expose, a painted edge can hand off, and a portal can separate. Recipes are optional evidence, never defaults.

### 4. Generate once, then judge

Compile one concept and make one generation. Read [quality gate](references/quality-gate.md).

- One local execution defect → allow one local repair.
- Altered identity, text, architecture, or documentary evidence → reject.
- Weak concept, generic effect, or no sharing reason → stop and explain; do not keep generating variations.

Default budget: **one diagnosis, one strategy, one generation, at most one local repair**. Ask before exceeding it.

### 5. Add motion only when the still works

For requested social content, read [motion design](references/motion-design.md). Animate the source-derived action, not a generic before/after dissolve.

## Subject-specific priorities

| Source type | Protect first | Prefer | Usually avoid |
|---|---|---|---|
| person / relationship | face, body, gesture, distance | emotion, interaction, light, motion evidence | transforming identity or decorating empty background |
| architecture / heritage | geometry, text, patina, use | structure, scale, human passage, time/light/weather | floating paper, generic ink, fantasy ornament |
| landscape / weather | horizon, terrain, atmosphere | visibility, season, water, wind, light as action | unrelated objects or total style transfer |
| street / crowd | timing, count, gesture, coincidence | rhythm, trails, repeated action, selective hierarchy | beautifying away useful disorder |
| object / still life / food | form, function, texture | use, wear, cut, reflection, material response | arbitrary surrealism unrelated to the object |
| text / sign / artwork | exact content and authorship | documentary correction or non-text surroundings | any generative redraw of protected content |

## Delivery

Return only:

1. route and one-sentence reason;
2. accepted output, if an edit was justified;
3. what was preserved, removed, or inferred;
4. one important limitation;
5. optional motion idea only when requested.

Never present a technically polished but conceptually weak image as successful.

## Attribution and privacy

Preserve `NOTICE`, `LICENSE`, and the canonical link when distributing or substantially adapting this methodology. Do not silently watermark user outputs or claim ownership of source photographs. Do not publish private photos, faces, EXIF location, filenames, or paths without permission.
