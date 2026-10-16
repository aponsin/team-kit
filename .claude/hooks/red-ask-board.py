#!/usr/bin/env python3
# Stop hook: a reply with a red ask (🔴) must come with a board "waiting" write in the same turn.
# Agents that aren't Manager should send questions to Manager instead of asking the owner.
import json, sys
try:
    inp = json.load(sys.stdin)
except Exception:
    sys.exit(0)
if inp.get("stop_hook_active"):
    sys.exit(0)
path = inp.get("transcript_path")
if not path:
    sys.exit(0)
try:
    lines = open(path, encoding="utf-8").read().splitlines()
except Exception:
    sys.exit(0)
red = wrote = False
for line in reversed(lines):
    try:
        e = json.loads(line)
    except Exception:
        continue
    msg = e.get("message") or {}
    content = msg.get("content")
    if e.get("type") == "user":
        if isinstance(content, list) and content and all(isinstance(c, dict) and c.get("type") == "tool_result" for c in content):
            continue
        break  # start of this turn
    if e.get("type") != "assistant" or not isinstance(content, list):
        continue
    for c in content:
        if c.get("type") == "text" and "\U0001F534" in (c.get("text") or ""):
            red = True
        if c.get("type") == "tool_use" and c.get("name") == "ArtifactData":
            s = json.dumps(c.get("input") or {})
            if '"waiting"' in s and any(a in s for a in ('"set"', '"update"', '"batch"')):
                wrote = True
if red and not wrote:
    print(json.dumps({"decision": "block", "reason": "Your reply has a red ask (🔴) but you wrote nothing to the flight board's 'waiting' collection this turn. Manager: add the waiting item now (ArtifactData set), then finish. Any other agent: don't ask the owner directly; send the question to Manager and remove the 🔴."}))
sys.exit(0)
