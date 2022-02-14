from random import randint
import time
from requests_html import HTMLSession

session = HTMLSession()
usersfound = set(())
specildeal = "https://scratch.mit.edu/explore/studios/all/"
filef = open("users.txt", "r")
filecontent = filef.read()
currentpage = session.get('http://scratch.mit.edu')

if len(filef.readlines()) > 100000:
    raise Exception("File too large to edit safely")
def loadpage():
    print(currentpage.url)
    try:
        currentpage.html.render()
    except:
        print("page render failed")
    links = currentpage.html.absolute_links

    for link in links:
        if "://scratch.mit.edu/users/" in link and not "/studios/" in link and not "/studios" in link and not "/favorites/" in link and not "/followers/" in link and not "/following/" in link and not "/projects/" in link and not "#comm" in link and not link in filecontent:
            usersfound.add(link)
    print("progressing")
    filex = open("users.txt", "r")
    filecont = filex.read()
    filex.close()
    filexr = open("users.txt", "w")

    for link in usersfound:
        if not link in filecont and not link + "/" in filecont and not link in filecont:
            filexr.append(link + "\n")
    
    usersfound.clear()
    filexr.close()
    return usersfound


filex = open("users.txt", "r")

loadpage()

filex.close()

currentpage = session.get('https://scratch.mit.edu/explore')

loadpage()

currentpage = session.get(specildeal)

loadpage()

filex = open("users.txt", "r")
flex = filex.readlines()
filex.close()
for i in range(1,30):
    specildeal = flex[len(flex) - randint(5, 1000)]
    specildeal = specildeal.replace("\n", "")
    specildeal = f'https://scratch.mit.edu/users/{specildeal}' 
    currentpage = session.get(specildeal)

    loadpage()
    time.sleep(0.5)
    if specildeal[len(specildeal) - 1] == "/":
        currentpage = session.get(specildeal + 'followers/')
    else:
        currentpage = session.get(specildeal + '/followers/')
    loadpage()

    if specildeal[len(specildeal) - 1] == "/":
        currentpage = session.get(specildeal + 'following/')
    else:
        currentpage = session.get(specildeal + '/following/')
    loadpage()
    time.sleep(1)
