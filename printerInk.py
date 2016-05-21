import urllib2, smtplib,

sender = 'johnapple@gmail.com'
receiver = ['applejohn@gmail.com']
url = "http://192.168.1.1/"
appCode = "xxxx xxxx xxxx xxxx"

message = """From: From Person <""" + sender + """>
To: To Person <""" + receiver[0] + """>
Subject: We need more ink for the printer

"""

addedMessage = "we need more "

colors = ["magenta", "cyan", "yellow", "black"]
colorsNeeded = []
amounts = []

inkNeeded = False

page = urllib2.urlopen(url)
for line in page:
		if "height" in line:
			pieces = line.split("height")
			amounts.append((pieces[1].split('"',1)[1]).split('"',1)[0])
			amounts.append((pieces[2].split('"',1)[1]).split('"',1)[0])
			amounts.append((pieces[3].split('"',1)[1]).split('"',1)[0])
			amounts.append((pieces[4].split('"',1)[1]).split('"',1)[0])

for thing in amounts:
	if int(thing) < 10:
		addedMessage += colors[amounts.index(thing)] + " ink its current level is " + thing + " out of approximily 50 \n"
		inkNeeded = True
		
if inkNeeded == True:
	print("trying host and port...")
	smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	smtpObj.login(sender, appCode)
	print("sending mail...")
	smtpObj.sendmail(sender, receiver, message + addedMessage)
	print("Email sent")
		
			