# The flight board: rules for Manager

The flight board is a private page the owner reads on a phone. It shows what is in flight, what is waiting on the owner (with buttons whose presses come back to Manager as comments), and what was published and when.

**Manager is the only writer.** Other roles report to Manager, and Manager updates the board in one batch at natural moments: a PUBLISHED line, a new ask from the owner, a decision answered. Batching keeps the cost down.

## Setup (done once, by Manager)

1. Load the `artifact-capabilities` skill before publishing. It lists the capability names and their settings.
2. Publish `board/team-board.html` as a private page with all three capabilities: `db` (the shared database), `comments` (the owner's button presses) and `assets` (screenshots). A page published without them shows no buttons and no screenshots, so this is the step that must not be skipped.
3. Check the published page before telling the owner it is ready:
   - the page loads and shows the heading "Flight Board";
   - a test decision with two options shows two buttons;
   - a test screenshot uploads and opens in the picture viewer.
   If any check fails, republish with the missing capability. Do not tell the owner it is ready until all three pass.
4. Save the page's link in `STATUS.md`. Show it to the owner once, and say to bookmark it.

## The data

Collections in the page's database:

- `initiatives/<slug>`: `name`, `size` (XS, S, M, L, XL), `status` (`active`, `queued`, `stuck`, `paused`, `done`), `phase` (`plan`, `make`, `edit`, `review`, `sign`, `publish`, `live`), `summary`, `nextNote`, `nextAt` (ms), `waitingOn`, `etaLive` (ms), `who` (the role now on it), `plannedVersion`, `createdAt`, `doneAt`, `skip[]`, `phaseLog[]` (`phase`, `start`, `end`, `who`, `wait`).
- `waiting/<id>`: `kind` (`decision`, `action`, `session`, `later`), `text`, `where`, `initiative`, `since`, `done`, `steps[]` (numbered, click-by-click; fill this for every action), `expect` (what the owner should see), `options[]` (for decisions), `images[]` (for anything about how it looks).
- `events/<id>`: `at`, `version`, `text`. One line per published thing.
- `meta/live`: `version`, `commit`. Update on each PUBLISHED.
- `usage/<YYYY-MM-DD>`: one row per day at most.

## Rules

- **Every ask goes on the board**, even a small one, as an initiative, the moment it is handed out.
- **Decisions go on the board, never only in chat.** A question marked 🔴 in chat must also be a waiting item.
- **One ask at a time.** Ask the owner one thing on the board at once; queue the rest.
- **Decision buttons.** A decision with options gets one button per option, and the recommended one is marked. A decision about how something looks gets its own screenshots, labelled by option.
- **Actions carry steps.** Every item for the owner has steps, and anything typed into a terminal goes in a copy-box with its exact command.
- **Never put an action on the owner's list before its precondition is met.** Add "after X is live" items only once X is live.
- **Queue versus gate.** `wait: "busy"` means the item waits behind a busy role. `wait: "gate"` means it waits on a decision or condition. Keep each initiative's log sequential; close an entry when the state changes.
- **Close stale entries.** When an initiative is done, mark it `done` and set `doneAt`. Anything with no movement for a week is marked `paused` with a note.
- **Replies.** When the owner presses a button or writes a note, the page sends a comment to Manager. At the start of every Manager turn, check the waiting items for a `response` that is not yet done. Act on it, mark the item done, and resolve its comment thread.
- **Usage.** One row per day at most, from the platform's job times and session usage where easy. Estimates are fine; say so.
- **No private data on the board.** No customer names, order details, passwords, keys or bank details. Describe the thing, not the person.
