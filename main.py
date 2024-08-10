from send_sms import *



if __name__ == '__main__':

    """ Envoie un mail a tout les destinataires """
    service = se_connecter_gmail()
    emails = get_mails()
    sujet = "Test de l'envoi d'e-mail via API Gmail"
    corps = "Ceci est un e-mail envoyé via l'API Gmail avec OAuth 2.0."

    for destinataire in emails:
        envoyer_email(service, destinataire, sujet, corps)
