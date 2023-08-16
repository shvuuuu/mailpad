# MailPad Python Library

MailPad is a Python library that simplifies email sending and integrates with language models for generating email content. Utilizing OpenAI's language models to generate text emails.

## Installation

You can install MailPad using pip:

```python
pip install mailpad
```
## Sending Email

```python
from mailpad import mailpad
import os

mail = mailpad('smtp-server','smtp-port')

os.environ["MAILPAD_EMAIL"] = "YOUR_EMAIL"
os.environ["MAILPAD_PASSWORD"] = "YOUR_PASSWORD"

from_email = "your_email@exphample.com"
to_email = ["her_email@example.com"]
subject = "Subject"
message = """Message Content"""
mail.send_mail(from_email, to_email, subject, message)
```

## Sending Email With Attachments

```python
from mailpad import mailpad
import os

mail = mailpad('smtp-server','smtp-port')

os.environ["MAILPAD_EMAIL"] = "YOUR_EMAIL"
os.environ["MAILPAD_PASSWORD"] = "YOUR_PASSWORD"

from_email = "your_email@exphample.com"
to_email = ["her_email@example.com"]
subject = "Subject"
message = """Message Content"""
attachment = "/Users/Docs/Letter.pdf"
mail.send_mail_with_attachmnet(from_email, to_email, subject, message,attachment)
```

## Brevo Integration
Create account at: https://www.brevo.com/

```python
from mailpad import mailpad
import os

#Using Brevo Servers
mail=mailpad()
mail.brevo()

os.environ["MAILPAD_EMAIL"] = "YOUR_EMAIL"
os.environ["MAILPAD_PASSWORD"] = "YOUR_PASSWORD"

from_email = "your_email@exphample.com"
to_email = ["her_email@example.com"]
subject = "Subject"
message = """Message Content"""
mail.send_mail(from_email, to_email, subject, message)
```

## Generating Emails With OpenAi

```python
from mailpad import mailpadAI
import os
import openai

os.environ["OPENAI_API_KEY"]="YOUR_OPENAI_KEY"

mail = mailpadAI()
mail.openai()

form_input = "EMAIL_MESSAGE/EMAIL_CONTEXT"
email_sender = "SENDER_NAME"
email_recipient = "RECIPIENT_NAME"
email_style = "EMAIL_STYLE"

response = mail.get_llm_response(form_input, email_sender, email_recipient, email_style)
print(response)
```
