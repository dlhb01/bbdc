from webbot import Browser
import time
web = Browser()

f=open("../security/credentials.txt","r")
lines=f.readlines()
username=lines[0]
username=username[0:len(username)-1] #remove the enter char
password=lines[1]
f.close()
#print(username,password)

web.go_to('https://nussweb.org.sg/nussweb/main/loginuser.asp')
web.type(username, id='txtMemberID',loose_match=True)
web.type(password, id='password',loose_match=True,number=2)
web.click('Submit' , tag='span') # you are logged in ^_^
print(web.get_current_url())

web.click('Booking')
web.go_to('https://nussweb.org.sg/nussweb/facility/schedule.asp?d=1-4-19&catid=TFC&colorcode=FFCE63&Bookcatname=T%20R%20U%20E%20Fitness')


