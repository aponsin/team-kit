# Start here: set up your team in 15 minutes

You will create a folder for your business, run one setup skill, then open a few Claude Code sessions, one per role. No coding is needed. Each step says what to click and what you should see.

If a menu looks different from what is written here, the app has changed. Look for the closest match and carry on. Ask Manager if you are stuck.

## Before you start

1. **Install Claude Code desktop.** Download it from claude.com/claude-code and open it. Sign in with your Claude account.
2. **Install Git and Python.** On a Mac, open the Terminal app (press Command and Space, type `Terminal`, press Return). Type `git --version` and press Return, then type `python3 --version` and press Return. Each should print a version number, such as `git version 2.x` or `Python 3.x`.
   - If a box offers to install **developer tools**, click **Install**, wait until it finishes, then run both commands again. This installs both Git and Python.
   - If either command still says "command not found", stop and tell Manager what the screen says.
3. **Get this kit.** On GitHub, open the team-kit page and click **Use this template**, then **Create a new repository**. Name it after your business, for example `acme-team`. Keep it **private**. Click **Create repository**.
4. **Copy it to your Mac.** Open the Terminal app and type the command below. Before you press Return, replace the two parts in angle brackets (`<` and `>`), and leave out the brackets themselves:

   - `<your-github-username>`: your GitHub username. It is shown on your GitHub profile page, under your name. Not your email.
   - `<your-repo-name>`: the name you gave the new repository in step 3, for example `acme-team`. Use the same name in both places.

```bash
git clone https://github.com/<your-github-username>/<your-repo-name>.git ~/Documents/<your-repo-name>
```

You should see "Cloning into..." and then the prompt returns.

## Step 1: create an environment for the business

An environment is a named place in Claude Code desktop that holds one business's folder and sessions. Give each business its own, so its sessions stay apart from your other projects.

1. At the bottom of the window, click the environment menu (it says **Choose environment** or shows the name of the current one). Click **New environment**.
2. In the **Name** box, type your business name, for example `acme-team`.
3. Under **Folders**, click **Add**. Choose `~/Documents/<your-repo-name>` (the folder from step 4 above). If the list already shows a different folder, remove it, so that only your business's folder is listed.
4. Leave **Environment variables** empty. Click **Create environment**.
5. If a box asks whether you trust the folder, click **Trust**.

## Step 2: run the setup

1. Click in the message box at the bottom of the chat window (the box that says "Reply…" or similar, where you type to Claude). Type this and press Return:

   ```text
   /team-init
   ```
2. Answer the ten questions, one at a time. They are: the business name; what it does in one line; your first name; which lane packs you want (writing, shop, sales, operations, software); the languages; the names of the platforms you publish on (shop, blog, email); how often to publish (as soon as work is approved, or at two fixed times a day); and your quiet hours.
3. After the ten questions, it shows you a short plan: your answers, the sessions it will create, and the files it will write. Check it, then tap **Yes, write it** (or **Change something** if an answer is wrong). This is the only approval in the setup. It also covers merging the files into `main`.
4. It writes your files and prints a list of sessions to create.

You should see a message ending "Setup written. Create these sessions next."

If the setup asks you to **merge** (for example "Merge team-setup into main now?"), click **Yes, I'll merge**. The sessions in Step 3 read the files from `main`, so the merge must happen first.

## Step 3: create Manager, and let it start the team

You create one session yourself: **Manager**. Manager then starts every other session for you.

1. Click **New** in the sidebar (the **+** at the top left). A new, empty chat opens.
2. Check the environment at the bottom left of the box. It should be your business's environment, for example `acme-team`. If it isn't, click it and choose yours.
3. Check the model at the bottom right of the box. Choose **Opus** with **medium** effort.
4. Type this and press Return. It names the session:

   ```text
   Manager
   ```

5. Then type this and press Return:

   ```text
   /pickup Manager
   ```

