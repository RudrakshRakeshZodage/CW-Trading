import logging
import os

def setup_logger():
    # Ensure logs directory exists
    os.makedirs("logs", exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("logs/crew_execution.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("AdCrew")

logger = setup_logger()
