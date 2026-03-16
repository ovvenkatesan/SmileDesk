# Visual Direction: {{project_name}}

> Brand Aesthetics & Design Guidelines

**Created:** {{date}}
**Author:** {{user_name}}
**Related:** [Product Brief](./product-brief.md) | [Content & Language](./content-language.md)

---

## Existing Brand Assets

### Current Assets

The product builds upon the existing visual identity of Smile Garden Dental Care while softening it for a modern SaaS/AI interface.

| Asset | Status | Location |
|-------|--------|----------|
| Clinic Website | Active Reference | `https://smilegarden.in/` |
| Brand Colors | Conceptually active (Green & Blue) | N/A (To be softened) |
| Logo | Needs Recreation | No high-res SVG provided. Must be traced or a clean UI typographic variant created for the dashboard. |

### Brand Constraints

- The "Garden" (Green/Growth) and "Clinical" (Blue/Trust) motifs must remain, but the exact hex codes will be modernized into softer, consumer-health friendly tones.
- There are no strict partnership or third-party affiliation logos (e.g., insurance providers) required to be displayed on the widget, allowing for a strictly minimalist layout.

---

## Visual References

### Inspiration Sites

**[Ro (Roman)](https://ro.co)**
- What we like: Clean consumer health aesthetics, approachable typography, clear calls to action.
- Relevance: Perfect example of taking medical logistics and making them feel like a premium consumer experience.

**[Calm](https://www.calm.com)**
- What we like: Soft color usage, massive amounts of whitespace, rounded UI elements.
- Relevance: Embodies the "unhurried and reassuring" tone we want the AI agent to convey visually.

### What to Avoid
- Dense, dark-mode 'hacker' aesthetics (too intimidating for patients).
- Rigid, grid-heavy enterprise CRM looks like Salesforce Classic (too stressful for clinic owners).

### Visual Mood

The visual mood should instantly lower the user's blood pressure. It should feel like stepping into a modern, sunlit clinic with a friendly receptionist, rather than logging into a database. 

**Keywords:** Reassuring, Clean, Warm, Approachable, Unhurried, Hygienic.

---

## Design Style

### UI Style

**Primary Style:** Minimal Soft (Flat Design Variant)

Avoids heavy shadows, complex gradients, or "glassmorphism". Uses very flat, clean surfaces with significant whitespace and large, rounded border radii.

**Characteristics:**
- High use of negative whitespace.
- Rounded corners on all interactive elements.
- Very subtle, diffused drop shadows (if any) only for depth hierarchy on the dashboard.

### Design Aesthetic

**Aesthetic:** Modern Clinical / Consumer Wellness

Bridges the gap between medical trust and consumer ease. It relies on clean lines, lack of clutter, and highly legible data visualization.

---

## Color Direction

### Color Strategy

Evolving the clinic's core identity into a softer, premium palette.

### Palette Direction

| Role | Direction | Notes |
|------|-----------|-------|
| **Primary** | Sage Green / Mint | Replaces harsh clinic green; conveys growth, health, and calm. |
| **Secondary** | Muted Cerulean / Teal | Replaces harsh clinic blue; used for primary actions/buttons to convey trust. |
| **Background** | Warm Off-White | Prevents the sterile "hospital" feel of pure white (#FFFFFF). |
| **Text** | Dark Charcoal | Never pure black (#000000) to reduce eye strain. |

### Color Scheme Type

**Type:** Analogous (Greens and Blues)

---

## Typography Direction

### Type Approach

Friendly for marketing/headlines, highly functional for data/dashboard.

### Font Direction

| Role | Style | Examples | Rationale |
|------|-------|----------|-----------|
| **Headlines** | Geometric Sans-Serif | Poppins, Outfit | Feels modern, approachable, and friendly. |
| **Body/UI** | Neo-grotesque Sans-Serif | Inter, Roboto | Maximum legibility for dense dashboard data and small widget text. |

*Reference: [Typography Classification](../../../docs/models/design-nomenclature/typography-classification.md)*

---

## Layout Direction

### Layout Approach

Functional and hierarchical, utilizing different structures for the two distinct interfaces (patient-facing widget vs. owner-facing dashboard).

### Key Layout Elements

| Element | Approach | Notes |
|---------|----------|-------|
| **Patient Web Widget** | Card-Based / Stacked | A floating card that stacks the 3 contextual "Hero Buttons" vertically. Feels like a native mobile UI component. |
| **Owner Dashboard** | Bento Box Grid | Organizes complex data. The "After-Hours ROI Snapshot" is the largest, most prominent card in the grid. |
| **Navigation** | Minimal / Absent | The widget should not require navigation (it is action-driven). The dashboard uses a simple, hidden-until-needed sidebar. |

---

## Visual Effects

### Effect Usage

Subtle and highly restrained.

### Specific Effects

| Effect | Usage | Notes |
|--------|-------|-------|
| **Shadows** | Subtle | Very soft, diffused drop shadows to separate cards from the background. |
| **Animations** | Minimal | Micro-interactions on buttons only. Avoid all heavy motion or parallax to ensure fast rendering. |
| **Glassmorphism** | None | Avoided entirely to maintain accessibility and performance. |

---

## Photography & Imagery

### Photography Style

Minimal. Because this is an AI interface, the use of photography is severely limited to prevent cognitive overload and maintain fast load times.

### Image Sources

| Type | Source | Notes |
|------|--------|-------|
| **AI Avatar** | Custom / Synthesized | Use an abstract, branded AI icon/illustration rather than a stock photo of a human. This maintains transparency (users know they are talking to an AI) while still feeling warm and approachable. |
| **Icons** | Phosphor (Fill) or Heroicons (Solid) | Use soft, filled icons rather than thin, precise line icons. Filled icons reinforce the "Consumer Health" approachability and feel less rigidly clinical. |

### Image Guidelines

- No heavy, high-resolution lifestyle imagery in the widget itself to ensure instant loading.
- Avatars and icons must strictly adhere to the Sage Green / Muted Cerulean color palette.

---

## Design Constraints

*From Platform Requirements and brand needs*

- **Performance Over Aesthetics:** The patient web widget must load instantly, even on 3G/4G roaming connections (crucial for medical tourists). This mandates a text-first rendering approach with no heavy graphical assets in the widget itself.
- **Accessibility:** Must maintain WCAG AA minimum contrast ratios, especially given the softer color palette.

---

## Summary: Visual DNA

```
Style:        Minimal Soft / Consumer Wellness (Flat, rounded, highly legible)
Colors:       Soft Analogous (Sage Green, Muted Cerulean, Warm Off-White)
Typography:   Friendly Geometric Headlines (Poppins) + Highly Legible Body (Inter)
Mood:         Reassuring, Clean, Warm, Approachable, Unhurried, Hygienic
Key Element:  Whitespace and Rounded Cards (creating a calm, low-stress environment)
```

---

## Next Steps

- [ ] **Phase 2: Trigger Mapping** — Connect visuals to user psychology
- [ ] **Phase 4: UX Design** — Apply visual direction to designs
- [ ] **Phase 5: Design System** — Build design tokens from direction

---

## Reference Files

- [visual-references/](./visual-references/) — Collected reference images
- [Design Nomenclature](../../../docs/models/design-nomenclature/index.md) — Vocabulary reference

---

_Generated by Whiteport Design Studio_
