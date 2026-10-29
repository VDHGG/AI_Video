# TikTok AI Explainer Factory
## Project brief, prototype plan, toolchain, and production playbook

**Project owner:** User  
**Stakeholder:** Sếp Đức  
**Document status:** Consolidated working brief  
**Last updated:** 2026-10-27  
**Purpose:** Turn the brief and brainstorming into a practical, repeatable production system for short Vietnamese AI explainer videos.

---

## 1. Executive summary

Build a reusable production pipeline for **20–30 second TikTok AI explainer videos**. Each clip should teach one useful thing about AI, such as a privacy setting, a practical workflow, or a technical concept, in a short and visually clear format.

The visual style is a **hybrid of real product UI/screen recordings and polished motion graphics**. The aim is not merely to make one impressive clip; it is to establish a repeatable template so later clips can be produced by replacing the script, UI assets, voiceover, and episode configuration rather than rebuilding everything.

### Working production concept

1. **Research and fact-check** the topic using primary/official sources.
2. **Write the creative package:** hook, narration, storyboard, captions, and CTA.
3. **Capture authentic product UI** using screenshots or screen recording.
4. **Compose and render** with a reusable video template.
5. **Review and approve** factual accuracy, readability, timing, sound, and visual quality.
6. **Reuse the same template** for the next episode.

### Guiding principle

> AI can propose the content and help build the video. Important claims must be verified, real interfaces must be captured honestly, and a human must approve the final clip.

---

## 2. Original brief from sếp Đức

The original messages said, in substance:

- The TikTok channel does not yet have many tips-and-tricks videos.
- Example topics include enabling/disabling settings related to sharing data with a provider, to help viewers manage privacy.
- These videos should be **educational explainers**.
- Each clip should be around **20–30 seconds**.
- The user should investigate **HyperFrames** and try making videos with “Astra 6”.
- Reference material was provided:
  - YouTube: https://youtu.be/UDE5eIT2CQk
  - Facebook reference 1: https://www.facebook.com/share/v/1Eud9Buh96/
  - Facebook reference 2: https://www.facebook.com/share/v/1KNgQr4SH6/

**Note:** The references above were supplied in the original brief. Their precise visual details should be reviewed directly before treating any particular style, pacing, or editing technique as confirmed.

---

## 3. Goals and success definition

### Primary goal

Produce short, useful AI explainer clips that are suitable for a TikTok audience and can be made through a repeatable workflow.

### Secondary goals

- Make AI concepts and settings understandable to non-experts.
- Provide value before promoting a product or course.
- Establish a consistent visual identity for the series.
- Minimize repeated manual editing.
- Keep tool and API costs low during the prototype.
- Make factual claims verifiable and avoid invented metrics, testimonials, or product behavior.

### Prototype acceptance criteria

The prototype is successful when:

- [ ] The environment can render a valid MP4.
- [ ] The pilot is 20–30 seconds long and vertical 9:16.
- [ ] The final file is technically playable and visually reviewed.
- [ ] The key instructional steps are based on the real product interface.
- [ ] Important claims are supported by current, credible sources.
- [ ] Captions are readable on a phone and Vietnamese diacritics render correctly.
- [ ] The next episode can reuse the template without rebuilding the whole composition.
- [ ] The actual production time and cost are measured rather than assumed.

A proposed initial output target is **1080 × 1920 at 30 fps**. This is a project default, not a claim that TikTok requires only this configuration.

---

## 4. Decisions already established

These are the choices the user explicitly confirmed in the conversation:

| Item | Confirmed choice |
|---|---|
| Content format | TikTok AI explainer |
| Duration | 20–30 seconds |
| Visual style | Combination of real UI and animation/motion graphics |
| AI model named by user | GPT-6 Astra |
| Main production priority | A reusable production line/template |
| First work mode | Prototype and validate before automating everything |
| Initial cost approach | Prefer existing tools and avoid unnecessary paid subscriptions/API calls |
| First proposed pilot | A privacy/data-control setting in ChatGPT |

### Recommendations, not yet confirmed decisions

- Use HyperFrames as the main rendering/composition framework.
- Use Cursor as the primary IDE, with Antigravity as an alternative if more convenient.
- Start with one manually reviewed pilot before batch production.
- Do not automate TikTok publishing in the first prototype.
- Do not buy a dedicated AI video-generation subscription until the initial workflow proves insufficient.

