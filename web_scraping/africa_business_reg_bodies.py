from bs4 import BeautifulSoup

with open("List of official business registers - Wikipedia.html", "r") as f:
    content = f.read()

    soup = BeautifulSoup(content, "lxml")
    bodies = soup.find_all("li")

    for body in bodies:
        if not "Retrieved" in body.text:
            if "[" in body.text:
                print(body.text)
