---
name: photo-material-intervention
description: Art-direct a real photograph into a high-impact, source-specific mixed-media artwork by first diagnosing the photographic subject, removing genuine obstructions when necessary, then letting a photo-native boundary such as a doorway, fog, sunlight, water, shadow, glass, paint edge, or motion trigger one coherent handmade medium. Use for photography fused with woodcut, charcoal, screenprint, cyanotype, drawing, monotype, or another physically motivated medium; for AI art transformations with strong mobile impact; for Douyin-ready visual concepts and motion plans; and when ordinary retouching, global style transfer, diptychs, decorative overlays, or generic filters are not enough.
---

# Photo Material Intervention

Create an artwork that still needs the supplied photograph. Do not choose a style first. Diagnose the image, protect its evidence, remove only genuine obstructions, and design one visible material event that could not belong to an arbitrary photo.

## Core Standard

A successful result must satisfy all five:

1. **One-second anomaly** — the intervention reads at mobile-thumbnail size without explanation.
2. **One-sentence event** — describe what happens in concrete language, not style jargon.
3. **Source specificity** — the mechanism depends on structures, weather, light, color, or relationships actually present in this photograph.
4. **Photographic anchor** — preserve at least one important region as truthful photography.
5. **Animatable action** — the transformation can occur through a physical verb such as carve, rub, expose, print, wipe, bleed, lift, or register.

Reject work that needs a long artist statement to become interesting.

## Required Workflow

### 1. Inspect before prompting

Read [visual diagnosis](references/visual-diagnosis.md). Identify:

- the real subject or subject relationship;
- two to five identity anchors that must remain;
- the strongest directional structure;
- foreground obstructions and competing elements;
- possible native boundaries or triggers;
- fidelity risks: faces, bodies, architecture, text, species, repeated objects, or occluded geometry.

State the subject as a relationship, not an inventory. Example: “a real seated watcher looking through a doorway at a rain-cleared mountain,” not “woman, chair, mountain, plants.”

### 2. Decide whether obstruction removal is necessary

Do not preserve every source pixel by default. Read [obstruction removal](references/obstruction-removal.md).

Remove an element only when it:

- materially blocks the intended subject;
- has high visual weight but little narrative value;
- breaks the subject's dominant rhythm or boundary;
- can be reconstructed conservatively from surrounding evidence.

If removal is substantial, use two separate generations:

1. make a clean documentary base with no stylization;
2. inspect the reconstruction;
3. only then perform material intervention.

Never hide bad reconstruction under art effects.

### 3. Compile a material event

Read [medium selection](references/medium-selection.md). Define exactly:

- **anchor** — what remains photographic;
- **trigger** — the existing visual fact that causes the change;
- **medium** — one primary handmade process;
- **action** — one physical verb;
- **domain** — where the intervention may occur;
- **contact** — where photography and medium physically meet;
- **scale** — enough area for one-second readability;
- **event sentence** — 8–20 concrete words.

Use one primary medium. A secondary mark is allowed only when materially subordinate and necessary for contact.

### 4. Choose a recipe or invent a new one

Use a verified recipe only when its eligibility conditions match:

- [Portal Woodcut](references/recipes/portal-woodcut.md) — a real doorway/window/arch divides the photographic observer from a transformed exterior or interior.
- [Paint-Stop Charcoal](references/recipes/paint-stop-charcoal.md) — real applied color ends on a subject and fog/darkness continues it in monochrome drawing; supports a clean-base stage.
- [Sunlight Screenprint](references/recipes/sunlight-screenprint.md) — a clear real light/shadow boundary turns a broad receiving plane into hand-pulled color while people or objects remain photographic.

Do not force a recipe. If none fits, create a new mechanism using the same compiler and record why it belongs to this source.

### 5. Generate with a locked prompt

Read [prompt compiler](references/prompt-compiler.md). The prompt must:

- name exact photographic anchors;
- explicitly forbid changes to high-risk identity regions;
- locate the intervention using source geometry;
- describe material behavior, not only a style name;
- define the transition/contact behavior;
- include relevant failure prohibitions;
- request no text by default.

Generate one concept image. Do not generate three random styles unless the user asks for variants.

### 6. Inspect and route corrections

Read [quality gate](references/quality-gate.md). Check at full size and thumbnail size.

Route failures correctly:

- wrong subject, weak event, arbitrary mechanism, bad obstruction decision → return to diagnosis;
- wrong boundary, weak photographic anchor, excessive intervention → recompile from the original or clean base;
- small material flaw → edit the current result locally;
- altered face/body, invented architecture, wrong species, repeated objects → reject; do not deliver as final.

Do not call a weak image “subtle.”

### 7. Design motion after the still succeeds

Only after the still passes, read [motion design](references/motion-design.md). Animate the material action rather than dissolving between before and after. Keep on-screen language conversational and first-person; keep technical terms out of subtitles unless the user asks for instruction.

## Creative Constraints

- Preserve the source's truth where it carries identity, emotion, or scale.
- Large intervention is allowed when anchored by a strong preserved photographic subject.
- Avoid fixed photo-plus-art panels, generic poster layouts, scrapbook devices, decorative doodles, and whole-image filters.
- Do not retain an ugly obstruction merely to invent a symbolic excuse for it.
- Do not remove useful mess, human evidence, or narrative context just to beautify the scene.
- Never invent unverified text, dates, places, logos, symbols, people, or culturally specific motifs.
- No imitation of named living artists or copying of external Skill prompts, layouts, examples, or proprietary reference systems.

## Default Deliverables

Return:

1. accepted concept image;
2. concise subject diagnosis;
3. one-sentence material event;
4. preservation/removal disclosure;
5. important generation limitations;
6. an optional 8–15 second motion concept when social publishing is requested.

Clearly label generated reconstruction as inferred, especially behind removed obstructions. Never claim generated pixels restore hidden reality.

## Privacy

Do not publish source photographs, generated outputs, EXIF location, faces, filenames, or private paths without explicit permission. For public Skill repositories, use only original diagrams or properly licensed assets.
