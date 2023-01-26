#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib


def generate(sender, recipient, subject, body, attachment_path):
  """Creates an email with an attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  # Process the attachment and add it to the email
  attachment_filename = os.path.basename(attachment_path)
  mime_type, _ = mimetypes.guess_type(attachment_path)
  mime_type, mime_subtype = mime_type.split('/', 1)

  with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                          maintype=mime_type,
                          subtype=mime_subtype,
                          filename=attachment_filename)

  return message

def send(smtp_server, sender, sender_pass, message):
  """Sends the message to the configured SMTP server."""
#  mail_server = smtplib.SMTP('localhost')
  mail_server = smtplib.SMTP_SSL(smtp_server) # Connect to SMTP Server
  mail_server.set_debuglevel(1) # FIXME: Activate Debug Mode in Object (Only for Testing purpouses!)

  mail_server.login(sender, sender_pass)
  mail_server.send_message(message)
  mail_server.quit()