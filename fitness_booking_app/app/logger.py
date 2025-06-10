import logging

# Configure root logger
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG for more details
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger("fitness_booking_app")
