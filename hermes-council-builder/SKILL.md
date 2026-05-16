---
name: hermes-council-builder
description: Use when creating a personalized team of Hermes profiles/agent personas from a user's workflow. Interviews the user, designs a small council of specialized profiles, creates Hermes-compatible SOUL.md files, profile workspaces, routing docs, learning logs, and installable sharing docs. Use for “build me a team of agents”, “create specialized AI assistants”, “migrate OpenClaw council agents to Hermes”, or “set up agent profiles”.
version: 1.0.0
author: Abdullah AlRashoudi + Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, profiles, agents, multi-agent, skills, personalization]
    related_skills: [hermes-agent, subagent-driven-development, writing-plans]
---

# Hermes Council Builder

## Overview

Build a small, useful team of specialized Hermes profiles tailored to a user's real workflow. This is the Hermes-compatible port of the OpenClaw `council-builder` skill.

OpenClaw created `agents/<name>/SOUL.md` inside one workspace. Hermes has a better primitive for this: **profiles**. Each profile has isolated config, sessions, skills, memory, `SOUL.md`, and workspace under:

```text
~/.hermes/profiles/<profile-name>/
```

This skill helps an agent interview the user, design the council, create the profiles, write each profile's `SOUL.md`, and add routing/coordination docs so the default assistant can delegate work cleanly.

## When to Use

Use when the user asks for any of these:

- “build me a team of agents”
- “create specialized AI assistants”
- “make profiles for my workflow”
- “set up an agent council / crew”
- “migrate my OpenClaw agents/council to Hermes”
- “make agents based on how I use Hermes”

Don't use when:

- the user only needs one reusable workflow → create a normal skill instead
- the user only wants to install an existing skill → use `hermes skills install`
- the user wants one-off subtask delegation → use `delegate_task`

## Phase 1 — Discovery

Interview the user in small batches. Ask 2-3 questions max per turn.

### Round 1: Identity

- What do you do? Profession, projects, industry.
- What tools/platforms do you use daily?

### Round 2: Pain points

- What tasks eat most of your time?
- Where do you need the most help?

### Round 3: domains and style

- What languages should agents use?
- Which domains need coverage: coding, content, research, finance, scheduling, ops, design, etc.?
- Do you want a theme for names or should the agent choose memorable names?

### Optional: history analysis

If the user already has Hermes/OpenClaw history, inspect it before proposing the council:

- `session_search` for recurring tasks and corrections
- `~/.hermes/memories/USER.md` and `MEMORY.md` if available
- `~/.hermes/cron/jobs.json` and active skills for existing automation
- old OpenClaw paths only as historical input, never as live runtime state

Do not build until the roles are clear enough. If unclear, ask follow-ups.

## Phase 2 — Planning

Design the council:

1. Pick **3-7 profiles**. Fewer is better. Every profile must earn its existence.
2. Define each profile: name, role, specialties, personality angle, boundaries, and risk limits.
3. Map coordination: who researches, who drafts, who reviews, and where shared docs live.
4. Present the plan for approval.

Use Telegram-friendly lists instead of markdown tables when on Telegram:

```text
- Leia
  Role: content commander
  Specialties: X drafts, video scripts, content strategy
  Personality: bold, direct, audience-aware
```

Get explicit approval before writing profiles.

## Phase 3 — Building Hermes Profiles

Prefer the included script:

```bash
python3 scripts/init-hermes-council.py --council-name my-council --profiles leia r2 anakin
```

Useful flags:

```bash
--clone-default        # clone default profile config into each profile (default)
--no-clone            # create from scratch if supported by installed Hermes
--force               # overwrite generated SOUL.md/profile docs
--dry-run             # show what would be created
```

The script creates/updates:

```text
~/.hermes/profiles/<name>/SOUL.md
~/.hermes/profiles/<name>/PROFILE.md
~/.hermes/profiles/<name>/workspace/<name>/
~/.hermes/profiles/<name>/references/council-builder/
```

For each profile's `SOUL.md`:

1. Read `references/soul-philosophy.md`.
2. Use `assets/SOUL-TEMPLATE.md` as conceptual structure, but adapt to Hermes profile semantics.
3. Make each profile distinct. No copy-paste personalities.
4. Include hard rules for side effects: no posting, sending, payments, or destructive commands without permission.
5. Include useful Hermes skills/toolsets.
6. Include profile workspace paths.

