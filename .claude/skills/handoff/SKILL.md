---
name: handoff
description: Save this role's state before clearing its context. Writes the role's pick-up note so a cleared session (or tomorrow's fresh one) resumes with /pickup and loses nothing. Use when the owner says "handoff", "save state", "reset", or the context is getting full.
---

# Handoff: save state, then clear

You are about to lose this conversation. Write down everything the next you needs, then tell the owner how to clear.

1. **Who am I?** Your role is the session title (for example Manager, Writer, Shop). Your pick-up note is `docs/pickup/<role>.md`. Create the folder and file if they do not exist.

2. **Rewrite the pick-up note** (replace it, do not append). Keep it under about 60 lines, as facts, not a story:
   - **Live:** what is published now that matters for your role.
   - **In flight:** every open task you own or wait on: name, state, who it waits on.
   - **Waiting on the owner:** open questions, in the order you will ask them. Note which one is asked now.
   - **Promised:** anything you told the owner or a teammate you would do or report.
   - **Rules from this session** that are not yet in `CLAUDE.md`, `docs/TEAM.md` or `DECISIONS.md`. Put lasting rules in those files and point to them.
   - **Traps:** what went wrong and how to avoid it.
   - **Next step:** the very first thing to do after pickup.
   Never put a password, a key, a customer's details or a private number in the note.

3. **Save any unfinished work** in the files it belongs to. Commit it if the repository is in use. Nothing sits uncommitted.

4. **Tell your teammates nothing.** Their messages will wait until after the clear.

5. **Tell the owner, in three lines:**
   - "State saved to `docs/pickup/<role>.md`."
   - If Manager started this session: "Manager will reset me." Otherwise: "Now type `/clear`, then `/pickup <Role>`."
   - Anything the owner is waiting on from you, so they know it survives.

Do not clear the session yourself. Manager resets the sessions it started; the owner clears the others.
