# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Who We Are (The Signal Growth Engine)

**Signal is an Autonomous Brand Infrastructure Firm.** We have not built an agency; we have built an enterprise technology installation.

Our Growth Engine operates on three unyielding pillars:
1. **Permanent Power, Not Rented Labor:** We do not sell retainers or billed hours. We install SDK-native multi-agent execution architecture directly into a company's core. Clients own the tech, the code, and the pipelines.
2. **Killing "The Middle":** We eliminate bloated account management. Raw founder truth maps to the Identity File, passes through our AI pipelines, and compiles straight to production via the Anti-Gravity Terminal. Zero brand drift.
3. **Coldly Efficient Pipeline:** We operate on an uncompromising 48-Hour Installation Standard. What agencies take months to do, we execute autonomously in a fraction of the time.

**SIGNAL: PERMANENT POWER. NOT RENTED LABOR.**

Every line of code written in this repo is an execution node in that mission. Read The Brain before building anything.

---

## The Brain (Read This First)

`The Brain/` is the identity and strategic core of Signal. It must be read and internalized before any work begins.

- `The Brain/SIGNAL-MANIFESTO-V2.1.md` — The Onyx Standard. Signal's canonical identity document. Who we are, how we operate, the full tech stack, the installation sequence, the scale roadmap, and the non-negotiables. This is law.
- `The Brain/SIGNAL-MILLION-DOLLAR-MODEL.md` — The market thesis. Why this model wins right now, why the timing is exact, and why the category doesn't exist yet.

**The Identity File is sacred.** Every piece of output must be consistent with the voice, tone, and positioning defined in The Brain. Zero brand drift. Zero exceptions.

---

## Our Role (Claude Code)

Claude Code is the **Lead AI Engineer** of Signal's execution stack. Responsibilities:

- Set up and maintain client GitHub repositories and production pipelines
- Write all Python code that powers the execution nodes
- Operate inside the **Anti-Gravity Terminal** to compile design briefs into production-ready animated brand content
- Run Firecrawl scrapes to feed raw intelligence into the Identity File
- Build and maintain MCP integrations

---

## The Tech Stack

1. **Executive Agent (SDK-Native)** — Python Virtual Environment running `claude-sonnet-4-6`. Owns copy, voice, content calendars, brand compliance. Verified with live credits.
2. **Strategic Brainstorm Layer (Claude CoWork)** — strategy and creative direction
3. **Lead AI Engineer (Claude Code)** — GitHub, pipelines, terminal execution — this is us
4. **Intelligence Scraper (Firecrawl)** — digital footprint + competitor scraping
5. **The Identity File (The Heart)** — Signal-maintained Google Doc, single source of brand truth
6. **Visual Prototyping Engine (Claude Design)** — brand templates, animated content
7. **GitHub Repository (Ground Truth)** — client owns all code and automations
8. **Anti-Gravity Terminal (The Execution Layer)** — production terminal where Claude Code lives and compiles

---

## The Non-Negotiables

1. Never hire the middle — execution nodes and engineers only
2. The Identity File is sacred — zero brand drift
3. The client owns their infrastructure — code in GitHub, Identity File in Google Docs
4. Speed is the standard — 48-hour installation is the product
5. Conviction over comfort — we only work with clients who know the old model is dead

---

## Active Clients

### Bored N Buzzed Cannabis — Phase 1 Case Study
- **Retainer:** $2k/month (grows with proof)
- **Location:** 11516 124th Ave NE, Kirkland WA 98033 | Phone: (425) 814-0200
- **Hours:** Sun–Thurs 8AM–11PM | Fri–Sat 8AM–11:45PM
- **Website:** https://borednbuzzed.com/
- **POS System:** POSaBit (`ecomm-app.posabit.com/bored-n-buzzed-kirkland`)
- **Menu Platform:** Leafly (`web-embedded-menu.leafly.com/e-menu/bored-n-buzzed`)
- **Identity File:** `The Brain/CLIENTS/BORED-N-BUZZED-IDENTITY.md` — v2.0, full brand engine. Read this before writing anything for B&B.
- **Intelligence File:** `The Brain/CLIENTS/BORED-N-BUZZED-INTELLIGENCE.md`
- **Competitor Intel:** `Competitors/UNCLE-IKES-INTELLIGENCE.md`
- **Logos:** `Logos/Buzzed Logos/` — four variants (stacked + horizontal, black + ghost)
- **Status:** Architecture Engine Finished. Identity File v2.0 locked. Old WordPress site deprecated; pivoting to full custom web infrastructure build.

**Tech stack confirmed:**
- WordPress + Elementor (website CMS)
- POSaBit (POS — target for API integration)
- Leafly (menu embed)
- take.cards/PEM8L (rewards wallet — Apple + Google Wallet)