6. When Manager has replied, type this and press Return. **Type it on this Mac**, not from your phone or another computer: Manager can only start sessions on words typed on the computer it runs on.

   ```text
   Start the rest of the team.
   ```

   Manager starts one session per role on the setup list, each with its name, model and effort. They appear in the sidebar under **Manager**. It may take a minute or two.
7. Check the sidebar: each role on the setup list should appear once, with exactly its name. If one is missing, type `start <Role>` in the Manager session on this Mac, for example:

   ```text
   start Publisher
   ```

   If a role appears twice, archive the extra one from the sidebar (right-click it, then **Archive**).

Let Manager start every session except itself. Manager can reset the sessions it started on its own, so you only ever clear Manager by hand.

## Step 4 (optional): turn on Remote Control

Remote Control lets you follow up on the team's work from your phone or another computer. You can open a session, read what it did, and reply, without being at your Mac. Skip this step if you only work at your Mac.

Manager turns Remote Control on for every session it starts. You only turn it on for Manager.

1. In the Manager session, type this and press Return. Or click the session's menu and choose **Remote Control**.

   ```text
   /remote-control
   ```
2. Check the Claude app on your phone. The sessions should appear there.

## Step 5: let scheduled tasks reach Manager (one time)

Two scheduled tasks check on the team: the watchdog and the context keeper. They need permission to message Manager without asking you each time. This command adds that permission for you. You don't need to edit any file by hand.

1. Open the **Terminal** app (press Command and Space, type `Terminal`, press Return).
2. Copy this whole line, paste it into the Terminal, and press Return:

```bash
python3 -c "import json,os,shutil; p=os.path.expanduser(\"~/.claude/settings.json\"); shutil.copy(p,p+\".bak\"); d=json.load(open(p)); a=d.setdefault(\"permissions\",{}).setdefault(\"allow\",[]); r=\"mcp__ccd_session_mgmt__send_message\"; a.append(r) if r not in a else None; json.dump(d,open(p,\"w\"),indent=2); print(\"done\")"
```

3. You should see the word `done`.

If instead you see **"command not found"**, or a box asks you to install **developer tools**, click **Install**, wait until it finishes (it can take 10 minutes), then paste the line again. If it still fails, don't try to fix it yourself. Tell Manager what the screen says, and Manager will set up the permission for you in the Claude session.

The command also saves a backup of your settings file next to it, called `settings.json.bak`. It's safe to run it again: it won't add the permission twice.

This is the only permission the kit needs. If your team later adds a command that keeps being refused after a session is replaced, Manager will ask you before adding a lasting permission for it, and list it here.

## Step 6: schedule the two checks

The two checks run on their own: the watchdog every 30 minutes, and the context keeper every 2 hours. Ask the **Manager** session to set them up. Manager works inside your business's folder, so it can find the files.

1. Open the **Manager** session.
2. Type this message, and press Return:

   ```text
   Create a scheduled task whose name is this business's name, a colon, and "watchdog", that runs every 30 minutes, using the prompt in tasks/watchdog.md in this folder.
   ```

3. Do the same again with this message:

   ```text
   Create a scheduled task whose name is this business's name, a colon, and "context keeper", that runs every 2 hours, using the prompt in tasks/context-keeper.md in this folder.
   ```

4. If Claude says a schedule that often isn't allowed, reply "yes, hourly is fine". The watchdog still works at an hourly check, just less often.
5. Set the model for each task. Open the task on the **Scheduled** page, choose **Haiku** with **low** effort. Claude can't set these for you.
6. Check the result: open the **Scheduled** page in the sidebar. Each task should show its name, which starts with your business's name, its schedule, and "Next run". Open each task and check its prompt: it should name your business's folder, and must not contain `{{business folder}}`. If it does, tell Manager.
7. The tasks run only while the Claude desktop app is open. If the app was closed when a run was due, the run happens when you next open it.

