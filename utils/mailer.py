import smtplib


def mailer(to,text):
	try:
		# print(to,text)
		# s = smtplib.SMTP('smtp.gmail.com', 587)
		# s.starttls()
		# s.login("zafraan999@gmail.com","tjueghjkrdergqfl")
		# s.sendmail("zafraan999@gmail.com", to, text)
		# s.quit()
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login("zafraan999@gmail.com","tjueghjkrdergqfl")
		message = "Message_you_need_to_send"
		s.sendmail("zafraan999@gmail.com", 'jeeshanr599@gmail.com', 'hello from me')
		s.quit()
	except Exception as e:
		# print(e)
		return "send failed"
	s.quit()
	return "send succesfully"