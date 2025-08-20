from openai import OpenAI
from config import  OPENAI_API_KEY, AI_MODEL
from logger import get_logger

logger = get_logger(__name__)

def chat_setup() -> OpenAI:
    """
    Function sets up OpenAI client.

    Returns:
        client: OpenAI client
    """
    logger.info("Connecting to OpenAI...")
    try:
        client = OpenAI(
            api_key=OPENAI_API_KEY,
            timeout=60.0,
            max_retries=3
        )
        return client
    except Exception as e:
        logger.error(f"Error while connecting to OpenAI: {e}")
        raise


def compile_mail_request(mail_request: str) -> list[ dict[str, str]]:
    """
    Function creates a full AI request.

    Args:
        mail_request: body for AI request

    Returns:
        messages: AI request
    """
    logger.info("Compiling mail request...")
    messages = [
        {"role": "system", "content": "Ти — асистент, який аналізує вхідні емейли."},
        {"role": "user", "content": f"""
        {mail_request}
    Carefully analyze the following emails. Summarize the key points clearly and concisely. Then, based on the email contents, generate a prioritized list of actionable straightforward tasks I should perform. Format your answer in two separate sections titled 'Main Points from Emails' and 'Action Items', using bullet points and short sentences for clarity. Provide answer in English.
    """}
    ]
    return messages


def get_response(client: OpenAI, messages: list) -> object:
    """
    Function makes a request to OpenAI. And returns answer provided by AI.

    Args:
        client: OpenAI client
        messages: AI request

    Returns:
        response: AI response
    """

    logger.info("Getting response from OpenAI...")
    try:
        response = client.chat.completions.create(
            model=AI_MODEL,
            messages=messages,
            max_completion_tokens= 2000       # обмеження по довжині відповіді
        )
        return response
    except Exception as e:
        logger.error(f"Error while getting response from OpenAI: {e}")
        raise