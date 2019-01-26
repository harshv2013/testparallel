import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "vardhan@paralleldots.com"
you = "harsh2013@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Subject of this mail is Cool ! "
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
#text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
name = 'Harsh'

html = """Hi """+name+""",
            <br>
            Congratulations!
            <br> 
            Your SmartReader project has been trained. Our Customer Success team is now working to set up the classifier for you. 
            <br>
            Please book a slot below(or from your dashboard) to discuss the results and the interesting insights that we have discovered from your data.
            
            <br>  
            Here is the link to join with us:  <a href=" https://calendly.com/akriti-1/15min">link</a>   
            <br>
                
            Meanwhile, if you have any questions, please do not hesitate to contact us. We'll be right here."""

# Record the MIME types of both parts - text/plain and text/html.
#part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
#msg.attach(part1)
msg.attach(part2)
# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('vardhan@paralleldots.com', 'sudhansu')
mail.sendmail(me, you, msg.as_string())
mail.quit()
