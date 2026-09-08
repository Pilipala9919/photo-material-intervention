# Diagnostic Router

> Part of Photo Material Intervention · original methodology by [Pilipala9919](https://github.com/Pilipala9919/photo-material-intervention) · CC BY 4.0.

Use vision to choose a subject-specific artistic treatment. Technical inspection cannot identify meaning or medium.

## Compact diagnosis

```yaml
subject: ""
visual_asset: ""
anchors_to_lock: []
risks: []
medium_candidates: []
chosen_medium: ""
medium_reason: ""
transition_boundary: ""
event_sentence: ""
route: DIRECT_ART | CLEAN_THEN_ART | PREP_THEN_ART | ASK | DECLINE
confidence: 0.0
```

Show a short natural-language version before editing.

## Route

- `DIRECT_ART`: source subject and geometry are readable; generate the selected treatment.
- `CLEAN_THEN_ART`: a genuine low-value obstruction blocks the subject. Remove it conservatively, verify, then use the already-selected artistic direction.
- `PREP_THEN_ART`: only for severe exposure, color, crop, or perspective defects that prevent visual understanding. Preparation is not a final output.
- `ASK`: confidence below 0.75, competing subjects imply incompatible work, or a person/protected text/artwork/cultural detail may be altered.
- `DECLINE`: resolution, corruption, or unsupported reconstruction makes responsible treatment impossible.

## Subject-to-medium reasoning

Choose by both subject and mark affinity:

### Person / relationship

Prioritize gesture, gaze, touch, distance, posture, clothing and motion. Use charcoal for weight and absence; pastel/pencil for intimacy; monotype for memory or doubling; embroidery when seams, clothing or connection lines physically support it. Preserve faces and bodies photographically unless the user explicitly requests portrait transformation.

### Architecture / heritage

Prioritize geometry, construction logic, age, scale, light and use. Use:

- woodcut/linocut for strong mass, silhouette and carved rhythm;
- jiehua or technical line drawing for layered roofs, perspective and construction order;
- etching/drypoint for dense ornament and weathered surface;
- blueprint only when construction, restoration or plan/elevation logic is visible.

Route boundaries along eaves, arches, facade planes, perspective axes or real shadows. Lock text and culturally significant ornament. Do not add generic rice paper, floating prints or fantasy decoration.

### Landscape / weather

Prioritize depth, horizon, terrain, water, season and atmospheric movement. Use ink wash/watercolor for diffusion, charcoal for erasure and density, monotype for transfer/reflection, cyanotype for hard light or botanical silhouettes. Transition along fog, rain, shoreline, horizon or light—not arbitrary gradients.

### Street / crowd / transport

Prioritize timing, repetition, crossing, trajectory and sign rhythm. Use screenprint/risograph for flat social color and registration, stencil for repeated urban forms, stamping or sequential drawing for movement. Preserve person count and protected signs.

### Object / craft / food

Prioritize function, handling, wear, cut, fold, heat, steam, glaze and reflection. Use gouache for mass and color, pencil/technical drawing for construction, cut-paper for layers, relief print for texture. The transformation should emerge from a seam, cut, reflection or material change.

### Plant / animal

Prioritize vein/branch rhythm, silhouette, fur, feather, growth and movement. Use botanical drawing, drypoint, watercolor or paper cut according to edge and texture. Preserve species-defining anatomy.

## Selection checks

A chosen medium passes only if:

1. its native marks correspond to visible structure;
2. the transition follows an existing boundary or contact;
3. the subject—not an added decorative prop—carries the event;
4. the treatment differs materially from what another source category would receive;
5. the event is visible at 360 px width.

If several media pass, choose the one with the clearest physical boundary and lowest fidelity risk. Do not present a style menu unless the user asks.

## Example: layered heritage facade

For a sharply visible facade with layered flying eaves, dense brackets, circular windows and protected calligraphy:

```yaml
chosen_medium: precise architectural etching / jiehua line drawing
photo_anchor: sky, trees and garden context
transformed_domain: 70–100% of the complete visible building body
ground: warm mineral-paper tone clipped to the building silhouette
transition_boundary: the complete outer building silhouette and ground-contact edge
event_sentence: "The whole temple becomes a single measured architectural plate while its living garden remains photographic."
route: DIRECT_ART
```

This is preferable to a floating rubbing or a horizontal half-photo/half-drawing split because the building remains one coherent subject.

## Time budget

One diagnosis, one medium decision, one generation, and at most one source-pixel restoration or local boundary repair. Do not generate multiple styles to discover the idea.