### Important naming caveat: “Astra 6”

The user referred to “GPT-6 Astra”. The precise product/model identity, access method, and feature set should be verified in the actual environment or official documentation before implementation. Do not assume that a model name automatically implies access to a particular API or video-rendering capability.

---

## 5. Content strategy: four content families

The recommendation is to use **AI tips and hidden settings** as the primary pillar, with explainers and practical demos as supporting formats. Motion graphics are a presentation style that can be used across all pillars.

### A. AI tips and settings — primary pillar

Examples:
- A privacy or data-control setting worth checking.
- A setting that changes how an AI tool behaves.
- A permission or sharing option users may overlook.
- A quick checklist before pasting sensitive information into an AI service.

Why it fits:
- The viewer can take an immediate action.
- The screen recording provides proof of the instruction.
- It is easy to turn into a numbered series.

### B. AI explained in 30 seconds

Examples:
- Why AI can sound confident and still be wrong.
- What context windows mean in practice.
- What an AI agent is, explained with a familiar analogy.
- Why a chatbot may not remember something from another conversation.

Why it fits:
- It makes complex ideas approachable.
- Motion graphics can explain invisible processes.
- It can build trust through clear teaching.

### C. One prompt, one result

Examples:
- Turn messy notes into a structured summary.
- Convert a plain-language request into a useful table.
- Ask AI to identify missing information in a draft.
- Show how adding context changes the quality of a response.

Why it fits:
- A visible before/after result creates a clear payoff.
- It is naturally demo-driven.
- It can be made with real recordings rather than fabricated results.

### D. Visual explainers

Use animation, typography, diagrams, callouts, and visual metaphors to support the other content families.

Examples:
- Data flows from a user input to a service, illustrated carefully.
- A “new employee” analogy for an AI assistant.
- A simple visual comparison between a prompt with little context and one with useful context.

**Recommended mix for the first batch:** prioritize A, then test B and C. Use D as a consistent visual language rather than a separate channel topic.

---

## 6. Recommended toolchain

The toolchain should have as few moving parts as possible. Do not add tools merely because they are available.

### 6.1 GPT-6 Astra — research and editorial assistance

Use it to:
- Explore topic angles.
- Find and summarize official documentation.
- Draft a short hook and narration.
- Break the script into timed scenes.
- Suggest visual metaphors and animation ideas.
- Review the video script for ambiguity or unsupported claims.
- Help write or debug code when paired with an IDE.

It does **not** replace a renderer, a real screen recording, or a final human review.

### 6.2 Cursor or Antigravity — coding environment

Use one IDE as the main project environment to avoid duplicated setup.

Possible responsibilities:
- Inspect and set up the project.
- Build reusable HTML/CSS/JavaScript compositions.
- Implement scene transitions, callouts, captions, and end cards.
- Run preview/render commands.
- Fix rendering issues and maintain the template.

**Recommendation:** start with Cursor if it is the environment the user prefers for code/project management. Antigravity is a valid alternative. This choice is not yet final.

### 6.3 HyperFrames — video composition and rendering

Proposed role:
- Render HTML/CSS/JavaScript-based scenes into video.
- Animate typography, callouts, UI highlights, diagrams, and transitions.
- Combine real images/screen recordings, captions, and audio.
- Reuse the same composition logic across episodes.

Potential setup references:
- HyperFrames project: https://github.com/heygen-com/hyperframes
- HyperFrames documentation: https://www.hyperframes.dev/
- HyperFrames quickstart (verify current path/content): https://hyperframes.app/docs/1-startup/2-quickstart

The framework and its commands can change. Follow the current official instructions and the installed skill's conventions rather than relying blindly on an old command or example.

### 6.4 Node.js and FFmpeg

Proposed prerequisites for the HyperFrames workflow:
- Node.js 22 or a version currently supported by the official project.
- npm.
- FFmpeg available from the terminal.

Check the environment before installing anything:

```bash
node -v
npm -v
ffmpeg -version
```

The first check is diagnostic only. It does not install or modify anything.

A command previously suggested for adding the HyperFrames skill was:

```bash
npx skills add heygen-com/hyperframes
```

