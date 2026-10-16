---
name: team-init
description: Set up a new business's team from this kit. Asks ten questions, one at a time, then writes the business's own CLAUDE.md, docs/TEAM.md, role briefs, STATUS.md and DECISIONS.md from the packs, and prints the sessions to create. Use when the owner types /team-init, or on a fresh copy of this kit.
---

# Team init: set up the business's team

You are setting up a team for a business that is not yet set up. The kit's files have placeholders in double braces, such as `{{Business name}}`. Your job is to replace them with the owner's answers and write the business's own files. Run once per business.

Work in this order. Do not write any file until all ten questions are answered and the owner has said "yes, write it".

## 1. Ask the ten questions

Ask them one at a time, in plain words. Wait for each answer. Offer a default in brackets where one exists. After each answer, say it back in one short line.

1. **Business name.** What is it called in public?
2. **What it does.** One line, in the owner's words.
3. **Owner's first name.** How the team should address the owner.
4. **Lane packs.** Which packs do you want? Pick any of: `writing` (Writer, Editor), `shop` (Shop, Support), `sales` (Sales, Outreach), `operations` (Admin, Research), `software` (Builder, Checker, Security, Release). [default: writing, shop, sales]. Then ask: **Reviewer** as a separate role? [default: no; Editor reviews text, and Manager checks the rest]. Manager, Publisher and Triage are always included.
5. **Languages.** Which languages do customers read? [default: English]
6. **Shop platform.** Name only, for example "Shopify" or "Etsy". No logins. Write "none" if there is no shop.
7. **Blog or content platform.** Name only. Write "none" if there is none.
8. **Email tool.** Name only, for example "Mailchimp". Write "none" if there is none.
9. **Publish rhythm.** Should Publisher put each item live as soon as it is signed off, or only at two fixed times a day? [default: as soon as signed off]. If fixed times: ask for the two local times and the time zone, for example "9:00 and 16:00 MST".
10. **Quiet hours.** When should the team not push to the owner's phone? [default: 21:00 to 08:00]

Never ask for passwords, keys, logins or account numbers. If the owner offers one, say: "Please don't paste that here. Keep it in the platform's own settings."

## 2. Confirm the plan

Show one short summary:

- the business name, owner's first name, languages, and the publish rhythm;
- the sessions that will be created (the list from the chosen packs, plus Manager, Publisher and Triage);
- which files you will write;
- that the files will be committed on a new branch called `team-setup` and then merged into `main`, so the Manager session reads them.

Ask: "Write these files now, commit them on `team-setup` and merge into `main`? (yes / change something)". Only write on "yes". That one yes covers the merge; do not ask about it again.

## 3. Write the files

First create the folders `docs/`, `docs/roles/`, `docs/briefs/` and `docs/pickup/` if they do not exist.

If a step has already run in an earlier attempt (for example, a file is already written or a line is already in `CLAUDE.md`), check it first and do not repeat it. Never add the same line twice.

Read these first: `CLAUDE.md`, `docs/TEAM.md`, `templates/`, and the role briefs in `packs/core/` and each chosen pack folder.

The business's folder name is the name of the folder this session is running in (the last part of the path). Use it wherever a file says `{{business folder}}`.

Then:

1. **`CLAUDE.md`**: replace `{{Business name}}` and add one line under the title: "For {{business}}: {{one-line description}}." Keep every rule.
2. **`docs/TEAM.md`**: replace the placeholders. Keep the roles table with only the roles that exist in this team, and remove the rows for roles not picked. If Reviewer is not picked, add to the Editor row: "also reviews the team's text." Fill in the publish rhythm and quiet hours: under "Publish rhythm", keep only the line that matches the owner's choice.
3. **`docs/roles/<Role>.md`**: for each chosen role, copy its brief from `packs/` (core or the chosen pack), replace placeholders with the business's name and platforms, and remove any lines that name a platform the owner did not pick.
4. **`STATUS.md`**: copy `templates/STATUS.md`. Fill in the business name and the date. Leave the sections empty except **Now**: "Team set up. Waiting for the first task."
5. **`DECISIONS.md`**: copy `templates/DECISIONS.md`. Add one entry: today's date, "Team set up", what was chosen (the packs, the publish rhythm, the platforms), and why.
6. **`CHANGELOG.md`**: copy `templates/CHANGELOG.md`, with one entry: "0.1.0: team set up."
7. **Scheduled-task prompts**: in `tasks/watchdog.md`, `tasks/context-keeper.md` and `tasks/money-watch.md`, replace `{{business folder}}` with the folder name, so the checks only watch this business's sessions, and replace `{{business name}}` with the business name, so each task's name is unique on this computer. Also replace the list of role names in each prompt with exactly the sessions this team will have (the list you print in step 4), so the checks watch the right sessions.
8. **Team files from the templates**: copy `templates/PUBLISH-LOG.md` to `docs/PUBLISH-LOG.md`, `templates/MONEY-WATCH.md` to `docs/MONEY.md`, and `templates/GOAL.md` to `docs/GOAL.md` (replace `{{Business name}}` and `{{date}}`; leave the goal sections empty for the owner to fill in). Create the folders `docs/briefs/` and `docs/pickup/`, each with an empty `.gitkeep` file so git keeps them. Copy `docs/RECOVERY.md` as it is.
9. **Outside helpers**: if the owner names an outside helper in setup, copy `packs/outside/outside-helper.md` to `docs/roles/outside-helper.md`. Otherwise skip it.
10. **Model table**: write `docs/MODELS.md` from `templates/model-table.md`, marking each chosen role with its model and effort.

Do not write any secrets. Do not create a place for passwords.

Commit the result on a new branch called `team-setup`, never directly on `main`:

1. If the current branch is `main`, create and switch to `team-setup`. If it already exists, switch to it.
2. Commit with the message "Team set up for {{business}}".
3. Merge `team-setup` into `main` (the owner's yes in step 2 covers it). Tell the owner: "Setup is merged into `main`. Now create the sessions, starting with Manager." Nothing uncommitted at the end.

## 4. Print the session list

Print the list of sessions the team will have, in this order: Manager, then the packs' roles, then Publisher and Triage, each with its model and effort from `docs/MODELS.md`. This list is for reference: the owner creates only Manager.

Then print exactly what the owner does next, as three separate messages, never combined:

- In a new session in this environment, with Opus at medium effort, send first: `Manager`
- Then send: `/pickup Manager`
- When Manager replies, send: `Start the rest of the team.`

Then say in one line: "Manager starts the other sessions. START-HERE.md Step 3 shows how." Do not start any session yourself.

## Rules for this skill

- One question at a time. Never ask two in one message.
- Plain words. No acronyms without a short explanation.
- If an answer is unclear, ask once more with two examples. If it is still unclear, write "to be decided" and note it in `DECISIONS.md`.