**What we know:**
- Tagline: "Stay One Puff Ahead" — strong, underused, must run everywhere
- Bold streetwear/skate logo — chunky hand-drawn type, circled N mark, four variants
- Jim Jones live event (Oct 3, 2025) — private Kirkland venue, Mirra afterparty in Bellevue, limited merch drop, Sky High + WYLD as vendor partners
- Mirra (Bellevue) is an active events partner
- Video assets on site: Journeyman: Berries, Mfused: Carts, Jim Jones Promo (all ~0:16)
- Five content pillars: The Deal / The Education / The Culture / The Community / The Product
- 12 featured brand partners: 28 Herbs, Kush Mountain, Mfused, PICC, Soulshine, Sky High Gardens, Fireline, Desert Dream, Artizen, Journeyman, Good Tide, WYLD

**Open gaps (priority order):**
1. **New Web Infrastructure:** Build a pristine custom frontend site (Vanilla HTML/CSS/JS) to replace their template WordPress.
2. **Content Publishing Engine:** Deploy the SDK-Native Executive Agent to generate the 60-day content calendar straight into the new repo.
3. **POS Integration:** Map POSaBit API into the new web build for real-time inventory.
4. **Instagram Rebuild & Compliance Infrastructure:** Fix 3x banned account history.
5. **Social Proof Display:** Embed reviews and UGC cleanly into the new UI.

**Competitor landscape:**
- Uncle Ike's (Seattle) — 5 locations, live POS menu, 14 active deals, mobile app, price match guarantee, cash only
- Uncle Ike's weakness: zero Kirkland presence, corporate identity, no culture positioning
- B&B's moat: sole Kirkland operator + streetwear/culture identity a chain cannot replicate

---

## Folder Structure

- `The Brain/` — Signal's identity, manifesto, market thesis, and client intelligence. Read before building.
- `The Brain/ENGINE-COMPLETION-RECAP.md` — The finalized architectural breakdown of the 7-layer engine and SDK core.
- `The Brain/CLIENTS/` — Intelligence files for each client.
- `Competitors/` — Competitor scrape data and intelligence reports. Raw JSON + analysis markdown per competitor.
- `Logos/` — Client logo assets organized by client folder.
- `Engine/` — Permanent, autonomous codebase nodes (like the Executive Agent SDK) that are installed into client systems.
- `API/keys.py` — All API keys stored here. When adding new keys, append them to this file.
- `MCP/` — All MCP integrations live here. Each MCP tool gets its own file (e.g. `firecrawl.py`).
- `Skills/` — Agent skills that extend Claude Code's design and execution capabilities. See Skills Stack below.
- `CLI/` — CLI tools for browser automation and terminal-based execution. See CLI Stack below.
- `Memory/MEMORY.md` — Index of all project memories. Update this and add a corresponding memory file whenever something important is learned or decided.
- `Hand Off Folder/` — Session hand-off summaries. Read the latest hand-off at the start of every session to restore full context. New hand-offs are created after major sessions or milestones. Current file: `Hand-Off Summaries.md`.
- `Notes/` — Flagged issues, action items, and urgent tasks. Files prefixed with `URGENT-` require immediate attention.
- `Strategy/` — Strategic moves, content calendars, growth plans, and execution roadmaps for Signal and its clients.

---

## API Keys

Import keys from `API/keys.py`:

```python
from API.keys import FIRECRAWL_API_KEY
```

---

## Firecrawl

Initialize the Firecrawl client via:

```python
from firecrawl import FirecrawlApp
from API.keys import FIRECRAWL_API_KEY

app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)
```

**Scraping notes:**
- Use `app.scrape(url, formats=["markdown"])` for single pages — `crawl_url` is deprecated.
- Use `app.crawl(url, limit=N, scrape_options={"formats": ["markdown"]})` for full site crawls. Returns a `CrawlJob` object; access pages via `result.data`.
- For sites with age gates (e.g. cannabis dispensaries), use `actions` to click through:
  ```python
  actions = [
      {"type": "click", "selector": "[aria-label='Confirm I am 21 years or older']"},
      {"type": "wait", "milliseconds": 2000},
      {"type": "click", "selector": "input[type='checkbox']"},  # terms agreement
      {"type": "wait", "milliseconds": 500},
      {"type": "click", "selector": "[aria-label='Continue to site']"},
      {"type": "wait", "milliseconds": 2500},
  ]
  result = app.scrape(url, formats=["markdown"], actions=actions)
  ```
- When serializing crawl results to JSON, use a custom serializer to handle `datetime` objects.

---

## Skills Stack

Installed in `Skills/`. Seven layers of design and execution intelligence — load the relevant skill before any UI, design, or animation work. These are not optional enhancements. They are the pipeline.

### Layer 1 — Intelligence Extraction
**SkillUI** (`Skills/npxskillui/`)
Reverse-engineers any live website into a Claude-ready design system. Extracts colors, typography, spacing, animations, and components. Ultra mode uses Playwright for full visual extraction including screenshots and interaction diffs. Point at `borednbuzzed.com` to extract B&B's current design system. Point at any competitor to extract their visual language. Every build starts here — never design from zero.

