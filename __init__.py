from src.scrape_wallpaper import fetchLinks, download_images

if __name__ == "__main__":
    keyword = input("Enter search query: ")
    image_links = fetchLinks(keyword)
    download_images(image_links, keyword)

    print("\n\n--------------------------------------------A program by Harshit Garg (hg1229@gmail.com)")
