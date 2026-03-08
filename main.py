# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def hi():
    # Use a breakpoint in the code line below to debug your script.
    """
    import random
    import requests


    res = requests.get('https://www.geeksforgeeks.org/python/python-programming-language-tutorial/')
    print(res.status_code)

    #print(res.content)  # Press ⌘F8 to toggle the breakpoint.
    content = res.content
    listOfWords = content.split()
    print(random.choice(listOfWords))
"""

    import random
    import requests
    from bs4 import BeautifulSoup

    ###############################
    #listOfLinks = ["https://mayahawk14.github.io/portfolio/", "https://uroulette.com/visit/wnnvv", "https://uroulette.com/visit/wrrwo"]

    h = requests.get("https://uroulette.com/")
    soup = BeautifulSoup(h.content, 'html.parser')


    content = soup.find('a', href=True)

    # Extracting all the <a> tags into a list.
    tags = soup.find("tr", {"valign": "top"}).find_all("a")

    # Extracting URLs from the attribute href in the <a> tags.
    for tag in tags:
        tag.get('href')


    goodlink = tag.get('href')

    try:
        while True:
            while True:
                link = "https://uroulette.com" + goodlink
                res = requests.get(link)
                if res.status_code == 200:
                    break
                else:
                    continue

            soup = BeautifulSoup(res.content, 'html.parser')

            content = soup.prettify()
            listOfWords = content.split()
            word = random.choice(listOfWords)

            special_characters = "!@#$%^&*(){}-+?_=,<>/:."

            # Check if any element in the list is a substring of the main string
            if any(substring in word for substring in special_characters):
                #print("One or more elements were found in the string: " + word)
                continue
            else:
                #print("No elements were found.")
                break
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    title = soup.title.string

    #print("Title: " + title + "\n")
    print(word)
    # Find the main content container

    #webbrowser.open(choice(random_page_generator), new=2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hi()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