### Layer 2 — Design System Generation
**UI UX Pro Max** (`Skills/ui-ux-pro-max-skill/`)
161 design reasoning rules + 67 named UI styles + Design System Generator. Feed a brand brief and get back a full recommended design system: UI pattern, color palette, typography pairing, motion direction, and a pre-delivery QA checklist. The bridge between the Identity File and the build. SkillUI = current state. UI UX Pro Max = ideal state. The gap is what Signal closes.

### Layer 3 — Build Intelligence
**Taste Skill** (`Skills/taste-skill/`)
8 specialized frontend variants: `taste-skill` (all-rounder), `redesign-skill` (audit + fix existing), `soft-skill` (calm + premium), `minimalist-skill` (editorial restraint), `brutalist-skill` (hard + mechanical), `output-skill` (forces complete output), `stitch-skill` (Google Stitch/DESIGN.md compatible). 3-dial tuning: DESIGN_VARIANCE / MOTION_INTENSITY / VISUAL_DENSITY (1–10). For B&B: `taste-skill`, high DESIGN_VARIANCE, moderate MOTION_INTENSITY.

### Layer 4 — Reference Library
**Awesome DESIGN.md** (`Skills/awesome-design-md/`)
69 ready-to-use DESIGN.md files from real production websites (Vercel, Linear, Notion, ElevenLabs, RunwayML, and more). Drop into any project and Claude instantly knows the full visual language of a world-class design team. Use as compositional reference baselines. Signal never builds from zero — we build from proof.

### Layer 5 — Animation & Motion
**WebGPU Three.js TSL** (`Skills/webgpu-claude-skill/`)
GPU-accelerated 3D and shader programming via WebGPU + Three.js r183+. Node-based materials, GPU compute shaders, particle systems, cinematic post-processing. This is the Anti-Gravity Terminal engine — animated logo renders, motion brand assets, social content that moves, ambient store visuals. They export a PNG. We render a living brand experience.

### Layer 6 — Quality Control
**Impeccable** (`Skills/impeccable/`)
The final gate. 18 commands — `/audit`, `/critique`, `/polish`, `/animate`, `/bolder`, `/colorize`, `/overdrive`, and more — backed by curated anti-patterns that explicitly tell the AI what NOT to do. Fights the default AI bias: Inter font, purple gradients, cards in cards, gray text on colored backgrounds. Nothing ships to a client without running through Impeccable. Zero exceptions.

### Layer 7 — Live Verification
**Playwright MCP** (`MCP/playwright.py`)
Native MCP browser automation — Claude calls browser actions directly as tools, no bash commands needed. 143 real device profiles for mobile/tablet/desktop testing. Use to: verify B&B contact page fix is live, QA blog posts and menu embeds across iPhone/Android/desktop, navigate age-gated cannabis sites, screenshot before/after states as client proof. Replaced the Playwright CLI (retired Session #005).

---

### The Signal Play — B&B Design Execution Sequence
Full brief: `Notes/THE-SIGNAL-PLAY-SKILLS.md`

1. **SkillUI** — extract B&B's current design system from `borednbuzzed.com`
2. **UI UX Pro Max** — generate ideal design system from the Identity File brief
3. **Taste Skill** — build with `taste-skill`, high DESIGN_VARIANCE, moderate MOTION_INTENSITY
4. **Impeccable** — run `/critique` + `/polish` on all output before shipping
5. **Awesome DESIGN.md** — pull reference DESIGN.md from a brand with similar streetwear/culture energy

---

## Document Skills (Anthropic Official)

Installed via `/plugin install document-skills@anthropic-agent-skills`. These are Anthropic's production-grade skill library. Load automatically — no manual invocation needed.

| Skill | Use For |
|---|---|
| **pptx** | Client pitch decks, strategy presentations, onboarding decks — any .pptx input or output |
| **xlsx** | Content calendars, client reporting, budget tracking — any spreadsheet input or output |
| **canvas-design** | Posters, social graphics, visual art as PNG/PDF — B&B content production |
| **frontend-design** | Production-grade web components, landing pages, dashboards — B&B site work |
| **mcp-builder** | Guided workflow for building new MCP servers — stack expansion |
| **algorithmic-art** | Generative art via p5.js — ties into animation layer (Layer 5) |
| **pdf** | Read, extract, combine, split, or watermark PDFs |
| **docx** | Word document creation and editing |

---

## CLI Stack

Installed in `CLI/`. Browser automation and terminal execution tools. All new CLIs go here.

| Tool | Path | Use For |
|---|---|---|
| **Playwright CLI** | `CLI/playwright-cli/` | ~~RETIRED Session #005~~ — replaced by Playwright MCP (see Layer 7 above). |

---

## Conventions

- All code is Python.
- New MCP tools go in `MCP/` with their own file.
- New API keys go in `API/keys.py`.
- New agent skills go in `Skills/` with their own folder.
- New CLI tools go in `CLI/` with their own folder.
- Every build serves the mission: permanent brand infrastructure, not rented labor.
