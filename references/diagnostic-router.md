# Diagnostic Router

> Part of Photo Material Intervention · original methodology by [Pilipala9919](https://github.com/Pilipala9919/photo-material-intervention) · CC BY 4.0.

Use this router before writing any generation or edit prompt. Image understanding is performed by the active vision-capable model; `scripts/inspect_image.py` supplies technical geometry only and must not be treated as semantic diagnosis.

## Diagnostic contract

Inspect the actual source image and produce this compact record:

```yaml
diagnosis:
  subject_relationship: ""
  image_intent: documentary | portrait | landscape | social-memory | art-ready | unclear
  anchors_to_lock: []
  dominant_structure: ""
  atmosphere_and_light: ""
  primary_problem: none | technical | framing | weak-hierarchy | obstruction | fidelity-risk | unclear-subject
  secondary_problems: []
  native_triggers: []
  obstruction_candidates:
    - element: ""
      remove: yes | no | uncertain
      reason: ""
      reconstruction_risk: low | medium | high
  route: HOLD | PHOTO_PREP | CLEAN_BASE | DIRECT_INTERVENTION | ASK
  route_confidence: 0.0
  next_action: ""
  success_condition: ""
```

Do not invent details that are not visually supported. Distinguish observation from inference.

## Route selection

Evaluate in this order; the first decisive condition wins.

### ASK — ambiguity or unacceptable risk

Choose `ASK` and pause before editing when any applies:

- `route_confidence < 0.75`;
- two plausible subjects would require materially different treatments;
- the requested edit could remove or alter a person, face, body, text, artwork, logo, cultural object, or documentary evidence;
- a large hidden area lacks enough surrounding geometry for conservative reconstruction;
- source resolution or corruption prevents reliable diagnosis.

Ask one focused question and give at most two concrete routes. Do not ask for vague aesthetic preferences that can be inferred from the image and request.

### HOLD — preserve photography

Choose `HOLD` when the image is already visually resolved, no source-native trigger supports a meaningful intervention, or transformation would weaken documentary/emotional truth. Explain why no mixed-media edit is justified. If useful, offer a restrained photographic correction, but do not force a recipe.

### PHOTO_PREP — correct before re-diagnosis

Choose `PHOTO_PREP` when exposure, white balance, haze, crop, perspective, noise, or local hierarchy prevents a fair reading of the subject, but no major object reconstruction is needed.

Make only reversible-looking photographic corrections. Lock people, object count, geometry, weather, and meaningful imperfections. Re-run the full diagnosis on the corrected image; never assume it should automatically receive a material intervention.

### CLEAN_BASE — remove a genuine obstruction first

Choose `CLEAN_BASE` when an element has high visual weight and obstruction cost, low subject/narrative value, and reconstructable surroundings. Follow [obstruction removal](obstruction-removal.md).

Generate only the documentary clean base. Check it against Stage A acceptance criteria. If it fails, repair or stop. After it passes, re-run diagnosis using the clean base, then select `HOLD`, `PHOTO_PREP`, or `DIRECT_INTERVENTION`. Never combine substantial removal and stylization in one generation.

### DIRECT_INTERVENTION — source is ready

Choose `DIRECT_INTERVENTION` only when:

- the subject relationship is clear;
- important anchors can be locked;
- no unresolved obstruction blocks the subject;
- at least one visible native trigger supports a physical verb;
- the event can be expressed in one concrete sentence;
- fidelity risk is controllable.

Then select a verified recipe or compile a new source-specific mechanism.

## Continuation policy

Before the first edit tool call, show the user a concise diagnosis containing:

1. what the photograph is really about;
2. what must remain unchanged;
3. the main problem, if any;
4. the selected route and why;
5. the exact next action.

Continue automatically when confidence is at least 0.75 and the route is `HOLD`, `PHOTO_PREP`, or `DIRECT_INTERVENTION`. For `CLEAN_BASE`, continue automatically only when removal does not affect people, identity, readable text, cultural objects, or documentary evidence; otherwise use `ASK`.

If the user explicitly requests “diagnose only,” stop after the diagnosis. If the user explicitly approves autonomous processing, still obey fidelity and Stage A quality gates.

## Route transitions

```text
SOURCE
  ├─ ASK ── user answer ──> re-diagnose SOURCE
  ├─ HOLD ────────────────> deliver diagnosis / optional photo-only advice
  ├─ PHOTO_PREP ──────────> inspect corrected image ──> re-diagnose
  ├─ CLEAN_BASE ──────────> Stage A gate ──> re-diagnose clean base
  └─ DIRECT_INTERVENTION ─> artwork gate ──> accepted still ──> optional motion
```

No stage may skip its acceptance gate. Every re-diagnosis may choose a different route.

## Three reference decisions

- A watcher framed by a doorway, with no blocking object and a strong outside/inside boundary → `DIRECT_INTERVENTION`; preserve watcher and doorway, consider Portal Woodcut.
- Painted tree trunks hidden by a visually dominant temporary canopy → `CLEAN_BASE`; remove only the canopy, validate reconstructed trunks and ground, re-diagnose, then consider Paint-Stop Charcoal.
- A busy lawn under a broad, legible light boundary → usually `DIRECT_INTERVENTION`; preserve people and silhouettes, consider Sunlight Screenprint. If the light boundary is weak, choose `HOLD` rather than forcing the recipe.