## Phase 4 — Default Profile Routing Note

After creating profiles, show the user an optional routing note they can add to their default profile if they want Telegram/default sessions to recognize names like `Leia`, `R2`, or `Anakin`.

Suggested note:

```md
## Council profiles

- `leia` — content and social media drafts.
- `r2` — research and intelligence.
- `anakin` — coding and technical work.

When a task starts with one of these names, use the matching profile/persona. For large standalone work, run `hermes -p <profile> chat -q "..."` and summarize the result back.
```

Do not start multiple gateways with the same Telegram bot unless the user intentionally configured separate bots/channels. Usually the default Telegram gateway stays active and profiles are invoked by CLI/subprocess as needed.

## Phase 5 — Self-Improvement

Each profile should have a lightweight learning structure:

```text
workspace/<profile>/.learnings/LEARNINGS.md
workspace/<profile>/.learnings/ERRORS.md
workspace/<profile>/.learnings/FEATURE_REQUESTS.md
workspace/<profile>/references/verification-checklist.md
```

Hermes also has built-in memory and skills. Use them for durable facts/workflows instead of writing stale OpenClaw memory files.

Promotion rules:

- user correction about profile style → update profile `SOUL.md` or memory
- repeated workflow → create/update a Hermes skill
- repeated error/pitfall → update skill references or profile checklist
- one-off task progress → do not save to durable memory

## Phase 6 — Verification

After building:

```bash
hermes profile list
hermes profile show <profile>
python3 scripts/validate-council.py ~/.hermes/profiles <profile>...
```

Manual checks:

- [ ] Each profile exists in `hermes profile list`
- [ ] Each profile has `SOUL.md`
- [ ] Each profile has `PROFILE.md`
- [ ] Original/source material is in `references/council-builder/` if applicable
- [ ] Default `SOUL.md` has routing hints if requested
- [ ] No extra Telegram gateway was started accidentally
- [ ] Commands to use the profiles are shown to the user

## Phase 7 — Sharing the Skill

Hermes currently supports skill sharing mainly through GitHub-hosted skills and taps.

### Direct install from raw SKILL.md

```bash
hermes skills install https://raw.githubusercontent.com/<owner>/<repo>/main/SKILL.md --name hermes-council-builder
```

### Add as a tap

```bash
hermes skills tap add <owner>/<repo>
hermes skills install <owner>/<repo>/hermes-council-builder
```

If tap layout compatibility varies by Hermes version, direct raw `SKILL.md` install is the most reliable fallback.

## Common Pitfalls

1. **Porting OpenClaw paths literally.** OpenClaw used `agents/<name>/`; Hermes should use profiles under `~/.hermes/profiles/<name>/`.
2. **Creating too many profiles.** A 12-agent council sounds cool and becomes routing noise. Start with 3-5.
3. **Starting gateways per profile.** This can conflict if all profiles use the same Telegram bot. Keep one default gateway unless intentionally separated.
4. **Generic personas.** “Research Agent” and “Content Agent” are weak. Give each profile a strong voice, clear boundaries, and hard rules.
5. **No approval step.** Always present the proposed council and get explicit approval before writing profile files.
6. **Forgetting side-effect limits.** Content profiles draft; they do not post. Admin profiles draft emails; they do not send. Finance profiles analyze; they do not transact.
7. **Assuming profile changes affect current session.** Start a new session or use `/restart` for gateway when necessary.

## One-Shot Recipe: migrate old OpenClaw council

1. Locate old council/persona files using normal file search tools.
2. Create matching Hermes profiles:
   ```bash
   hermes profile create leia --clone
   hermes profile create r2 --clone
   ```
3. Preserve original persona docs under each profile's reference folder if the user wants migration fidelity.
4. Write a Hermes-native active `SOUL.md` that references originals as historical material.
5. Verify with `hermes profile list` and `hermes profile show <name>`.

## Verification Checklist

- [ ] Discovery completed or existing council files inspected
- [ ] Council plan approved by user
- [ ] Hermes profiles created, not just folders
- [ ] Active `SOUL.md` is Hermes-native
- [ ] Original files preserved under references when migrating
- [ ] Default profile routing hints were suggested if requested
- [ ] No secrets copied into repo/skill/profile files
- [ ] GitHub sharing instructions included
