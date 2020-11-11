import sendgrid
from emotorad.settings import SENDGRID_API_KEY


def send_mail(reciever_email, subject, email_template, attachments=None):
    sendgrid_object = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)

    to = []
    if isinstance(reciever_email, list):
        for email in reciever_email:
            to.append({
                "email": email
            })
    else:
        to.append({
            "email": reciever_email
        })

    data = {
        "personalizations": [
            {
                "to": to,
                "subject": subject
            }
        ],
        "from": {
            "email": "info@emotorad.com",
            "name": "Emotorad"
        },
        "content": [
            {
                "type": "text/html",
                "value": email_template
            }
        ]
    }

    if attachments:
        data["attachments"] = attachments

    sendgrid_object.client.mail.send.post(request_body=data)
