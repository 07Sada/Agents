# """Run the Day 1 worker against the board as a plain subprocess.

# Seeds one task ("read notes.txt, translate to Marathi, write marathi.txt"),
# then lets the ADK agent loop work it: read the board, read the file through the
# filesystem MCP server, translate, write the Marathi back, and mark the task
# done. This is exactly how a worker runs on Day 5, just with one task.

#     uv run worker.py              # seed a fresh task and run the agent
#     uv run worker.py --seed-only  # just seed, then drive it from `adk web`
# """

# from __future__ import annotations

# import argparse
# import asyncio 

# from quiet import silence 
# silence()

# import board 
# from google.adk.runners import InMemoryRunner 
# from task_worker.agent import WORKSPACE, root_agent