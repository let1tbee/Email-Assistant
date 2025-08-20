from config import RESPONSE_FILE
from logger import get_logger

logger = get_logger(__name__)

def save_response(response: object) -> None:
    """
    Function saves AI response to a file.

    Args:
        response: AI response

    """
    logger.info("Saving response...")
    with open(RESPONSE_FILE, 'w') as f:
        f.write(response.choices[0].message.content)