Before running it, verify that this remains the official/current installation command and inspect what it installs. Do not run untrusted commands blindly.

### 6.5 Screen recording and UI capture

Use authentic product screenshots or screen recordings for instructions that depend on a real interface.

Requirements:
- Capture the actual product and current interface.
- Avoid exposing personal data, API keys, emails, private chats, or other secrets.
- Capture a clean account/session suitable for demonstration.
- Use zoom/crop/highlight overlays in the composition instead of fabricating the interface.
- If an asset is a placeholder, label it as such and do not present it as a real product screenshot.

### 6.6 Voiceover, captions, and optional post-production

Start simply:
- Record or generate a clear voiceover.
- Generate captions and manually check Vietnamese text.
- Add subtle background music only if it does not compete with narration.
- Use a separate editor only when necessary for audio cleanup or special post-production.

No dedicated voice/video subscription is required for the first proof of concept.

### 6.7 Avoid premature complexity

Do not initially add:
- Paid API orchestration.
- Automated TikTok publishing.
- A database.
- A full web dashboard.
- Multiple overlapping video-generation products.
- A complex agent framework.

First prove that the workflow can create two good videos efficiently.

---

## 7. Prototype episode #001: ChatGPT data-control setting

### Working title

**“Bạn dùng ChatGPT mỗi ngày? Kiểm tra setting này.”**

### Why this is a good pilot

- It follows the topic suggested by sếp Đức.
- It has a specific action the viewer can take.
- The actual UI can be recorded.
- The setting can be highlighted with motion graphics.
- The structure is reusable for future settings/tutorials.

### Accuracy warning

The exact setting label, navigation path, and current behavior must be checked against official OpenAI help documentation at production time. Product UI and policies can change.

Potential official source:
- ChatGPT Data Controls FAQ: https://help.openai.com/

Find the current official page about Data Controls and confirm all wording before recording. Do not claim that disabling a training-related option deletes chat history, prevents every form of data retention, or guarantees that no data is processed.

### Draft storyboard — 25 seconds

| Time | Purpose | Visual | Narration / on-screen text |
|---|---|---|---|
| 00–03s | Hook | Real UI blurred slightly behind bold kinetic typography | “Bạn dùng ChatGPT mỗi ngày? Kiểm tra setting này.” |
| 03–10s | Demonstration | Real screen recording; show the correct menu path and highlight the relevant control | “Vào phần cài đặt dữ liệu và tìm tùy chọn sử dụng nội dung để cải thiện mô hình.” |
| 10–20s | Explanation | UI close-up, animated highlight, then a simple data-control visual | Explain the verified effect and its limits in plain Vietnamese. |
| 20–25s | CTA | Reusable end card with a short instruction | “Vào kiểm tra ngay nhé. Lưu clip để khỏi quên!” |

The narration above is a **draft**, not a final verified script. The explanation line must be replaced with exact, current, source-checked wording before publication.

### Visual direction

- Dark, premium tech aesthetic.
- Real product UI remains the source of truth.
- Large, readable Vietnamese typography.
- Use a restrained accent color to point at the relevant control.
- Smooth zooms and callouts, not constant movement.
- Use a simple animation to explain the control, not to invent additional product behavior.
- Keep the end card short and reusable.

### Assets needed

- Clean screen recording of the relevant ChatGPT settings.
- One or more still screenshots for zooms/callouts.
- Voiceover file.
- Caption text or timing data.
- Optional sound effect and subtle music.
- Reusable logo/brand end card if the channel has approved brand assets.

### Final fact-check before publishing

- [ ] The setting name is correct.
- [ ] The menu path is correct for the product/version being shown.
- [ ] The explanation matches official documentation.
- [ ] Any limitations are explained accurately.
- [ ] No private user information is visible.
- [ ] No claim suggests the setting deletes chat history unless that is explicitly true and verified.
- [ ] UI shown in the clip matches the narration.

---

## 8. Reusable project structure

Suggested starting layout:

