#!/usr/bin/env python3

import json
import sys
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()

DATA_PATH = Path(__file__).parent.parent / "data" / "commands.json"

def load_commands():
    with open(DATA_PATH) as f:
        return json.load(f)

def show_topics(commands):
    console.print("\nAvailable topics:\n", style="bold cyan")
    for t in commands:
        console.print(f" • {t}")

def show_commands(topic, commands):
    table = Table(title=f"Commands for {topic}")
    table.add_column("Command", style="green")
    table.add_column("Description", style="white")

    for c in commands[topic]:
        table.add_row(c["cmd"], c["desc"])

    console.print(table)

def search(term, commands):
    table = Table(title=f"Search results for '{term}'")
    table.add_column("Command", style="green")
    table.add_column("Description")
    table.add_column("Topic", style="cyan")

    for topic, cmds in commands.items():
        for c in cmds:
            if term.lower() in c["cmd"].lower() or term.lower() in c["desc"].lower():
                table.add_row(c["cmd"], c["desc"], topic)

    console.print(table)

def main():
    commands = load_commands()

    if len(sys.argv) == 1:
        show_topics(commands)
        console.print("\nUsage:")
        console.print(" mac <topic>")
        console.print(" mac search <term>")
        return

    if sys.argv[1] == "search":
        if len(sys.argv) < 3:
            console.print("Provide search term")
        else:
            search(sys.argv[2], commands)
        return

    topic = sys.argv[1]

    if topic in commands:
        show_commands(topic, commands)
    else:
        console.print("Topic not found.", style="bold red")

if __name__ == "__main__":
    main()
