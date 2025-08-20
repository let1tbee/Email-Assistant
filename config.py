"""
File to add configurations and variables
"""
import os
from dotenv import load_dotenv

load_dotenv()

GMAIL_EMAIL = os.getenv('GMAIL_EMAIL')
GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
IMAP_SERVER = os.getenv('IMAP_SERVER')
IMAP_PORT = int(os.getenv('IMAP_PORT'))

MAILBOX_SELECT = 'inbox'
MAILS_TO_SEARCH = 'UNSEEN'
MAILS_READABILITY = '(BODY.PEEK[])'
RESPONSE_FILE = 'output.txt'
AI_MODEL = "gpt-5-nano"
