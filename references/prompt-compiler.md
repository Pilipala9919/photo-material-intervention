# Prompt Compiler

Write the final image-edit prompt in this order.

## 1. Output and truth lock

- edit the supplied photograph;
- preserve exact crop/aspect unless reframing is intentional;
- name protected people, objects, geometry, weather, and viewpoint;
- request no text by default.

## 2. Photographic anchor

Name what stays clearly photographic and why it carries reality, identity, emotion, or scale. Use concrete objects and positions.

## 3. Material event

State one sentence:

> [Trigger] [physical verb] [domain] into [medium], while [anchor] stays photographic.

Then locate the domain using visible source geometry—not generic “upper half” alone.

## 4. Material behavior

Specify 4–7 process facts, such as:

- relief gouges, ink pressure, unprinted cuts;
- vine-charcoal rub, broken tip, finger smudge, kneaded erasure;
- flat ink plates, mesh, squeegee skip, registration drift;
- wet transfer, pooling, tide line, capillary edge.

## 5. Contact zone

Describe one or two ways the media touch:

- foreground leaves cross the transformed region;
- print marks reflect in existing puddles;
- charcoal catches in bark grooves;
- cast shadows remain photographic over printed ground;
- ink deposits collect on an existing edge.

Contact must use real source geometry.

## 6. Scale and hierarchy

State intervention percentage, thumbnail readability, and dominant/secondary relationship. Large intervention requires a protected anchor.

## 7. Strict negatives

Ban only relevant failures:

- changed people/objects;
- global filter/full redraw;
- straight split or separate panel;
- wrong species/architecture;
- invented symbols/text;
- unrelated media;
- UI/watermark.

## Locked prompt skeleton

```text
Edit the supplied [orientation] photograph into one integrated [photography + medium] artwork with no text.

Preserve [exact anchors and geometry]. Do not alter [risk regions].

One visual event: because [source trigger], [physical action] transforms [source-defined domain] into [medium]. Keep [anchor] truthful photography. Intervention: [percentage].

Material behavior: [process facts]. Preserve [source structure] through the transformation.

At [real contact zone], let [specific physical interaction] connect both media.

Immediate statement: “[concrete event sentence].” [mood].

No [relevant failure list].
```

## Editing discipline

Generate from the original or accepted clean base. If identity preservation is critical, composite accepted generated regions back onto the original using masks rather than treating a full-image model output as ground truth.
