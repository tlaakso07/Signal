# The Signal Play — Connect SkillUI + UI UX Pro Max for B&B
**Flagged:** April 21, 2026
**Priority:** Execute after all Skills are installed

---

## The Play

Two newly installed skills work together as a one-two punch for building the B&B design system:

**Step 1 — SkillUI** (`Skills/npxskillui/`)
Point SkillUI at `borednbuzzed.com` to reverse-engineer their existing design system — extract live colors, typography, spacing, animations, and components into a Claude-ready skill folder.

```bash
skillui --url https://borednbuzzed.com
```

Use ultra mode for full visual extraction (screenshots, interaction diffs, DOM fingerprinting):
```bash
skillui --url https://borednbuzzed.com --ultra
```

**Step 2 — UI UX Pro Max** (`Skills/ui-ux-pro-max-skill/`)
Feed the B&B brand brief + Identity File into the Design System Generator. Get back a complete recommended design system: UI pattern, color palette, typography pairing, effects, and a pre-delivery QA checklist — all tuned to the streetwear/cannabis culture brief.

---

## Why This Combination

- SkillUI tells us what B&B *currently is* visually
- UI UX Pro Max tells us what B&B *should be* — reasoned from the brand brief
- Together: current state + ideal state = the gap Signal closes with every design deliverable

---

## Then Layer On Top

- **Impeccable** (`Skills/impeccable/`) — run `/critique` and `/polish` on any output to catch generic AI design patterns before they ship
- **Awesome DESIGN.md** (`Skills/awesome-design-md/`) — pull a reference `DESIGN.md` from a brand with a similar energy (streetwear, culture, premium-but-accessible) as a compositional reference

---

*Flagged by Signal — Claude Code*
