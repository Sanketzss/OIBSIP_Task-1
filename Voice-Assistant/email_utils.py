import os.path
import base64
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Path to your new service account credentials JSON file
SERVICE_ACCOUNT_FILE = r"C:\Users\SANKET PRASAD\Downloads\peak-radius-433513-s4-24392374ebcd.json"

# Define the scope
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_gmail_service():
    """Create a service object for interacting with the Gmail API."""
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('gmail', 'v1', credentials=creds)
    return service

def create_message(to, subject, body):
    """Create a message to send."""
    message = MIMEMultipart()
    message['to'] = to
    message['subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

def send_email(to_email, subject, message_text):
    """Send an email using the Gmail API."""
    service = get_gmail_service()
    message = create_message(to_email, subject, message_text)
    try:
        send_message = service.users().messages().send(userId='me', body=message).execute()
        print(f'Sent message to {to_email} Message Id: {send_message["id"]}')
    except HttpError as error:
        print(f'An error occurred: {error}')
