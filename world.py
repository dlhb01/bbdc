import requests
from lxml import html

USERNAME = "<USERNAME>"
PASSWORD = "<PASSWORD>"

LOGIN_URL = "http://www.bbdc.sg/bbweb/default.aspx"
URL = "http://www.bbdc.sg/bbdc/b-selectCourse.asp"

def main():

    session_requests = requests.session()
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    #print (headers)
    # Get login csrf token
    result = session_requests.get(LOGIN_URL,headers=headers)
    tree = html.fromstring(result.text)
    #print(result.text)
    #authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    # Create payload
    payload = {
        "txtNRIC": USERNAME, 
        "txtPassword": PASSWORD, 
     #   "csrfmiddlewaretoken": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    print(result.text)
    bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    print(bucket_names)

if __name__ == '__main__':
    main()
