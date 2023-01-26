#!/usr/bin/env python3

import emails
import os
import reports
import getpass # Prompt the user for a password without echoing

attachment_path = input("\nPlease enter the attachment path (e.g. /path/to/attachment/report.pdf)\n")

table_data=[
  ['Name', 'Amount', 'Value'],
  ['elderberries', 10, 0.45],
  ['figs', 5, 3],
  ['apples', 4, 2.75],
  ['durians', 1, 25],
  ['bananas', 5, 1.99],
  ['cherries', 23, 5.80],
  ['grapes', 13, 2.48],
  ['kiwi', 4, 0.49]]

reports.generate( attachment_path, "A Complete Inventory of My Fruit", "This is all my fruit.", table_data)

# Gets the information needed to send the message
smtp_server = input("Please insert a SMTP Server. e.g.(smtp.gmail.com)\n")
# sender = "sender@example.com"
sender = input("Please enter a valid sender's email address!\n")
mail_pass = getpass.getpass("Please enter your password! (NB: in Gmail use App passwords)\n")
#receiver = "{}@example.com".format(os.environ.get('USER'))
receiver = input("Please enter a valid receiver's address!\n")

subject = "List of Fruits"
body = "Hi\n\nI'm sending an attachment with all my fruit."

message = emails.generate(sender, receiver, subject, body, attachment_path)
emails.send(smtp_server, sender, mail_pass, message)