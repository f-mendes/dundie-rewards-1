import re
import smtplib
from email.mime.text import MIMEText

from dundie.utils.log import get_logger
from dundie.utils.settings import SMTP_HOST, SMTP_PORT, SMTP_TIMEOUT

log = get_logger()


# this is regex validate email address
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


def check_valid_email(email):
    """ "Return True if email is valid"""
    return EMAIL_REGEX.match(email) is not None


def send_email(from_, to, subject, text):
    """Send email"""
    if not isinstance(to, list):
        to = [to]

    try:
        with smtplib.SMTP(
            host=SMTP_HOST, port=SMTP_PORT, timeout=SMTP_TIMEOUT
        ) as smtp:
            message = MIMEText(text)
            message["Subject"] = subject
            message["From"] = from_
            message["To"] = ", ".join(to)
            smtp.sendmail(from_, to, message.as_string())
    except Exception:
        log.error("Cannot send email %s", to)
