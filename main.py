import boto3
import logging
from botocore.exceptions import WaiterError, ClientError

from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION
from ses_identity import SesIdentity
from ses_template import SesTemplate
from message_queue import MessageQueue
from email_template import EMAIL_SUBJECT, EMAIL_BODY_TEXT, EMAIL_BODY_HTML

def usage_demo():
    print("-" * 88)
    print("Welcome to the Amazon Simple Email Service (Amazon SES) email demo!")
    print("-" * 88)

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    ses_client = boto3.client(
        "ses",
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    ses_identity = SesIdentity(ses_client)
    ses_template = SesTemplate(ses_client)
    message_queue = MessageQueue(ses_client)

    email_server = "ntutlab321projects@gmail.com"
    
    # 收集多個收件人地址 recipients之後可以針對後端監測的帳戶 進行json訊息傳遞過來 並針對json資訊進行動作
    recipients = []
    while True:
        email = input("Enter an email address to receive mail (or press Enter to finish): ")
        if email == "":
            break
        status = ses_identity.get_identity_status(email)
        if status != "Success":
            print(f"Warning: The address '{email}' is not verified with Amazon SES.")
            verify = input("Do you want to verify this email? (y/n): ")
            if verify.lower() == 'y':
                ses_identity.verify_email_identity(email)
                print(f"Verification email sent to {email}. Please check the inbox and complete verification.")
            else:
                print(f"Skipping {email} as it's not verified.")
                continue
        recipients.append(email)

    recipients = list(set(recipients))
    if not recipients:
        print("No valid recipients. Exiting.")
        return

    message_queue.start_processing()


    # 發送普通郵件
    # 郵件資訊定義
    test_message_text = "Hello from the Amazon SES mail demo!"
    test_message_html = "<p>Hello!</p><p>From the <b>Amazon SES</b> mail demo!</p>"



    print(f"Sending mail from {email_server} to {', '.join(recipients)}.")
    message_queue.add_message(
        email_server,
        recipients,
        "Amazon SES demo",
        test_message_text,
        test_message_html
    )

    template = {
        "name": "doc-example-template",
        "subject": "Example of an email template.",
        "text": "This is what you will {{action}} .",
        "html": "<p><i>This</i> is what {{name}} will {{action}} if {{name}} <b>can</b> display HTML.</p>",
    }

    print("Creating a template and sending a templated email.")
    ses_template.create_template(**template)
    
    for recipient in recipients:
       template_data = {"name": recipient.split("@")[0], "action": "read"}
       user_name = recipient.split("@")[0]
       personalized_text = EMAIL_BODY_TEXT.format(name=user_name)
       personalized_html = EMAIL_BODY_HTML.format(name=user_name)

       if ses_template.verify_tags(template_data):  
            message_queue.add_message_with_attachment(
            email_server,
            [recipient],
            "Amazon SES demo (Combined)",
            personalized_text,
            personalized_html,
            "Image.png"
        )

    # 等待所有郵件發送完成
    message_queue.wait_for_completion()
    message_queue.stop_processing()

    print("All emails have been sent. Check your inboxes!")

    if ses_template.template is not None:
        try:
            print("Deleting demo template.")
            ses_template.delete_template()
        except ClientError as e:
            print(f"Error deleting template: {e}")

    print("Thanks for watching!")
    print("-" * 88)

if __name__ == "__main__":
     usage_demo()

