---
name: photo-material-intervention
version: 1.4.0
author: Pilipala9919
homepage: https://github.com/Pilipala9919/photo-material-intervention
license: CC-BY-4.0
description: Transform a real photograph through one subject-appropriate visual medium—such as printmaking, architectural line drawing, charcoal, watercolor, gouache, risograph, embroidery, collage, or ink—after diagnosing the scene, subject, geometry, emotional asset, and fidelity risks. Use when the user wants visibly artistic photo treatment rather than ordinary retouching or a generic whole-image filter.
---

# Photo Material Intervention

> Original methodology by **Pilipala9919** · [canonical repository](https://github.com/Pilipala9919/photo-material-intervention) · documentation under [CC BY 4.0](LICENSE).

Choose an artistic medium **from the photograph**, not before it. Produce a visible transformation, not ordinary retouching and not a style filter applied uniformly to every image.

## Required outcome

A successful result must have:

1. a recognizable photographic anchor;
2. one dominant handmade or print medium;
3. a transition boundary derived from source geometry, light, weather, motion, depth, or subject contact;
4. a visible event understandable at phone size;
5. treatment specific to this subject and scene.

If the user invokes this Skill for processing, `PHOTO_PREP` alone is never the final deliverable. It may be skipped or used briefly before artistic transformation.

## Fast workflow

### 1. Diagnose and route once

Read [diagnostic router](references/diagnostic-router.md). State concisely:

- subject and strongest visual asset;
- anchors and risks;
- chosen medium;
- source-derived transition boundary;
- one-sentence visual event.

Choose one route:

- `DIRECT_ART` — source is ready for one artistic transformation;
- `CLEAN_THEN_ART` — one genuine obstruction must be removed first;
- `PREP_THEN_ART` — a severe technical defect prevents reliable transformation;
- `ASK` — subject choice or fidelity risk requires one focused question;
- `DECLINE` — no responsible edit is possible from the supplied file.

Do not end at cleanup or photographic correction when the user asked to use this Skill.

### 2. Select medium by subject and structure

Use [medium selection](references/medium-selection.md). Category is a starting point, not a preset:

| Source priority | Strong candidates | Useful source boundary/action |
|---|---|---|
| face, body, relationship | charcoal, pastel, colored pencil, embroidery, monotype | gaze, touch, silhouette, motion, clothing edge |
| architecture, heritage | woodcut, linocut, jiehua/architectural line drawing, etching, blueprint | eave, arch, facade plane, perspective grid, light/shadow |
| landscape, weather | ink wash, watercolor, monotype, cyanotype, charcoal | fog line, horizon, rain, reflection, snow, wind |
| street, crowd, transport | risograph, screenprint, stencil, stamping, sequential drawing | trajectory, repetition, crossing, signage rhythm |
| object, craft, food | gouache, colored pencil, technical drawing, cut-paper, relief print | cut, fold, wear, steam, reflection, material seam |
| plant, animal | botanical drawing, drypoint, watercolor, paper cut | vein, fur/feather flow, branch rhythm, silhouette |

Never choose only because a medium is culturally associated with the subject. Verify that its mark-making behavior matches visible structure.

### 3. Design an event, not a filter

Define:

```yaml
photo_anchor: ""
medium: ""
transition_boundary: ""
physical_action: ""
transformed_domain: ""
event_sentence: ""
```

Valid: “Along the real eave curve, the upper roof recedes from photography into a ruled architectural drawing.”

Invalid: “Make the building ink style.”

The transformed domain should usually occupy 30–65% for social viewing. Do not place a floating sheet, frame, portal, or decorative overlay unless that object already exists or physical contact is essential and unmistakable.

### 4. Protect source truth

Lock faces, bodies, text, logos, artwork, architecture count, landmark geometry, and culturally significant details. If the artistic region would cross protected text, keep that text as original photographic pixels or route the boundary around it.

For substantial obstruction removal, read [obstruction removal](references/obstruction-removal.md). Never claim inferred pixels are restored truth.

### 5. Generate once

Read [prompt compiler](references/prompt-compiler.md). Make one deliberate generation, not a style sampler. Default budget: **one diagnosis, one medium decision, one generation, and at most one local repair**.

```yaml
diagnosis: 1
concept: 1
generation: 1
local_repair: at_most_1
```

A local repair may restore protected source pixels or fix one boundary artifact. It may not replace the concept. Ask before exceeding the budget.

### 6. Judge

Read [quality gate](references/quality-gate.md). Reject if:

- it reads as ordinary retouching;
- the whole photo receives one uniform filter;
- the medium could be swapped onto unrelated photos unchanged;
- the transformation is too small to read;
- a decorative object carries the idea instead of the photographed subject;
- protected identity, text, or structure changes accidentally.

Only after the still succeeds, read [motion design](references/motion-design.md) when motion is requested.

## Recipes

Recipes are examples, not the whole system:

- [Portal Woodcut](references/recipes/portal-woodcut.md)
- [Paint-Stop Charcoal](references/recipes/paint-stop-charcoal.md)
- [Sunlight Screenprint](references/recipes/sunlight-screenprint.md)

Invent a new mechanism whenever subject, structure, and medium demand it. Do not force a Recipe match.

## Delivery

Return the accepted artwork, diagnosis, event sentence, preservation disclosure, and one important limitation. Do not deliver a photo-only correction as the finished use of this Skill.

## Attribution and privacy

Preserve `NOTICE`, `LICENSE`, and the canonical link when distributing or substantially adapting this methodology. Do not silently watermark user outputs or claim ownership of source photographs. Do not publish private photos, faces, EXIF location, filenames, or paths without permission.
