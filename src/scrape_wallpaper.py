import requests
from bs4 import BeautifulSoup
from pprint import pprint
import shutil
import os


def fetchLinks(keyword):
    url = "https://old.reddit.com/r/Amoledbackgrounds/search/?q=" + \
        keyword + "&include_over_18=on&restrict_sr=on&t=all&sort=top"
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)

    print(page.status_code)
    content = page.content

    soup = BeautifulSoup(content, features="lxml")
    image_a = soup.find_all("a", "search-link")
    image_links = []
    for a in image_a:
        image_links.append(a.attrs['href'])
    return image_links


def download_images(image_links, keyword):
    if image_links == []:
        pprint("ERROR: Could not find *any* image links!")
        return -1

    try:
        os.mkdir(keyword)
    except FileExistsError:
        pass

    print("Downloading images...")
    n = len(image_links)
    for i, link in enumerate(image_links):
        print(str(i+1)+" of "+str(n)+"...")
        r = requests.get(link, stream=True)

        if r.status_code == 200:
            r.raw.decode_content = True

            filename = link.split("/")[-1]
            with open(os.path.join(keyword, filename), 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            print("Could not find image at " + link)

    print("Completed! (⌐■_■)")
    return 0


if __name__ == "__main__":
    keyword = input("Enter search query: ")
    image_links = fetchLinks(keyword)
    download_images(image_links, keyword)

    print("\n\n--------------------------------------------A program by Harshit Garg (hg1229@gmail.com)")
