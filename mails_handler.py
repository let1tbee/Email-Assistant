import imaplib
import email
from email import policy
from config import IMAP_SERVER, IMAP_PORT, GMAIL_EMAIL, GMAIL_PASSWORD, MAILBOX_SELECT, MAILS_TO_SEARCH, MAILS_READABILITY
from logger import get_logger

logger = get_logger(__name__)

def mail_setup() -> tuple[list[bytes], imaplib.IMAP4_SSL]:
    """
    Function setups email connection and retrieves email ids

    Returns:
        data: list of email ids
        mail: email connection

    """
    logger.info("Connecting to email server...")
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER,IMAP_PORT)
        mail.login(GMAIL_EMAIL, GMAIL_PASSWORD)
        mail.select(MAILBOX_SELECT)

        status, data = mail.search(None, MAILS_TO_SEARCH)
        return data[0].split(), mail

    except Exception as e:
        logger.error(f"Error while connecting to email server: {e}")
        raise


def compile_email(mail_ids: list, mail: imaplib.IMAP4_SSL)-> list[list[dict[str, str]]]:
    """
    Function goes through mail ids and retrieves email contents

    Args:
        mail_ids: list of email ids
        mail: email connection

    Returns:
        mail_pack: list of email contents

    """
    logger.info("Compiling emails...")
    mail_pack = []
    try:
        for id in mail_ids:
            single_mail =[]
            status, msg_data = mail.fetch(id, MAILS_READABILITY)
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email, policy=policy.default)
            single_mail.append({'Subject' : msg['Subject']})

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == 'text/plain':
                        body = part.get_payload(decode=True).decode()
                        clean_body = body.replace("\r\n", "\n").strip()
                        single_mail.append({'Body': clean_body})
            else:
                body = msg.get_payload(decode=True).decode()
                clean_body = body.replace("\r\n", "\n").strip()
                single_mail.append({'Body': clean_body})
            mail_pack.append(single_mail)
    except Exception as e:
        logger.error(f"Error while reading emails: {e}")
        raise
    return mail_pack

def pack_mail(mail_pack: list[list[dict[str,str]]]) -> str:
    """
    Function creates a body for AI request.

    Args:
        mail_pack: list of email contents

    Returns:
        mail_request: body for AI request
    """
    mail_request = "\n\n"
    logger.info("Packing emails...")
    if len(mail_pack) < 5:
        for i in range(len(mail_pack)):
            mail_request += f"""
        Лист {i+1}:
        ---
        Тема: {mail_pack[i][0]['Subject']}
        Текст: {mail_pack[i][1]['Body']}
        ---
        """
    else:
        raise Exception("Too many emails to analyze, please change model or purchase a Pro plan.")
    return mail_request