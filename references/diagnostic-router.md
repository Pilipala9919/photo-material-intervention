# Diagnostic Router

> Part of Photo Material Intervention · original methodology by [Pilipala9919](https://github.com/Pilipala9919/photo-material-intervention) · CC BY 4.0.

Use vision to understand the actual photograph. `scripts/inspect_image.py` reports geometry only; it cannot identify subject or meaning.

## Compact record

```yaml
subject: ""
asset: ""
problem: none | technical | distraction | obstruction | weak-hierarchy | absent-tension | ambiguous
risk: []
goal: faithful-photo | memory | art | social-reach
route: HOLD | PHOTO_EDIT | CLEANUP | NARRATIVE_TRANSFORM | MATERIAL_TRANSFORM | ASK
confidence: 0.0
reason: ""
next_action: ""
```

Show this record in natural language before the first tool call. Separate visible observation from inference.

## Decision order

### 1. `ASK`

Use only when confidence is below 0.75, two subjects imply incompatible edits, or treatment may alter a person, protected text/artwork, cultural evidence, or unreconstructable hidden geometry. Ask one focused question with at most two concrete options.

### 2. `HOLD`

Use when the photograph is already resolved or when no edit would strengthen its subject, feeling, story, or visual hierarchy. Also use when a proposed transformation has no source-specific cause or sharing reason.

### 3. `PHOTO_EDIT`

Use when exposure, color, crop, perspective, noise, or local hierarchy is the real limitation. It is a final route, not automatically preparation for art. Prefer deterministic editing over generative redraw.

### 4. `CLEANUP`

Use when one element has high visual weight and obstruction cost, low subject/story value, and conservatively reconstructable surroundings. Do not remove useful mess or documentary evidence. After cleanup, stop unless transformation was explicitly requested and still has a valid meaning/reach case.

### 5. `NARRATIVE_TRANSFORM`

Use when a visible source relationship supports a surprising event without requiring a handmade-medium metaphor. The event must change how the scene is read and remain describable without style words.

Examples:

- a reflection shows a different moment already implied by the subject;
- hard light reveals the path or person that the composition points toward;
- motion leaves traces that preserve real trajectories;
- fog erases depth while one real anchor resists it.

Reject added props, floating art surfaces, decorative portals, or generic surrealism.

### 6. `MATERIAL_TRANSFORM`

Use only when source matter and artistic process have physical affinity. Require a real trigger, physical verb, contact zone, preserved anchor, and one-sentence event. Finding a doorway, fog, sun, water, or texture is not sufficient by itself.

## Subject routing

- **Person/relationship:** read gesture, gaze, distance, touch, absence, and action before background aesthetics.
- **Architecture/heritage:** read structure, use, age, scale, passage, light, weather, and cultural text. Static documentation normally routes to `PHOTO_EDIT` or `HOLD`.
- **Landscape/weather:** read depth, horizon, visibility, season, water and atmospheric movement.
- **Street/crowd:** read timing, repeated rhythm, collision, direction and social evidence.
- **Object/food:** read function, wear, surface, cut, heat, reflection and transformation of matter.
- **Protected text/art:** lock content; do not use generative editing across it.

## Meaning and reach gate

For `NARRATIVE_TRANSFORM` or `MATERIAL_TRANSFORM`, require four concrete answers:

```yaml
worth_seeing: ""
visible_event: ""
belongs_here_because: ""
stop_or_share_because: ""
```

If `belongs_here_because` is merely “there is space” or “the style matches,” reject. If `stop_or_share_because` relies on an explanation rather than visible tension, reject.

## Time budget

Default execution budget:

```yaml
diagnoses: 1
strategies: 1
generations: 1
local_repairs: 1
```

Do not repeatedly generate to rescue a weak concept. A local repair may correct masking, edge contact, or one artifact; it may not replace the strategy. Ask before exceeding the budget.

## Current-photo example: static heritage facade

A sunlit heritage facade with legible roof structure but no human action, weather event, temporal contrast, or source-native transformation should route to `PHOTO_EDIT` if tonal hierarchy is weak, otherwise `HOLD`. Do not attach floating xuan paper, ink, portals, or fantasy ornament merely to create novelty. Recommend a stronger source frame—human passage, ritual use, rain, shadow movement, restoration traces, or old/new contrast—if social reach is the goal.
