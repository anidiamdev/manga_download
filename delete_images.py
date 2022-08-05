import shutil
import os


def delete_images(data):

    manga_title = data["manga_title"]

    path = "{}\\temporal_images\\{}\\".format(os.getcwd(), manga_title)

    try:

        shutil.rmtree(path)

    except:

        print("couldn't delete images, check the corresponding path: {}".format(path))