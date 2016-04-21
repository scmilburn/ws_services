import smtplib


fromaddr = 'winterfell.services@gmail.com'
toaddrs  = '@gmail.com'
msg = 'HERE IS THE MESSAGE'

username = 'winterfell.services@gmail.com'
password = 'CHUM_4801w'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
