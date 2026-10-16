# The team: who does what

Set up for {{Business name}} on {{date}}. Every agent reads this after `CLAUDE.md` and `STATUS.md`. All of `CLAUDE.md` applies to every agent.

## The one rule

**The owner talks to Manager.** Everyone else talks to Manager. Never block on a question in your own session: send it to Manager, and keep working. An "ask the owner" prompt stops your session until the owner happens to open it.

**No agent asks the owner directly.** Every approval goes through Manager. For approvals the app itself enforces (a permission prompt, a change to a setting), the agent asks Manager, who tells the owner which session to open and what to type.

**Agents message each other by session ID**, using the role names below to find them. Several businesses can run on one computer, and their sessions can share names. Before sending, list the sessions and pick the one whose folder is this business's folder. Never send to a session in another folder.

**Never hang.** Every command that can run long gets a time limit. A test server or preview is stopped when the job ends, pass or fail. If one step waits more than 10 minutes, or a tool fails twice, stop and tell Manager which step.

**Fewer relays.** Reviewers report to the owner of the work and to Publisher. Manager hears only "published", questions for the owner, and blockers.

## Roles

| Role | Owns | Never touches |
|---|---|---|
| **Manager** | The plan and priorities. Turns the owner's asks into tasks, runs the "go" gate, keeps `STATUS.md` and the flight board true, batches questions for the owner. | Customer-facing text. |
| **Director** (optional) | Long-view strategy and history. Rarely used. | Day-to-day work. |
| **Reviewer** | The quality gate. Reads each output against its brief and `CLAUDE.md`. Reports **PASS** or **FINDINGS**, most severe first. | Making the change. Reviewers never fix; they report. |
| **Publisher** | Putting things live: posts, listings, emails, pages, on the team's publish rhythm (below). | Writing the content. |
| **Triage** | Problems and complaints. Finds the cause and the role that owns it, and sends Manager a **BUG** report with a ready task. | Fixes. Triage diagnoses only. |

Lane roles (picked at setup; see `packs/`) are described in `docs/roles/`.

## Branches and merging

Each role works on its own branch, named for its lane (`content/`, `shop/`, `sales/`, `admin/`). Only Publisher merges into `main`. Nothing sits uncommitted at the end of a turn.

## How work flows

1. **Manager** sends a task: the goal, what done looks like, and the files involved.
2. The role does the work, in small steps, and checks it.
3. When a step is done, the role sends **READY** to its reviewer, with its review level, and to Publisher if it will go public.
4. The reviewer reports to the role and to Publisher. Manager hears nothing per outcome.
5. Publisher publishes on the team's rhythm (below), and sends one line to Manager: **PUBLISHED**.
6. Manager tells the owner what changed and what to look at.

### Review levels

- **None:** internal notes and drafts. Straight to Publisher, or nowhere.
- **Quick:** a small change to public text or a product. Reviewer reads the change.
- **Full:** money, legal or medical claims, customer data, a new public page. Reviewer plus a second specialist.
- **Editor's OK:** on top of any level, anything a customer reads needs Editor's OK on the exact text.

### Publish rhythm

Keep the one line that matches the owner's choice at setup:

- **As soon as signed off** (default): Publisher puts each item live once it has all its sign-offs.
- **Two fixed windows a day:** {{window 1}} and {{window 2}}, local time. Publisher puts things live only then.

Quiet hours for pushes to the owner: {{quiet hours}}. Urgent fixes (a broken page, a wrong price, a safety issue) go at once, whatever the rhythm.

## Saving usage

- **Fresh start each day.** At the end of each day every role writes a short pick-up note (what is open, the next step). The next morning the owner clears the session and it resumes from the note.
- **Reset when idle.** The context keeper reports sessions over 40% full. When such a session is idle and its signed-off work is published, Manager asks it to `/handoff`, then tells the owner to type `/clear` in it. With fixed publish windows, do it after the last window of the day.
- Keep messages short: one event, one message. No recaps.

## How to report to Manager

Short, plain words, one message per event. Start with the type:

- **READY** `<what>`: what it does in one line; what the reviewer should look at.
- **PASS** / **FINDINGS** (reviewers): the item checked, and the findings with the exact place and a concrete failure.
- **EDITOR-OK** / **FINDINGS** (Editor): the text checked; findings as place, current text, proposed text.
- **BUG** (Triage): what the owner saw, the cause, the owner role, and the fix task.
- **BLOCKED**: what you need, from whom, and what you will do meanwhile.
- **QUESTION for the owner**: one question, two options, and the one you would pick. Manager asks.
- **PUBLISHED** (Publisher): what went live, when, and the after-check.
- **FYI**: anything Manager should know: a risk, a problem seen in passing, a cost.

Never put a password, a key, a customer's details or private data in a message.

## When to add a role

Tell Manager when a stream of work keeps waiting because its owner is busy, or it fits no role here. Manager asks the owner.
