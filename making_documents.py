import os


def do_document_logic(data):

    data["paths_to_downloaded_images"] = get_paths_to_images(data)

    return 1


# returns the paths to the immages 
def get_paths_to_images(data):

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

    e = os.path.splitext(e)[0]
    e = e.split("#")[0].split(" ")[1]

    print(e)

    return int(e)


def sorting_key(e):

    e = os.path.splitext(e)[0]
    e = e.split("#")[1]

    return int(e)


if __name__ == "__main__":

    do_document_logic({
        'manga_title': 'the scholars reincarnation', 
        'chapters': [1, 2]
        }, "docx")
    