```text
ai-explainer-factory/
├── README.md
├── STYLE_GUIDE.md
├── package.json
├── template/
│   ├── composition/
│   ├── components/
│   │   ├── HookScene
│   │   ├── DemoScene
│   │   ├── ExplanationScene
│   │   ├── TakeawayScene
│   │   └── EndCard
│   ├── styles/
│   └── assets/
├── episodes/
│   ├── 001-chatgpt-data-control/
│   │   ├── research.md
│   │   ├── script.md
│   │   ├── scenes.json
│   │   ├── assets/
│   │   └── voiceover/
│   └── 002-ai-hallucinations/
│       ├── research.md
│       ├── script.md
│       ├── scenes.json
│       └── assets/
├── exports/
│   ├── previews/
│   └── final/
└── qa/
    ├── fact-check.md
    └── release-checklist.md
```

This is a **logical target structure**, not a verified HyperFrames directory layout. Adapt it to the actual framework's required file conventions.

### Separate reusable template from episode-specific data

Reusable template owns:
- Canvas and output settings.
- Typography and colors.
- Scene transitions.
- Caption appearance.
- Highlight/callout components.
- Animation timing primitives.
- End card.
- Audio mixing defaults.

Episode package owns:
- Topic and source links.
- Approved script.
- Scene text and timestamps.
- UI capture assets.
- Voiceover.
- Captions.
- CTA.
- Episode-specific factual caveats.

The intended result is that episode #002 requires changing its content/assets rather than rewriting the video system.

### Example episode data (illustrative only)

```json
{
  "id": "001-chatgpt-data-control",
  "title": "Check this ChatGPT setting",
  "language": "vi",
  "durationSeconds": 25,
  "format": {
    "width": 1080,
    "height": 1920,
    "fps": 30
  },
  "scenes": [
    {
      "type": "hook",
      "start": 0,
      "end": 3,
      "text": "Bạn dùng ChatGPT mỗi ngày?"
    },
    {
      "type": "demo",
      "start": 3,
      "end": 10,
      "asset": "assets/data-controls-screen-recording.mp4"
    },
    {
      "type": "explanation",
      "start": 10,
      "end": 20,
      "text": "REPLACE_WITH_VERIFIED_EXPLANATION"
    },
    {
      "type": "end-card",
      "start": 20,
      "end": 25,
      "text": "Lưu clip để khỏi quên!"
    }
  ]
}
```

This is a proposed content schema for planning. It is **not guaranteed to be directly compatible** with HyperFrames without adapting it to the current API/composition conventions.

---

## 9. Coding-agent prompt for building the template

Paste this into the chosen IDE agent after checking the environment and current official HyperFrames instructions.

```text
# Build a reusable TikTok AI Explainer Video Factory

Act as a senior motion designer, frontend engineer, and video automation engineer.

## Goal
Build a reusable HyperFrames project for producing Vietnamese TikTok AI explainer videos, 20–30 seconds long, combining real product UI recordings with premium motion graphics.

## Technical requirements
- Use HyperFrames and follow its current official composition conventions.
- Use HTML, CSS, and JavaScript; use GSAP if appropriate and compatible.
- Output portrait 9:16 video at 1080×1920, 30 fps.
- Support a deterministic preview and MP4 rendering workflow.
- Do not introduce React, Vite, or a separate application build system unless the official HyperFrames workflow requires it.
- Keep episode-specific content separate from the reusable template.

## Visual direction
- Premium dark technology aesthetic.
- Clear typography, restrained accent colors, smooth zooms, highlights, transitions, and kinetic captions.
- Combine authentic screenshots/screen recordings with animated callouts and explanatory diagrams.
- Avoid excessive glow, clutter, tiny text, and generic stock visuals.
- Render Vietnamese diacritics correctly.

## Reusable scene system
Create configurable scenes for:
1. Hook
2. Real UI demonstration
3. Animated explanation
4. Key takeaway
5. CTA/end card

Keep narration, captions, timestamps, and asset references configurable.

## First pilot
Create a 25-second explainer about a ChatGPT data-control setting.

Use only the real, verified interface assets supplied by the user. Do not fabricate screenshots or claim that disabling a setting deletes chat history or prevents all data retention.

If real UI assets are not supplied, use clearly labeled placeholders and make the missing assets obvious.

## Deliverables
- Reusable project structure.
- One working pilot composition.
- A sample episode configuration.
- Preview and render instructions.
- README with prerequisites, setup, asset replacement, and troubleshooting.
- QA checklist for timing, Vietnamese typography, captions, audio, and factual accuracy.

## Working rules
1. Inspect the environment and current official HyperFrames instructions before editing.
2. Report prerequisites and a minimal implementation plan.
3. Build the smallest working version first.
4. Render and inspect the actual output; do not claim success without verification.
5. Fix issues found in the render before polishing.
6. Keep the workflow maintainable for future episodes.
7. Do not install unnecessary dependencies or make paid API calls without approval.
8. Do not overwrite unrelated files.
```

