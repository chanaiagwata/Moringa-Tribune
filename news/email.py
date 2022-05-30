from django.core.mail import EmailMultiAlternatives  #this mail module is responsible for sending emails************.
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):  #takes name and receiver*********
    # Creating message subject and sender
    subject = 'Welcome to the MoringaTribune NewsLetter'
    sender = 'james@moringaschool.com'

    #passing in the context vairables in the render to string functions 
    text_content = render_to_string('email/newsemail.txt',{"name": name})
    html_content = render_to_string('email/newsemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')  #We also attach the HTML template alternative for the times the User logs in to the email with basic html.
    msg.send()