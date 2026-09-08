# Visual Diagnosis

## 1. Name the subject relationship

Use one sentence with a noun, action/tension, and environment. Prefer:

- “a seated watcher looking from a dark room toward a rain-cleared mountain”
- “human-painted pine trunks disappearing into an unpainted fog canopy”
- “families crossing a sunlit lawn while one yellow balloon anchors the foreground”

Do not use an object list.

## 2. Build the evidence map

Record:

- **identity anchors**: face/body, posture, landmark geometry, exact object relation, species, distinctive color, viewpoint;
- **structure**: frame, axis, slope, horizon, repeated rhythm, light boundary, occlusion;
- **atmosphere**: fog density, rain, reflection, hard sun, shadow, glass, steam;
- **negative space**: darkness, sky, fog, wall, grass, water;
- **risk regions**: people, hands, text, architecture, repeated trunks, hidden areas.

## 3. Score visual elements

Score each major element 0–3:

- subject relevance;
- narrative value;
- visual weight;
- obstruction cost;
- reconstruction risk.

A likely obstruction has high visual weight and obstruction cost, but low subject relevance and narrative value. High reconstruction risk may still require retention.

## 4. Find native triggers

A valid trigger already exists in the photograph and suggests physical behavior:

- doorway/window → separates worlds;
- fog/steam → conceals, lifts, erases, exposes;
- rain/puddle → bleeds, transfers, reflects, develops;
- sunlight/shadow → exposes, burns, prints, reveals;
- paint endpoint → hands off from color to another medium;
- glass/mirror → doubles, registers, refracts;
- motion/crowd rhythm → trails, stamps, repeats.

Reject triggers invented only after selecting a favorite style.

## 5. Preflight decision

Before generation, produce the full user-visible diagnostic record required by [diagnostic router](diagnostic-router.md), including a single route and next action. At minimum, populate:

```yaml
subject_relationship:
anchors_to_lock: []
primary_problem:
obstructions:
  remove: []
  weaken: []
  preserve: []
clean_base_required: false
native_triggers: []
route: HOLD | PHOTO_PREP | CLEAN_BASE | DIRECT_INTERVENTION | ASK
route_confidence:
trigger:
medium:
action:
domain:
contact_zone:
event_sentence:
risks: []
next_action:
success_condition:
```

For `HOLD`, `PHOTO_PREP`, `CLEAN_BASE`, or `ASK`, leave medium-event fields blank until a later diagnosis selects `DIRECT_INTERVENTION`. If `event_sentence` cannot be concrete and source-specific, do not intervene; select `HOLD` or diagnose again.