If you'd rather set them up by hand, click **Scheduled**, then **New task**, then **Set up manually**. Fill in the name, paste the prompt from the file named in the message, and choose the schedule yourself.

## Step 7: open the flight board

1. In the Manager session, type this and press Return. Manager publishes the board from `board/team-board.html` as a private page.

   ```text
   Set up the flight board.
   ```

2. Manager will ask you a few quick checks in the Manager session. Each one comes with buttons. Tap the button that matches what you see:
   - **"Open the board and tell me whether it loads."** Open the link on your phone. Tap **Yes, it loads** if you see the heading "Flight Board". Tap **It does not load** if you don't, and say what you see.
   - **Test decision.** Manager puts a test question on the board with two buttons. Tap the row to open it, then tap one of the buttons.
     The first time, a box asks **"Let this artifact send messages to your Claude session?"** Tap **Allow**. This is how your answers on the board reach Manager. It asks only once. If you tap **Don't allow**, your answers stay on the board and Manager only sees them at its next check.
     After you allow it, the item should say your choice was sent to Manager.
   - **Test screenshot.** Manager may ask you to upload a picture. Tap the button, choose any photo, and confirm it opens.
3. Bookmark the link on your phone once the first check passes.
4. You should see the heading "Flight Board", with "Waiting on you: nothing yet".

If a check fails, don't skip it. Tap **It does not load**, or type what went wrong, and Manager will fix the board and ask again.

## Step 8: the first test

1. In the Manager session, type this and press Return. Replace the text in square brackets with an item you sell.

   ```text
   Start with a short test: write one product description for [an item you sell] and send it through review.
   ```
2. Watch the board. The item appears under "Initiatives in flight" and moves through the phases.
3. When Manager asks you for an approval, it appears under "Waiting on you". Tap **Done**, or type your answer.

If the task finishes, setup is complete.

## How to answer on the flight board

Manager puts every question for you on the board, under **Waiting on you**. There are three kinds:

- **Decision with options.** You see one button per option. One is marked **Manager's pick**. Tap the one you choose. To suggest something else, tap **Something else (say what)** and type it in the box.
- **Decision to approve a look.** You see pictures, labelled by option. Tap **OK** if you're happy, or **Change something** and say what to change in the box.
- **Action for you.** You see numbered steps, sometimes with a box to copy from. Do the steps, then tap **Done**. If you get stuck, tap **Something went wrong, help** and say where.

After you tap, the item shows "Sent to Manager". Manager picks it up at its next check, usually within a few minutes. If it still shows as waiting after that, send Manager a short message in the Manager session: "Board reply waiting: <the question>."

Only answer on the board, not in other sessions, so Manager sees every decision in one place.

## After a restart

If the Mac restarts, the app crashes, or a session stops responding, follow `docs/RECOVERY.md` in your business folder. It takes a few minutes.

## When something goes wrong

- **"Couldn't switch environments" warning.** Close it. Check that the environment at the bottom left of the message box shows your business's environment. If it does, carry on. If it doesn't, click it and choose yours.
- **"Turn on Worktree" suggestion.** Ignore it. The team doesn't need it.
- **A session stops and asks you to open it.** Open it, read the question, answer it, and go back to Manager.
- **A session is over 40% full.** Manager resets the sessions it started by itself, once they are idle and their work is published. For Manager itself (or any session you started by hand): when its tile on the board says "Saved · /clear me", type `/clear` in it, then `/pickup <Role>`.
- **The board shows "Blocked".** Open the item. It will say what is needed.
- **Anything else.** Ask Manager in plain words.

## Where to go next

- `CLAUDE.md`: the rules every session follows.
- `docs/TEAM.md`: who does what.
- `LESSONS.md`: the traps other teams have hit, and the rules that came from them.
- `docs/GOAL.md`: the goal, what "proven" and "disproven" mean, and the verdict date. Fill it in with the owner before the first big task.
