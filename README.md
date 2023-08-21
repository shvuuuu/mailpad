<p align="center">
  <a href="https://mailpad.tech/">
    <img src="https://i0.wp.com/mailpad.tech/wp-content/uploads/2023/08/mailpad-tech-logo.png?w=837&ssl=1" alt="Mailpad" />
  </a>
</p>
<p align="center">
  <h1 align="center">MailPad Python Library</h1>
  <p align="center">
    MailPad is a Python library that simplifies email sending and integrates with language models for generating email content. Utilizing OpenAI's language models to generate text emails.
    <br />
    <a href="https://twitter.com/shvuuuu">
      <img src="https://img.shields.io/twitter/follow/shvuuuu?style=social" />
    </a>
    <a href="https://pypi.org/project/mailpad/">
      <img src="https://img.shields.io/badge/pypi-3775A9?style=for-the-badge&logo=pypi&logoColor=white">
    </a>
    <a href="https://reddit.com/r/getumbrel">
      <img src="https://img.shields.io/linkedin/shvuuuu?style=social">
    </a>
  </p>
</p>


# MailPad Python Library

MailPad is a Python library that simplifies email sending and integrates with language models for generating email content. Utilizing OpenAI's language models to generate text emails.

## Installation

MailPad can be installed using pip:

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
mail.openai(temperature,model)

form_input = "EMAIL_MESSAGE/EMAIL_CONTEXT"
email_sender = "SENDER_NAME"
email_recipient = "RECIPIENT_NAME"
email_style = "EMAIL_STYLE"

response = mail.get_llm_response(form_input, email_sender, email_recipient, email_style)
print(response)
```

## Features
* Send plain text emails or emails with attachments
* Brevo Integration
* Supports OpenAI's language models

## Contributing
Contributions are welcome! If you have suggestions, bug reports, or would like to add new features, feel free to create issues or pull requests on the GitHub repository.

## License
This project is licensed under the MIT License.
