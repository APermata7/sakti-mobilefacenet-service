import sys
from loguru import logger
from app.core.config import settings

def setup_logger():
    logger.remove()
    
    logger.add(
        sys.stdout,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name} | {message}",
        level=settings.LOG_LEVEL,
        colorize=True
    )
    
    logger.add(
        settings.LOG_FILE,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name} | {message}",
        level=settings.LOG_LEVEL,
        rotation="500 MB",
        retention="10 days",
        compression="zip"
    )
    
    return logger

log = setup_logger()