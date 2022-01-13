url = 'http://archive.nexts.live/version/' + "version_v04" + ".zip"
import requests


r = requests.head(url, allow_redirects=True)

if str(r) == "<Response [200]>":
    print("Dosya Var")
else:
    print("Dosya yok")

open('facebook.zip', 'wb').write(r.content)


"""

url = 'http://archive.nexts.live/' + "ChromeRivals_Makro.zip"
import requests


r = requests.get(url, allow_redirects=True)

print("---",r.text)

#open('facebook.zip', 'wb').write(r.content)


"""