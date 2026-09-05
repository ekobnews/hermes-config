#!/bin/bash
# Sync notes between repo and Windows Obsidian vault
REPO_NOTES="$HOME/hermes-config/notes"
WIN_NOTES="/mnt/c/Users/ELBRUS/Documents/hermes-notes"

case "${1:-help}" in
  to-win)
    echo "Syncing repo → Windows..."
    cp -r "$REPO_NOTES"/* "$WIN_NOTES"/ 2>/dev/null
    echo "Done"
    ;;
  to-repo)
    echo "Syncing Windows → repo..."
    cp -r "$WIN_NOTES"/* "$REPO_NOTES"/ 2>/dev/null
    echo "Done"
    ;;
  *)
    echo "Usage: sync-notes to-win | to-repo"
    ;;
esac