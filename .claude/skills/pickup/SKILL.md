---
name: pickup
description: Resume a team role after /clear or at the start of a fresh session. Reads the role's pick-up note and the team docs, checks what changed, and continues. Use when the owner types /pickup, or says "pick up", "resume", or "you are <role>".
---

# Pickup: resume your role

1. **Role:** use the argument if one was given (`/pickup Shop`), otherwise the session title. If neither is clear, ask Manager, not the owner: "Which role am I?"

2. **Read, in this order, and nothing else yet:**
   - your pick-up note `docs/pickup/<role>.md` (if it exists) and your role brief `docs/roles/<role>.md`;
   - `docs/TEAM.md` (lanes, routing, the never-hang rule);
   - `STATUS.md`, the **Now** and **Next** sections only.
   `CLAUDE.md` is already loaded.

3. **Catch up on what changed while you were away** (cheaply):
   - the last few commits, and the top entry of `CHANGELOG.md`;
   - any queued messages. Treat them as newer than the note.

4. **Report to the owner in at most five lines**, starting with the business name: what is published, what is in flight, and the one thing you need from the owner (if anything). Then do the note's **Next step**.

5. **Tell Manager you're back** (skip this if you are Manager): send Manager one message, "picked up <Role>". Find Manager by session id, in this business's folder. Manager uses it to drop your "/clear me" flag on the board.

Keep the session lean: read sections, not whole files, and do not re-read what the note already says.
