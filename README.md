# Mac Command Agent

A CLI assistant to quickly search and reference Mac terminal commands — now with NLP-powered search that understands natural language queries and tolerates typos.

## Features

- **NLP search** — find commands using plain English, not exact keywords
- **Typo tolerance** — fuzzy matching corrects misspelled queries automatically
- **BM25 ranking** — results sorted by relevance, not insertion order
- **81 commands** across 9 topics: `files`, `git`, `network`, `process`, `disk`, `permissions`, `text`, `brew`, `system`
- Clean, readable CLI output powered by Rich

## Installation

```bash
git clone https://github.com/myst9811/mac-command-agent
cd mac-command-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

### List all topics

```bash
python src/main.py
```

### Browse commands by topic

```bash
python src/main.py files
python src/main.py git
python src/main.py network
python src/main.py process
python src/main.py disk
python src/main.py permissions
python src/main.py text
python src/main.py brew
python src/main.py system
```

### Search commands (NLP-powered)

```bash
python src/main.py search "<query>"
```

The search understands natural language and corrects typos:

```bash
# Natural language queries
python src/main.py search "show files"
python src/main.py search "running processes"
python src/main.py search "kill process by name"
python src/main.py search "disk space"
python src/main.py search "homebrew install package"

# Typos are corrected automatically
python src/main.py search "gti commti"       # → git commit
python src/main.py search "dsk spase"        # → df -h, du -sh

# Multi-word queries
python src/main.py search "find and replace text in file"
python src/main.py search "check what is on a port"
```

## Available Topics

| Topic | Description | Commands |
|---|---|---|
| `files` | File and directory operations | ls, cd, find, cp, mv, rm, mkdir... |
| `git` | Git version control | clone, commit, push, stash, merge... |
| `network` | Networking and connectivity | ping, curl, netstat, traceroute... |
| `process` | Process management | ps, kill, pgrep, pkill, htop... |
| `disk` | Disk usage and storage | df, du, diskutil, ncdu... |
| `permissions` | File permissions and ownership | chmod, chown, stat, umask... |
| `text` | Text processing and search | grep, sed, awk, sort, wc, head... |
| `brew` | Homebrew package manager | install, update, upgrade, search... |
| `system` | macOS system info and settings | sw_vers, uptime, caffeinate... |

## Extending the Command Database

Commands are stored in `data/commands.json`. To add your own:

```json
{
  "mytopic": [
    {"cmd": "my-command --flag", "desc": "Description of what it does"}
  ]
}
```

Add a new key for a new topic, or append entries to an existing topic array. The NLP search index is rebuilt automatically on each run.
