import os
import smtplib
import ssl
import smtplib
from email.message  import EmailMessage

email_sender = 'matrix.team.mu@gmail.com'
email_password = "jojjbjqxmweznouj"
email_reciver = ["semohamedali1@gmail.com"
,"ak3808468@gmail.com"
,"elsaedelsobky56@gmail.com"
,"redam1077@gmail.com"
,"ea6156637@gmail.com "
,"rodykhaled2222008@gmail.com"
,"yasseralaa041@gmail.com"
,"salmat935@gmail.com"
]

subject = 'MATRIX Team Recruitment | Regretful Decision - Next Opportunities Await'
body = """

Dear Applicant,

I regret to inform you that your application has been unsuccessful following Round 2. 
We appreciate the time and effort you invested in the selection process, and while your qualifications and skills are commendable, we have made the difficult decision to pursue other candidates who align more closely with our current needs.

We sincerely appreciate your interest in joining our team, and we hope to have the opportunity to cross paths again in the future. 
Thank you for your understanding, and we wish you the very best in your future endeavors.



best wishes
Team MATRIX
"""
em = EmailMessage()
em ['From'] = email_sender
em ['To'] = email_reciver
em['Subject'] = subject
em.set_content(body)

context =ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender , email_reciver , em.as_string())
    print("Emails Sent sucessfully")