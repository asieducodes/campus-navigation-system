"""
main.py — Entry point for the Campus Navigation System.

Usage:
    python main.py           → launches CLI (default)
    python main.py --gui     → launches Tkinter GUI
    python main.py --both    → CLI first, then GUI on exit
"""

import sys
import os

# Ensure the project root is importable regardless of where you run from
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from storage.data_manager import get_or_create_graph


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "--cli"

    print("\n  Loading campus graph...")
    graph = get_or_create_graph()

    if mode == "--gui":
        from ui.gui_interface import run_gui
        run_gui(graph)

    elif mode == "--both":
        from ui.cli_interface import run_cli
        from ui.gui_interface import run_gui
        run_cli(graph)
        run_gui(graph)

    else:  # default: CLI
        from ui.cli_interface import run_cli
        run_cli(graph)


if __name__ == "__main__":
    main()