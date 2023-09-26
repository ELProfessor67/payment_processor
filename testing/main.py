import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("zafraan999@gmail.com","tjueghjkrdergqfl")
message = "Message_you_need_to_send"
s.sendmail("zafraan999@gmail.com", 'jeeshanr599@gmail.com', 'hello from me')
s.quit()