---

## 10. Three-day implementation plan

This is a proposed schedule, not a report of completed work.

### Day 1 — Environment and first render

1. Choose the primary IDE.
2. Check Node.js, npm, and FFmpeg.
3. Read the current official HyperFrames quickstart.
4. Install the framework/skill according to current official instructions.
5. Create a minimal composition with placeholder text and one transition.
6. Render a short test video.
7. Confirm the MP4 plays and the fonts render correctly.
8. Record setup issues in the README.

**Exit condition:** a short test MP4 renders successfully. Do not build the full pilot before this works.

### Day 2 — Produce pilot #001

1. Research the setting using official documentation.
2. Lock the factual wording.
3. Capture the real UI.
4. Record or generate the voiceover.
5. Build the hook, demo, explanation, and CTA scenes.
6. Add captions and sound.
7. Preview and render.
8. Watch the exported file from beginning to end on a phone-sized display.
9. Fix pacing, legibility, factual, and audio issues.

**Exit condition:** one complete draft is ready for stakeholder review.

### Day 3 — Test reuse with episode #002

1. Pick a different, source-checkable topic.
2. Duplicate only the episode data/assets, not the whole template.
3. Replace the script, recordings, captions, and voiceover.
4. Render again.
5. Measure time spent on research, asset capture, content, rendering, and revisions.
6. Identify any manual steps that repeat unnecessarily.
7. Update the README and release checklist.

**Exit condition:** a second episode renders using the same template without rebuilding the whole composition.

---

## 11. QA and release checklist

### Factual quality
- [ ] Claims are supported by current, credible sources.
- [ ] Product-specific instructions were checked against official documentation.
- [ ] The video does not overstate privacy/security guarantees.
- [ ] No fabricated metrics, testimonials, or outcomes.
- [ ] The narration matches the actual UI shown.
- [ ] Any important caveat fits within the short format.

### Visual quality
- [ ] Video is vertical 9:16.
- [ ] Resolution and frame rate match the project configuration.
- [ ] No black frames, missing assets, or unexpected blank scenes.
- [ ] Text is legible on a phone.
- [ ] Vietnamese diacritics render correctly.
- [ ] Callouts point to the correct UI control.
- [ ] Transitions are consistent and not distracting.
- [ ] The ending does not cut off abruptly.

### Audio and captions
- [ ] Voiceover is intelligible and not clipped.
- [ ] Background music does not overpower speech.
- [ ] Captions match the spoken words.
- [ ] Captions are timed correctly.
- [ ] Important meaning is still understandable with sound off.
- [ ] No copyrighted audio/visual assets are used without appropriate rights.

### Privacy and release
- [ ] No private messages, emails, credentials, API keys, or personal data are visible.
- [ ] All footage/assets have appropriate usage rights.
- [ ] The exported MP4 was watched in full.
- [ ] Final file and source assets are stored in the correct episode folder.
- [ ] A human reviewer approved the clip before posting.

---

## 12. Measurement plan

The initial target is to work toward producing one standard clip in **30–60 minutes after the template stabilizes**, excluding unusually difficult research. This is a hypothesis to measure, not a guaranteed result.

Record per episode:

| Metric | What to measure |
|---|---|
| Research time | Minutes to verify claims and sources |
| Script time | Minutes to draft and approve narration |
| Asset time | Minutes to capture UI and prepare visuals |
| Production time | Minutes to assemble and render |
| Revision time | Minutes spent fixing issues after review |
| Total time | Sum of the above |
| Render reliability | Whether render succeeded on first attempt |
| Reuse rate | How much template code was reused |
| QA failures | Factual, visual, caption, or audio defects |
| Cost | Any paid tool/API usage attributable to the clip |

Do not evaluate the pilot only by views. Early performance is affected by topic, hook, distribution, account history, and many other factors. First establish a consistent production baseline.

