import os
from typing import Final
from dotenv import load_dotenv
load_dotenv()

DISCORD_TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY: Final[str] = os.getenv("OPENAI_API_KEY")
ALLOWED_SERVER_IDS: Final[list[int]] = []

server_ids = os.getenv("ALLOWED_SERVER_IDS").split(",")
for s in server_ids:
    ALLOWED_SERVER_IDS.append(int(s))