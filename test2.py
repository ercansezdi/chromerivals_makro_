url = 'http://archive.nexts.live/' + "ChromeRivals_Setup.exe"
import requests


r = requests.head(url, allow_redirects=True)

print("---",r)

open('facebook.zip', 'wb').write(r.content)


"""

url = 'http://archive.nexts.live/' + "ChromeRivals_Makro.zip"
import requests


r = requests.get(url, allow_redirects=True)

print("---",r.text)

#open('facebook.zip', 'wb').write(r.content)


"""