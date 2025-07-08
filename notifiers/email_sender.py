import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, content, to_email, from_email, smtp_server, smtp_port, username, password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(content, 'plain'))

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(username, password)
            server.sendmail(from_email, to_email, msg.as_string())
        print("✅ 邮件发送成功")
    except Exception as e:
        print("❌ 邮件发送失败：", e)
