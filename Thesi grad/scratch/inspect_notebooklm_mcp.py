import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Search for notebooklm related files in AppData or user profile
user_dir = os.path.expanduser('~')
print(f"User dir: {user_dir}")

# Look for credentials, config, or cookie files
for root, dirs, files in os.walk(user_dir):
    # Only search top-level config folders to be fast
    if any(p in root.lower() for p in ['appdata\\local\\temp', 'node_modules', '.git', 'appdata\\local\\microsoft', 'appdata\\local\\google']):
        continue
    for file in files:
        if 'notebooklm' in file.lower() or 'cookie' in file.lower() and ('mcp' in file.lower() or 'zotero' in file.lower()):
            print(os.path.join(root, file))
