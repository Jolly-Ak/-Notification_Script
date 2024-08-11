from send_sms import *



if __name__ == '__main__':

    """ Envoie un mail a tout les destinataires """
    service = se_connecter_gmail()
    emails = get_mails()
    sujet = "Test de l'envoi d'e-mail via API Gmail"
    corps = "Ceci est un e-mail envoyé via l'API Gmail avec OAuth 2.0."

    for destinataire in emails:
        #ask for     inpute 
        sujet = input("subject of the mail")
        corps = input("body of the mail")


        envoyer_email(service, destinataire, sujet, corps)
dsd