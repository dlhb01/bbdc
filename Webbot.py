from webbot import Browser
web = Browser()

f=open("../security/credentials.txt","r")
lines=f.readlines()
username=lines[0]
username=username[0:len(username)-1] #remove the enter char
password=lines[1]
f.close()
#print(username,password)

web.go_to('https://nussweb.org.sg/nussweb/main/loginuser.asp') 
web.click('txtMemberID')
web.type(username , tag='txtMemberID')
#web.click('NEXT' , tag='span')
web.type('password' , into='Password:') # specific selection
web.click('Submit' , tag='span') # you are logged in ^_^
print(web.get_current_url())
