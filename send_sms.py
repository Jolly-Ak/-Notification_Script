import csv 
import os
import base64

from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build



def get_mails():
    mails = []
    with open('recipient.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            mail = row['mail']
            mails.append(mail)
    return mails

print(get_mails())



# Scopes autorisés pour l'accès à Gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def se_connecter_gmail():
    """Se connecte à Gmail et renvoie un service Gmail """
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    service = build('gmail', 'v1', credentials=creds)
    return service

def envoyer_email(service, destinataire, sujet, corps):
    """ Envoie un e-mail à un destinataire 
     args :
        num1 (default) : le service Gmail
        num2 (str): l'adresse de l'utilisateur cible
        sujet (str): le sujet de l'e-mail
        corps (str): le contenu de l'e-mail
        """
    message = MIMEText(corps)
    message['to'] = destinataire
    message['subject'] = sujet
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    message = {
        'raw': raw
    }
    try:
        message = service.users().messages().send(userId="me", body=message).execute()
        print(f"E-mail envoyé avec l'ID : {message['id']}")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")


# import from info.json all recipients mail and send email


fdgh