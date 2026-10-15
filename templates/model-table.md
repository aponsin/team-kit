# Model table

Which model and effort each role uses. Check this file after any crash or restart, because sessions can drift back to a default.

Rule of thumb: **judgment** roles use Opus at medium effort. **Mechanical** roles use Sonnet at low effort. **Tasks** that only check or count use Haiku at low effort.

| Role | Model | Effort | Why |
|---|---|---|---|
| Manager | Opus | medium | Judgment: plans and batches for the owner |
| Director | Opus | medium | Judgment: long view |
| Reviewer | Opus | medium | Judgment: finds the real problems |
| Writer | Opus | medium | Judgment: voice and facts |
| Editor | Opus | medium | Judgment: language and facts |
| Shop | Sonnet | low | Mechanical: listings, prices from the source |
| Support | Sonnet | low | Mechanical: drafts replies for the owner's approval |
| Sales | Opus | medium | Judgment: follow-ups and what to say next |
| Outreach | Sonnet | low | Mechanical: drafts from a template |
| Admin | Sonnet | low | Mechanical: notes, calendar, records |
| Research | Opus | medium | Judgment: sources and summaries |
| Publisher | Sonnet | low | Mechanical: puts approved text live |
| Triage | Opus | medium | Judgment: diagnosis |
| Builder | Opus | medium | Judgment: code |
| Checker | Opus | medium | Judgment: review |
| Security | Opus | medium | Judgment: attacker's view |
| Release | Sonnet | low | Mechanical: ships approved changes |
| Watchdog task | Haiku | low | Count and report |
| Context keeper task | Haiku | low | Count and report |

Change a row here and in the session's own settings together.

## Permission mode

Every session runs in **auto** mode. "Read-only" roles (Reviewer, Checker, Security, Triage) are a **rule in their brief**, not a setting: they report and never change files. The brief is the only place that decides it, so check the brief if a role starts changing things.

