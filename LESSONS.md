# Lessons: the traps, and the rule each one produced

Each entry is a trap a working team of Claude sessions fell into, in plain words, and the rule that now prevents it. Read it once. The rules are already in `CLAUDE.md` and `docs/TEAM.md`; this file says why they are there.

## Hangs and waiting

**A browser page script hung for eight hours, and another session about ten.** Long steps had no time limit, so nothing noticed.
*Rule:* every command that can run long has a time limit. Stop and report after 10 minutes on one step, or after two failures.

**A session sat for 3.5 hours waiting on a question nobody saw.** It asked the owner a question inside its own session, and the question waited until someone opened that session.
*Rule:* never ask the owner a question inside a session. Send it to Manager, and keep working.

**A permission prompt waited silently for approval.** A browser asked a site-approval question, and the session stopped on it.
*Rule:* no browser on outside sites. Use `curl` with a time limit, or ask Manager.

**A watchdog task now pings the owner about any session stuck on one step for 30 minutes.** Hangs were found only when someone noticed.
*Rule:* the watchdog task in `tasks/` runs every 30 minutes.

## Asking and deciding

**A decision asked only in chat was missed.** The owner asked why a question was not on the board.
*Rule:* every decision goes on the flight board, as well as in chat.

**The owner got several questions at once, and answered none of them.**
*Rule:* one question at a time. Batch the rest for later.

## Reviews and publishing

**A secret token shipped inside a public page.** Nobody checked what the browser downloads.
*Rule:* an independent review checks what the public page actually contains, before every publish.

**A change passed its tests, but a check guarding it had never actually run.** An edit matched nothing, so the guard looked tested when it was not.
*Rule:* after breaking a rule on purpose to test it, confirm the break really happened before trusting the green result.

**A stale server passed the whole test run.** A test ran against a server that was already running, not one it started itself.
*Rule:* tests run against a fresh copy the run starts itself.

**A sign-off was written for code that had changed since.** A new commit needs a new review.
*Rule:* a sign-off names the exact commit it reviewed. A new commit needs a new sign-off.

## Usage and context

**Sessions ran for days without a reset, and each turn got slower and more costly.** Long histories were re-read every turn.
*Rule:* `/handoff` before a session gets full, then `/clear` and `/pickup`. The context keeper reports sessions over 40%. Reset a session once it is idle and its signed-off work is published.

**Models drifted back to a default after a crash.** A session ran at the wrong model and effort without anyone noticing.
*Rule:* `templates/model-table.md` is checked after any restart.

**Sessions were asked to hold their work until a quiet moment, and it never came.** Busy roles were never reset.
*Rule:* reset at a defined point (idle, with its signed-off work published), not when things feel quiet.

## Records and secrets

**Private notes were saved in the repository, and had to be rewritten out of history.**
*Rule:* secrets and private data never go in the repository. If one does, stop and ask the owner before any more commits.

**A bot account was suspended after an automated flood of requests.** Appeal it, do not recreate it.
*Rule:* one account per tool. Rate limits are part of the design, not an afterthought.

## Writing for the owner

**Words such as "guaranteed" and "number one" were written into customer copy without a source.**
*Rule:* no claims without a source. Use "found on search" style wording, never a ranking promise.

## The flight board

**Time kept counting on finished steps.** A step's log entry was left open after the work moved on, so the board showed hours of work that never happened.
*Rule:* close the log entry at every hand-over. The board also caps an open step at 2 hours.

**A question was asked only in chat, and the owner missed it.**
*Rule:* every ask to the owner goes on the board, never only in chat.

**Owners copied text by hand, and made mistakes.**
*Rule:* any text the owner pastes (a command, a message) goes in a copy box.

## Scheduled tasks

**A scheduled task's alerts silently never arrived.** Its messages to Manager needed approval, and no one was there to approve them.
*Rule:* add the messaging permission to `~/.claude/settings.json` once (`START-HERE.md` Step 5), so scheduled tasks can reach Manager.

**Real agents stopped being measured after a day or two.** Each scheduled run leaves its own session behind, and the runs pushed the agents out of the most recent 25 sessions the task looked at.
*Rule:* when a scheduled task lists sessions, set the limit well above the number of agents (the kit uses 50), and skip the tasks' own runs.

**A single push notification was missed, and a session waited hours for its reset.**
*Rule:* anything the owner must act on also gets a standing sign on the board. A saved session shows as a dashed red tile, "Saved · /clear me", until it is cleared.

**Manager tried to clear sessions itself, and couldn't.** A session can only clear the sessions it started, and Remote Control blocks it too.
*Rule:* clearing stays with the owner. Manager asks for `/handoff`, marks the tile, and tells the owner which sessions to clear.
