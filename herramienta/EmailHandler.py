import sendgrid
import os
from sendgrid.helpers.mail import *

from_email_address = 'app91642978@heroku.com'
from_email_password = 'ddz0wkcz3463'
sg_key = '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'


def send_email (to_email_address, subject, body):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get(sg_key))
    from_email = Email(from_email_address)
    to_email = Email(to_email_address)

    content = Content("text/plain", body)
    final_mail = Mail(from_email, subject, to_email, content)

    response = sg.client.mail.send.post(request_body=final_mail.get())

    print(response.status_code)
    print(response.body)
    print(response.headers)
