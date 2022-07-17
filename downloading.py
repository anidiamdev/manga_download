import requests
import os

from requests.exceptions import Timeout
from bs4 import BeautifulSoup as bs
from re import sub


# DOES ALL THE LOGIC SO WE ONLY IMPORT THIS ON THE MAIN
def do_download_logic(data):

    data["links_to_images"] = return_links_to_images(data)
    download_chapters(data)


# THIS WILL RETURN ALL THE IMAGES LINKS FOR EVERY SUGGESTED CHAPTER
def return_links_to_images(data):

    # actually loving dictionaries lol
    manga_title = data["manga_title"]
    chapters = data["chapters"]

    # {"chapter x": <list-with-images-links>}
    links_to_images = {}

    print("===== GETTING THE CHAPTERS LIST =====")

    # gets the image links for every chapter by iteration
    for chapter in chapters:

        url = "http://mangareader.cc/chapter/{}-chapter-{}#1".format(sub(r"\s", "-", manga_title), chapter)
        
        # u can always use ctrl + C
        while True:
            try:
            
                # requests the data
                req = requests.get(url).text
                break

            except Timeout:
                
                print("retrying to get the data\nyou can always use Ctrl + C if you think this is not gonna work")
                continue
        
        # parsing the data
        soup = bs(req, features="html.parser")
        
        # the p element contains the links for the images
        links_to_images["chapter {}".format(chapter)] = soup.find("p", id="arraydata").text.split(",")

    print("===== SUCCESSFULLY DONE =====\n")
    return links_to_images


# DOWNLOAD CHAPTERS
def download_chapters(data):

    manga_title = data["manga_title"]

    if not os.path.isdir(os.getcwd() + "\\temporal_images\\{}".format(manga_title)):

        os.mkdir(os.getcwd() + "\\temporal_images\\{}".format(manga_title))

    # a dictionary with all the links to specific chapters 
    links_to_images = data["links_to_images"]

    print("===== DOWNLOADING THE CHAPTERS =====\n")
    # will download all in the links_to_images array iteratively
    for chapter in links_to_images:

        # downloads the current chapter
        download_chapter(manga_title, chapter, links_to_images[chapter])
    
    print("===== SUCCESSFULLY DOWNLOADED ALL CHAPTERS =====\n")


# DOWNLOADS A SINGLE CHAPTER
def download_chapter(manga_title, chapter, chapter_images):

    iteration = 0

    print("===== DOWNLOADING CHAPTER NUMBER {} =====".format(chapter.split()[-1]))
    # chapter_images is supposed to be a list of links for downloading
    for image in chapter_images:
        
        # u can always use ctrl + C
        while True:

            try:
                # downloading the image
                req = requests.get(image)
                print("downloading {} - {}".format(chapter, iteration))
                break

            except Timeout:
                
                print("retrying to download this chapter\nyou can always use Ctrl + C if you think this is not gonna work")
                continue

        # creating the path for the future image
        image_extension = os.path.splitext(image)[-1].lower()
        path = os.getcwd() + "\\temporal_images\\{}\\{}#{}{}".format(manga_title, chapter, iteration, image_extension)

        # saving the image
        with open(path, "wb") as f:

            f.write(req.content)

        # doing this so the number of picture changes
        iteration += 1
    print("===== SUCCESSFULLY DOWNLOADED CHAPTER {} =====\n".format(chapter.split()[-1]))
