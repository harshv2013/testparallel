
import smtplib




server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("vardhan@paralleldots.com", "sudhansu")


msg=" bla bla bla bla bla"

server.sendmail("vardhan@paralleldots.com", "harsh2013@gmail.com", msg)
server.quit()

# print(type(msgdg))
