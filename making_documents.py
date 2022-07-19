import os
from docx_logic import do_docx_logic
from pdf_logic import do_pdf_logic

def do_document_logic(data):

    data["paths_to_downloaded_images"] = get_paths_to_images(data)
    document_type = data["document_type"]
    
    if document_type == "docx":

        do_docx_logic(data)

    if document_type == "pdf":

        do_pdf_logic(data)

    return 1


# returns the paths to the immages 
def get_paths_to_images(data):
    """
    returns a dictionary with the paths to the downloaded images
    1: []
    1 is the chapter, and the list represents the list of images
    """
    manga_title = data["manga_title"]
    chapters = data["chapters"]


    paths_dictionary = {}
    # getting the names for the files and sorting the data 
    paths = os.listdir(".\\temporal_images\\{}\\".format(manga_title))

    # filtering by chapter
    for chapter in chapters:
        paths_dictionary[chapter] = list(filter(lambda path: chapter == filtering_key(path), paths))

    # sorting by image in every chapter list
    for chapter in paths_dictionary:
        
        # sorting by image number
        paths_dictionary[chapter].sort(key=sorting_key)  
        # adding the complete path to every element in the array 
        paths_dictionary[chapter] = list(map(lambda path: "{}\\temporal_images\\{}\\{}".format(os.getcwd(), manga_title, path), paths_dictionary[chapter])) 

    return paths_dictionary


def filtering_key(e):
    """
    filters by chapter
    """
    e = os.path.splitext(e)[0]
    e = e.split("#")[0].split(" ")[1]

    return int(e)


def sorting_key(e):
    """
    sorts by image number
    """
    e = os.path.splitext(e)[0]
    e = e.split("#")[1]

    return int(e)


if __name__ == "__main__":

    do_document_logic({
        'manga_title': 'the scholars reincarnation', 
        'chapters': [1],
        'document_type': 'docx'
        })
    