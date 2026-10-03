#!/bin/bash
# Bidirectional sync: hermes-config/notes/ ↔ Obsidian vault
REPO_DIR="/home/elbrus/hermes-config"
OBSIDIAN_DIR="/home/elbrus/hermes-notes"
LOG_FILE="/home/elbrus/.hermes/logs/cron-notes-sync.log"

cd "$REPO_DIR" || exit 1

# 1. User edits from Obsidian → repo (so they get committed)
rsync -a --delete "$OBSIDIAN_DIR/" "$REPO_DIR/notes/"

# 2. Commit & push (if anything changed)
if ! git diff --quiet; then
  git add notes/
  git commit -m "auto-sync: Obsidian notes $(date '+%Y-%m-%d %H:%M')" 2>/dev/null
  git push origin master 2>/dev/null
fi

# 3. Pull remote changes
git pull --ff-only origin master 2>/dev/null

# 4. Repo changes → Obsidian
rsync -a --delete "$REPO_DIR/notes/" "$OBSIDIAN_DIR/"

echo "[$(date '+%H:%M')] Sync tamam" >> "$LOG_FILE"
