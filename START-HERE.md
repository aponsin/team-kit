# Start here: set up your team in 15 minutes

You will create a folder for your business, run one setup skill, then open a few Claude Code sessions, one per role. No coding is needed. Each step says what to click and what you should see.

If a menu looks different from what is written here, the app has changed. Look for the closest match and carry on. Ask Manager if you are stuck.

## Before you start

1. **Install Claude Code desktop.** Download it from claude.com/claude-code and open it. Sign in with your Claude account.
2. **Install Git.** On a Mac, open the Terminal app and type `git --version`, then press Return. If a box offers to install developer tools, accept it.
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

1. Click in the message box at the bottom of the chat window (the box that says "Reply…" or similar, where you type to Claude). Type `/team-init` and press Return.
2. Answer the ten questions, one at a time. They are: the business name; what it does in one line; your first name; which lane packs you want (writing, shop, sales, operations, software); the languages; the names of the platforms you publish on (shop, blog, email); your two publish windows; and your quiet hours.
3. At the end it writes your files and prints a list of sessions to create.

You should see a message ending "Setup written. Create these sessions next."

## Step 3: create the sessions

For each session on the list:

1. Click **New session** (the **+** at the top of the sidebar).
2. Click the session's name at the top and type the name shown on the list, for example `Manager`.

   **Name it exactly as shown, with the same capital letters.** The name is how the team's scheduled checks and messages find each session. A session named `writer` or `Writer 2` will be missed. If you make a mistake, rename the session (click its name again) before you go on.
3. Under the model menu, pick the model and effort shown on the list.
4. Paste the first message from the list and press Return. It is always `You are <Role>. Run /pickup <Role>.`, with the role name filled in, for example `You are Writer. Run /pickup Writer.`

Start with **Manager**. Every other session reports to it.

## Step 4 (optional): turn on Remote Control

Remote Control lets you follow up on the team's work from your phone or another computer. You can open a session, read what it did, and reply, without being at your Mac. Skip this step if you only work at your Mac.

1. In the Manager session, type `/remote-control` and press Return. Or click the session's menu and choose **Remote Control**.
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

1. In the desktop app, click **Scheduled** in the sidebar, then **New task**.
2. Name it `Team watchdog`. Paste the text from `tasks/watchdog.md` into the prompt box. Set it to run every 30 minutes.
3. Click **New task** again. Name it `Context keeper`. Paste `tasks/context-keeper.md`. Set it to run every 4 hours.
4. Click **Save**. Each should show "Next run" in its row.

## Step 7: open the flight board

1. In the Manager session, type: "Set up the flight board." Manager publishes the board from `board/team-board.html` as a private page.
2. Manager sends you a link. Open it on your phone and bookmark it.
3. You should see the heading "Flight Board", with "Waiting on you: nothing yet".

## Step 8: the first test

1. In the Manager session, type: "Start with a short test: write one product description for [an item you sell] and send it through review."
2. Watch the board. The item appears under "Initiatives in flight" and moves through the phases.
3. When Manager asks you for an approval, it appears under "Waiting on you". Tap **Done**, or type your answer.

If the task finishes, setup is complete.

## When something goes wrong

- **A session stops and asks you to open it.** Open it, read the question, answer it, and go back to Manager.
- **A session is over 40% full.** Manager will ask it to `/handoff`. When it says "state saved", type `/clear` in that session, then `/pickup`.
- **The board shows "Blocked".** Open the item. It will say what is needed.
- **Anything else.** Ask Manager in plain words.

## Where to go next

- `CLAUDE.md`: the rules every session follows.
- `docs/TEAM.md`: who does what.
- `LESSONS.md`: the traps other teams have hit, and the rules that came from them.
