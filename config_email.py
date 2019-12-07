import smtplib, ssl


def send_email_to_user(receiver_email, books):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "<your_email>"
    password = "<your_password>"
    message = """\
    Subject: Hi there,\n
    \n
    I want to exchange those books: """ + books

    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

