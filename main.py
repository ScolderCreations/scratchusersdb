from random import randint

from requests_html import HTMLSession

session = HTMLSession()
usersfound = set(())
specildeal = "https://scratch.mit.edu/explore/studios/all/"
filef = open("users.txt", "r")
filecontent = filef.read()
currentpage = session.get('http://scratch.mit.edu')


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
    filex = open("users.txt", "a")

    for link in usersfound:
        if not link in filecont:
            filex.write(link + "\n")
            usersfound.remove(link)

    filex.close()
    return usersfound


filex = open("users.txt", "r")

loadpage()

filex.close()

currentpage = session.get('https://scratch.mit.edu/explore')

loadpage()

currentpage = session.get(specildeal)

loadpage()

filex = open("users.txt", "r")

specildeal = filex.readlines()[len(filex.readlines()) - randint(1, 200)]
specildeal = specildeal.replace("\n", "")

currentpage = session.get(specildeal)

loadpage()

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
