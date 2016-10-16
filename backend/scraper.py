import requests
from bs4 import BeautifulSoup
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


url = "http://gndec.ac.in"
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
news = soup.select("#block-block-15")[0].select(".content")[0].find_all("p")

fromaddr = "YOUR ADDRESS"
toaddr = "ADDRESS YOU WANT TO SEND TO"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE MAIL"
body = str(news)
msg.attach(MIMEText(body, 'plain'))


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "YOUR PASSWORD")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()