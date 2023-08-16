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
mail.send_mail (from_email, to_email, subject, message)
```

Brevo Integration
Login as - https://www.brevo.com/

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
mail.send_mail (from_email, to_email, subject, message)
```
