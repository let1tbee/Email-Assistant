from mails_handler import mail_setup, compile_email, pack_mail
from openAI_handler import get_response, chat_setup, compile_mail_request
from utils import save_response
from logger import get_logger

def main() -> int:
    """
     Main application entry point for email scraping and processing.

     This function orchestrates the entire workflow:
     1. Sets up email connection and retrieves emails
     2. Processes emails through AI analysis
     3. Saves the results
     """
    logger = get_logger(__name__)
    try:
        logger.info("="*60)
        logger.info("Starting email scraping application")
        logger.info("="*60)

        mail_ids, mail = mail_setup()
        mail_pack = compile_email(mail_ids, mail)
        mail_request = pack_mail(mail_pack)

        client = chat_setup()
        messages = compile_mail_request(mail_request)
        response = get_response(client, messages)

        save_response(response)

        logger.info("Email scraping application finished")
        return 0
    except Exception as e:
        logger.error(f"Application failed: {e}")
        return 1



if __name__ == "__main__":
    main()


