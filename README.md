# Hermes Council Builder Skill

A Hermes-compatible port of the OpenClaw `council-builder` skill.

It helps you design and create a personalized team of specialized Hermes profiles: content, research, coding, business, personal admin, ops, design, or whatever fits your workflow.

## Install

Direct install:

```bash
hermes skills install https://raw.githubusercontent.com/Abdullah4AI/hermes-council-builder-skill/main/SKILL.md --name hermes-council-builder
```

Or add as a tap:

```bash
hermes skills tap add Abdullah4AI/hermes-council-builder-skill
hermes skills install Abdullah4AI/hermes-council-builder-skill/hermes-council-builder
```

If tap layout differs in your Hermes version, use the direct raw `SKILL.md` install.

## Use

In Hermes:

```text
/skill hermes-council-builder
```

Then ask:

```text
Build me a council of agents for my workflow.
```

## Script

```bash
python3 scripts/init-hermes-council.py --council-name my-council --profiles researcher builder operator
```

The script creates Hermes profiles under:

```text
~/.hermes/profiles/<name>/
```

## Sharing vs OpenClaw ClawHub

OpenClaw had ClawHub. Hermes has GitHub-hosted skills and taps:

- direct raw `SKILL.md` install
- `hermes skills tap add owner/repo`
- `hermes skills publish PATH` for registry publishing when configured

This repo is structured to be usable as a GitHub-hosted skill.
