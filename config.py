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
AIROLE = "You are assistant for email analysis"
AIPROMPT = """
    Carefully analyze the following emails. 
    Summarize the key points clearly and concisely. 
    Then, based on the email contents, generate a prioritized list of actionable straightforward tasks I should perform. 
    Format your answer in two separate sections titled 'Main Points from Emails' and 'Action Items', using bullet points and short sentences for clarity. 
    Provide answer in English."""
