from src.brain_mri.utils.logger import logger

logger.info("Project started")

try:
    x = 10
    y = 0
    result = x / y

except Exception:
    logger.exception("An error occurred")

logger.info("Project finished")