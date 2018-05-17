import smtplib
from django.template import loader
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_email_address = 'herramientasconectate@gmail.com'
from_email_password = 'conectate123'


def send_email_miembro(miembros_list, usuario_editor, herramienta):
    subject = 'Nueva herramienta a la espera de ser revisada'
    html_template = 'HTMLEmails/notification_miembroGTI.html'
    text_template = 'HTMLEmails/notification_miembroGTI_text.html'

    send_email_to_users(miembros_list, usuario_editor, herramienta, subject, html_template, text_template)

def send_email_to_publish_tool (admin_list, owner, herramienta):
    subject = 'Una herramienta ha sido marcada como lista para ser publicada'
    html_template = 'HTMLEmails/notificacion_Herramienta_por_publicar.html'
    text_template = 'HTMLEmails/notificacion_Herramienta_por_publicar_text.html'

    send_email_to_users(admin_list, owner, herramienta, subject, html_template, text_template)

def send_email_to_users(user_list, posting_user, herramienta, subject, html_template, text_template):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email_address, from_email_password)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_email_address

    for user in user_list:
        msg['To'] = user.email
        text = loader.render_to_string(text_template,
                                  {
                                        'user_name': user.first_name,
                                        'editors_name': posting_user,
                                        'herramienta':  herramienta
                                  }).encode('utf-8').strip()
        html = loader.render_to_string(html_template,
                                  {
                                        'user_name': user.first_name,
                                        'editors_name': posting_user,
                                        'herramienta':  herramienta
                                  }).encode('utf-8').strip()

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        msg.attach(part1)
        msg.attach(part2)

        server.sendmail(from_email_address, [user.email], msg.as_string())

    server.quit()