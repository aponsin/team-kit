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
2. Answer the ten questions, one at a time. They are: the business name; what it does in one line; your first name; which lane packs you want (writing, shop, sales, operations, software); the languages; the names of the platforms you publish on (shop, blog, email); your two publish windows; and your quiet hours.
3. At the end it writes your files and prints a list of sessions to create.

You should see a message ending "Setup written. Create these sessions next."

If the setup asks you to **merge** (for example "Merge team-setup into main now?"), click **Yes, I'll merge**. The sessions in Step 3 read the files from `main`, so the merge must happen first.

## Step 3: create the sessions

For each session on the list, in this order, starting with Manager:

1. Click **New** in the sidebar (the **+** at the top left). A new, empty chat opens with a box to type in.
2. Before you type, check the environment shown at the bottom left of the box. It should be your business's environment, for example `acme-team`. If it isn't, click it and choose your business's environment from the list.
3. Check the model at the bottom right of the box. Click it and choose the model and effort shown on the list (for example **Opus** with **medium**, or **Sonnet** with **low**).
4. Type the role name on its own, and press Return. For the Writer session, that is just `Writer`. This names the session.
5. Then type the pickup command, and press Return:

   ```text
   /pickup <Role>
   ```

   For example, for the Writer session:

   ```text
   /pickup Writer
   ```

6. Check the session's name at the top of the chat. It should match the role on the list exactly, with the same capital letters. The name is how the team's scheduled checks and messages find each session. If the name is wrong, click the name at the top and rename it before you go on.

Start with **Manager**. Every other session reports to it.

## Step 4 (optional): turn on Remote Control

Remote Control lets you follow up on the team's work from your phone or another computer. You can open a session, read what it did, and reply, without being at your Mac. Skip this step if you only work at your Mac.

1. In the Manager session, type this and press Return. Or click the session's menu and choose **Remote Control**.

   ```text
   /remote-control
   ```
2. Turn it on for each session you want on your phone.
3. Check the Claude app on your phone. The sessions should appear there.

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

## Step 6: schedule the two checks

The two checks run on their own: the watchdog every 30 minutes, and the context keeper every 4 hours. Ask the **Manager** session to set them up. Manager works inside your business's folder, so it can find the files.

1. Open the **Manager** session.
2. Type this message, and press Return:

   ```text
   Create a scheduled task whose name is this business's name, a colon, and "watchdog", that runs every 30 minutes, using the prompt in tasks/watchdog.md in this folder.
   ```

3. Do the same again with this message:

   ```text
   Create a scheduled task whose name is this business's name, a colon, and "context keeper", that runs every 4 hours, using the prompt in tasks/context-keeper.md in this folder.
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
   - **Test decision.** Manager may show a test question with two buttons. Tap one. It should appear as sent.
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

- **A session stops and asks you to open it.** Open it, read the question, answer it, and go back to Manager.
- **A session is over 40% full.** Manager will ask it to `/handoff`. When it says "state saved", type `/clear` in that session, then `/pickup`.
- **The board shows "Blocked".** Open the item. It will say what is needed.
- **Anything else.** Ask Manager in plain words.

## Where to go next

- `CLAUDE.md`: the rules every session follows.
- `docs/TEAM.md`: who does what.
- `LESSONS.md`: the traps other teams have hit, and the rules that came from them.
- `docs/GOAL.md`: the goal, what "proven" and "disproven" mean, and the verdict date. Fill it in with the owner before the first big task.
