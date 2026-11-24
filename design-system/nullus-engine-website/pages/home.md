# Nullus Home Page Override

This page targets an open-source-adjacent, developer-first game engine website. It overrides the generated project category and uses the actual Nullus product context.

## Direction

- Dark technical interface with Swiss information hierarchy
- Real Editor and Launcher screenshots as the primary visual proof
- HUD-inspired grid, signal cards, ticker metadata, thread lines, terminal details, and restrained motion
- One primary CTA per section

## Tokens

```css
--bg: #070b12;
--bg-elevated: #0b121d;
--surface: #0e1724;
--surface-raised: #131f2f;
--text: #f2f6fb;
--text-muted: #91a3b8;
--line: rgba(162, 188, 215, 0.16);
--accent: #68ddff;
--accent-strong: #2397ff;
--warm: #f5b858;
--success: #9de56a;
```

## Typography

- UI and body text use IBM Plex Sans
- Headlines use Space Grotesk
- Code and technical labels use JetBrains Mono

## Content order

1. Hero with positioning, Editor screenshot, and build CTA
2. Capability proof strip
3. Scrolling engine signal ticker
4. Why Nullus advantage panel with runtime, RHI, content, and scripting proof
5. Rendering, Editor, assets, scripting, simulation, and build cards
6. Thread model and FrameGraph architecture panel
7. Four-step creation loop
8. Developer documentation path
9. Platform support matrix
10. Editor and Launcher screenshot gallery
11. Platform-aware quickstart terminal
12. Final build CTA and project footer

## Interaction rules

- Mobile navigation is a collapsible top menu
- Language toggle switches the main content between Chinese and English
- Quickstart tabs switch Windows, Linux, and macOS commands
- Copy action gives visible feedback and retains keyboard focus
- Scroll reveals use opacity and small translateY values
- The engine ticker pauses on hover and is disabled by reduced-motion preferences
- Signal cards use status labels, measured bars, and pipeline diagrams as supporting content
- Reduced motion renders reveal elements in their final state
