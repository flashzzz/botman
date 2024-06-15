from src.config.env import ALLOWED_SERVER_IDS
from discord import Guild
from typing import Optional
from src.utils.logging_utils import logger

def should_block(guild: Optional[Guild]) -> bool:
    if guild is None:
        # dm's not supported yet (TODO: dm support)
        logger.info(f"DM not supported")
        return True

    if guild.id and guild.id not in ALLOWED_SERVER_IDS:
        # not allowed in this server
        logger.info(f"Guild {guild} not allowed")
        return True
    return False