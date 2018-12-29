import requests
import time
from lxml import html

f=open("../security/credentials.txt","r")
lines=f.readlines()
username=lines[0]
username=username[0:len(username)-1] #remove the enter char
password=lines[1]
f.close()


LOGIN_URL = "https://nussweb.org.sg/nussweb/main/loginuser.asp"
URL = "https://nussweb.org.sg/nussweb/main/main.asp"

def main():

    s = requests.Session()
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    print (headers)
    # Get login csrf token
    #result = s.get(LOGIN_URL,headers=headers)
    #tree = html.fromstring(result.text)
    #print(result.text)
    #authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    # Create payload
    #payload = {
    #    "txtMemberID": username, 
    #    "txtPassword": password, 
    #   "csrfmiddlewaretoken": authenticity_token
    #}

    # Perform login
    result=s.post(LOGIN_URL, data = dict(txtMemberID=username,txtPassword=password))
    print(result.cookies.get_dict())
    print(result.text)
    time.sleep(5)
    result = s.get(URL)
    print(result.text)

    # Scrape url
    #result = s.get(URL, headers = dict(referer = URL))
    #tree = html.fromstring(result.content)
    #print(result.text)
    #bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    #print(bucket_names)

if __name__ == '__main__':
    main()
