import smtplib
import json 
import urllib2

def email(recipients, msg):
    username = 'winterfell.services@gmail.com'
    password = 'CHUM_4801w'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(username, recipients, msg)
    server.quit()

def groupme(msg):
    data = {"bot_id": "cb54c0cc4cf14a04ef6737e67d", "text": msg}    
    url = 'https://api.groupme.com/v3/bots/post'
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')

    response = urllib2.urlopen(req, json.dumps(data))


