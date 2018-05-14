import smtplib
import string
from django.template import loader
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_email_address = 'herramientasconectate@gmail.com'
from_email_password = 'conectate123'


def send_email_miembro(miembros_list, usuario_editor, herramienta):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email_address, from_email_password)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Nueva herramienta a la espera de ser revisada'
    msg['From'] = from_email_address

    for miembro in miembros_list:
        msg['To'] = miembro.email
        text = loader.render_to_string('HTMLEmails/notification_miembroGTI_text.html',
                                  {
                                        'user_name': miembro.username,
                                        'editors_name': usuario_editor,
                                        'herramienta':  herramienta
                                  }).encode('utf-8').strip()
        html = loader.render_to_string('HTMLEmails/notification_miembroGTI.html',
                                  {
                                        'user_name': miembro.username,
                                        'editors_name': usuario_editor,
                                        'herramienta':  herramienta
                                  }).encode('utf-8').strip()

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        msg.attach(part1)
        msg.attach(part2)

        server.sendmail(from_email_address, [miembro.email], msg.as_string())

    server.quit()
