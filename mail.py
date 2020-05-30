import smtplib
receiver = "vmsingare11@gmail.com"
sender = "vimsingare11@gmail.com"
text = "Hello Developer, your model achieved more than 96% accuracy and is ready to use for predictions!!!" 
pass = "" #password for sender's mail address
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(sender,pass)
print("Access Granted")
server.sendmail(sender,reciever,text)
print("Mail sent!!")