---

## 13. Risks and mitigations

| Risk | Mitigation |
|---|---|
| The model/tool name “Astra 6” is ambiguous | Verify the exact product, access method, and official docs before depending on its features. |
| HyperFrames instructions change | Follow the current official docs and installed skill rather than stale snippets. |
| The rendered video looks polished but teaches the wrong thing | Fact-check all product-specific claims and capture authentic UI. |
| Fake or outdated UI appears in the clip | Use actual screen recordings and label placeholders during development. |
| The first project becomes over-engineered | Render a minimal 5-second test before building all scenes. |
| Tool/API costs rise unnecessarily | Start with existing subscriptions and manual review; obtain approval before paid API use. |
| Template is difficult to reuse | Separate reusable components from per-episode data/assets. |
| Captions are too small or dense | Preview at phone size and keep each caption short. |
| The clip promises too much about privacy | State the exact setting effect and its limits; do not imply universal deletion or zero retention. |
| Automation masks failures | Require a human to inspect the exported MP4 before release. |

---

## 14. Open questions to resolve

These points are not yet settled and should not be treated as decisions already made.

1. **Exact “GPT-6 Astra” access:** Is the user using it inside ChatGPT, through an IDE agent, or through an API? Which model selector/product label is visible?
2. **Primary IDE:** Cursor or Antigravity?
3. **Voice:** User's own voice, TTS, or text-only captions?
4. **Branding:** Does the channel have a logo, approved colors, fonts, or a standard end card?
5. **Language and tone:** Vietnamese only? Friendly, humorous, professional, or a mixture?
6. **Screen-recording method:** Which recorder is preferred and already installed?
7. **Review process:** Who approves factual content and final video?
8. **Output handoff:** Does sếp want MP4 only, or also source project and editable assets?
9. **Production target:** How many clips per week?
10. **Reference-video style:** After watching the supplied links directly, what exact traits should be matched—pacing, text style, sound design, visual density, or camera movement?

---

## 15. Immediate next steps

Follow this order to avoid wasting time:

### Step 1 — Check the machine

Run:

```bash
node -v
npm -v
ffmpeg -version
```

Record the output. If a command fails, fix that prerequisite before starting the project.

### Step 2 — Verify HyperFrames setup

Read the current official quickstart and check the installation/skill instructions. Do not assume that an older command or file structure is still current.

### Step 3 — Choose one IDE

Use Cursor or Antigravity as the primary environment for this prototype. Avoid splitting the same project across both until the initial workflow works.

### Step 4 — Render a 5-second technical test

Create a simple composition with:
- One background.
- One Vietnamese headline.
- One motion transition.
- One short render.

Verify the actual exported MP4, not just a browser preview.

### Step 5 — Research and capture pilot #001

Verify the ChatGPT setting's current name and behavior using official documentation, then capture the real UI with no sensitive data visible.

### Step 6 — Build and review the 25-second pilot

Use the storyboard in Section 7. Keep the initial version simple enough to revise quickly.

### Step 7 — Test reuse with episode #002

Change only the episode-specific content and assets. Measure the real production time.

---

## 16. Reference links

The following links are provided as starting points. Confirm the current page and product details before relying on them.

### Original references from sếp Đức
- YouTube: https://youtu.be/UDE5eIT2CQk
- Facebook video 1: https://www.facebook.com/share/v/1Eud9Buh96/
- Facebook video 2: https://www.facebook.com/share/v/1KNgQr4SH6/

### Proposed tooling references
- HyperFrames GitHub: https://github.com/heygen-com/hyperframes
- HyperFrames site: https://www.hyperframes.dev/
- HyperFrames quickstart: https://hyperframes.app/docs/1-startup/2-quickstart
- OpenAI Help Center: https://help.openai.com/

---

## 17. Final recommendation

Do not attempt to automate the entire content factory at once.

**First prove one reliable loop:**

> verified idea → concise script → real UI capture → reusable animation template → rendered MP4 → human QA

Then prove the same template can create a second clip. Once that is reliable, automate the repetitive parts: episode configuration, caption generation, asset validation, rendering, file naming, and production tracking.

The most valuable outcome of this prototype is not a single beautiful video. It is a maintainable production system that can keep making accurate, useful, consistent clips for the channel.
