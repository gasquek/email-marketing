# Simple script used to send an HTML file as an HTML formatted email,
# using Gmail's SMTP service. Used for testing HTML emails.
# The core message-sending code is taken from the docs:
# http://docs.python.org/2/library/email-examples.html
# The code for correctly authenticating against Gmail comes from:
# http://kutuma.blogspot.co.uk/2007/08/sending-emails-via-gmail-with-python.html
import smtplib
import argparse
from getpass import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def parse_args():
    """
    Parse script input arguments.

    Returns the parsed args, having validated that the input
    file can be read, and that there is a valid Username.
    """
    parser = get_parser()
    args = parser.parse_args()

    # artificially adding this to args, so that
    # it can be passed around easily
    args.html = open(args.html_filename).read()

    # we have to have a valid Gmail account in order to access the SMTP service
    if args.username is None:
        args.username = "admin@gasquen.se"
    print_args(args)
    return args

def get_parser():
    """ Return the parser used to interpret the script arguments."""
    usage = (
        "Script to send an HTML file as an HTML email, using Google's SMTP server."
        "\nExamples:"
        "\n1. Send the contents of test_file.html to fred"
        "\n$ send_html_email.py fred@example.com test_file.html"
        "\n"
        "\n2. Send the mail to both fred and bob"
        "\n$ send_html_email.py fred@example.com bob@example.com test_file.html"
        "\n"
        "\n3. Use fred123@gmail.com as the Gmail authenticating account"
        "\n$ send_html_email.py fred@example.com test_file.html -u fred123@gmail.com"
        "\n"
        "\n4. Override the default test mail subject line"
        "\n$ send_html_email.py fred@example.com test_file.html -t 'Test email'"
        "\n"
        "\n5. Turn on SMTP debugging"
        "\n$ send_html_email.py fred@example.com test_file.html -d"
    )
    epilog = "NB This script requires a Gmail account."

    parser = argparse.ArgumentParser(description=usage, epilog=epilog,
        # maintains raw formatting, instead of wrapping lines automatically
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('recipients', help='The recipient email addresses (space delimited)', nargs='+')
    parser.add_argument('html_filename', help='The HTML file to use as the email body content')
    parser.add_argument('-s', '--sender',
        help='The sender email address (defaults to <do-not-reply@example.com>)',
        default='info@gasquen.se'
    )
    parser.add_argument('-u', '--username',
        help=('A valid Gmail user account (used to authenticate against Google\'s SMTP service). '
            'If this argument is not supplied, the user will be prompted to type it in.')
    )
    parser.add_argument('-t', '--title',
        help='The test email subject line (defaults to "Test email")',
        default="Test email"
    )
    parser.add_argument('-p', '--plain',
        help=('The test email plain text content. This script is designed primarily for the '
            'testing of HTML emails, so this text is really just a placeholder, for completeness. '
            'The default is "This is a test email (plain text)."'),
        default="This is a test email (plain text)"
    )
    parser.add_argument('-d', '--debug', action='store_true',
        help=('Use this option to turn on DEBUG for the SMTP server interaction.')
    )
    return parser


def print_args(args):
    """Print out the input arguments."""
    print ('Sending test email to: %s' % args.recipients)
    print ('(Sending test email from: %s' % args.sender)
    print ('Using Gmail account: %s' % args.username)


def create_message(args):
    """ Create the email message container from the input args."""
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = args.title
    msg['From'] = "Era babes i GK <info@gasquen.se>"
    msg['To'] = ','.join(args.recipients)

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(args.plain, 'plain')
    part2 = MIMEText(args.html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    return msg


def main():

    args = parse_args()
    msg = create_message(args)

    try:
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.set_debuglevel(args.debug)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        # getpass() prompts the user for their password (so it never appears in plain text)
        smtpserver.login(args.username, getpass())
        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        smtpserver.sendmail("<info@gasquen.se>", args.recipients, msg.as_string())
        print ("Message sent to '%s'." % args.recipients)
        smtpserver.quit()
    except smtplib.SMTPAuthenticationError as e:
        print ("Unable to send message: %s" % e)

if __name__ == "__main__":
    main()