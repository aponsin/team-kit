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

**The owner had to clear every session by hand, every day.** Manager can clear only the sessions it started, and not while their Remote Control is on. It can't clear sessions the owner started, and a session can't clear itself.
*Rule:* the owner starts only Manager, and Manager starts every other session. Manager then resets its own sessions (Remote Control off, clear, `/pickup`, Remote Control on). The owner clears only Manager.

**Manager couldn't start sessions from a phone message.** Starting a session works only on the owner's words typed on the host computer, not over Remote Control, a board click or another agent's message.
*Rule:* the owner types "start <Role>" in the Manager session on the host computer.

**Eight board items were logged up to 39 minutes in the future.** Times were estimated instead of read.
*Rule:* read the real clock before writing any timestamp.

**Steps logged by Manager from relayed messages went stale, with wrong times.**
*Rule:* each role logs its own steps on the board as they happen, and closes every step at hand-over.

**The "every ask on the board" rule failed three times in one evening.** A rule in a document is easy to skip under pressure.
*Rule:* where a rule keeps failing, enforce it with a check that runs on its own. The kit includes a hook (`.claude/hooks/red-ask-board.py`) that stops a reply with a 🔴 ask unless the board's waiting list was written in the same turn.

## Swapping and resetting sessions

**A new session for a role missed what the old one did after its last note.**
*Rule:* the new session runs `/pickup <Role>`, then reads the old session's last 20 or so messages as data, never messaging it. The owner archives the old session from the sidebar on the host computer. Archiving from Remote Control only drops the link.

**Commands the old session had been allowed were refused in the new one.** Permissions granted at a prompt don't carry over, and some commands look like self-approval to the safety check.
*Rule:* give such commands a lasting allow rule in settings, with the owner's yes, and list it in `START-HERE.md`.

**A cleared agent's "/clear me" flag stayed on the board.**
*Rule:* the pickup skill ends by telling Manager "picked up <Role>", and Manager drops the flag.

## The owner's habits

**Mock-ups reached the owner straight from an agent, outside the board.**
*Rule:* look mock-ups go to Manager, who puts them on the board as a decision with labelled screenshots.

**The board's automatic replies to button presses promised too much.**
*Rule:* Manager follows each one with an accurate note in the same thread.

**The red-ask check fired on a mere mention of the red mark.** It blocked a session that wasn't asking anything.
*Rule:* the check reacts only when the mark starts a line, the way a real ask is written.

## Outreach

**Warm contacts who were interested still didn't say yes.** One read the message as a scam. Another feared the offer would hurt something he already had. A message stacked with guarantees read as too good to be true.
*Rule:* open with the real person (name, town, phone), give one believable reason it's easy, keep one guarantee line, state the plain price, send no attachments to a stranger, and ask for a one-word YES. The Sales and Outreach briefs carry the full list.

## The flight board, continued

**The memory tiles looked frozen.** They were fed only by a keeper that ran every few hours.
*Rule:* each role writes its own memory reading whenever it logs a step. The keeper (every 2 hours) is used only to decide who gets reset.

**A step landed on the wrong board item.** One id had been reused for two pieces of work.
*Rule:* one board id per task, never reused.

**Model settings drifted after crashes, unnoticed.**
*Rule:* the board shows each session's model and effort under its name, checked against `docs/MODELS.md`.

**Two crew-list notes went stale in a day.**
*Rule:* Manager updates a role's note whenever it goes idle or picks up new work.
