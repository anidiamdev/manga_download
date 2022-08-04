
# USES ALL THE FUNCTIONS IN THIS FILE FOR PASSING INTO THE NEXT DOWNLOADING STAGE
def do_logic():

    data = ask_for_data()
    data["chapters"] = return_chapters(data["chapters"])

    return data


# RETURNS THE USER DATA ABOUT THE CHAPTER THEY WANT TO DOWNLOAD
def ask_for_data():

    manga_title = input("Title: ").lower()

    while True:

        # just in case the user is stupid
        document_type = input("Document type (docx/pdf)?: ").lower()
        if document_type != "docx" and document_type != "pdf":
            continue

        try:

            print("Which chapters do you want to download?\nYou can input a single number or do it this way:\n5-13 (downloads from chapter 5 to 13)")
            chapters = input().split("-")
            chapters = list(map((lambda x: int(x)), chapters))  # converting list items to ints
            break

        except ValueError:

            continue

    return({
        "manga_title": manga_title,
        "chapters": chapters,
        "document_type": document_type
    })


# RETURNS A LIST WITH THE CHAPTERS THE USER WANTS TO DOWNLOAD
def return_chapters(chapters):

    if len(chapters)>1:
        
        assert chapters[0] < chapters[1], "THE SECOND VALUE CANT BE LEAST THAN THE FIRST"

        return list(range(chapters[0], chapters[1] + 1))

    else:
        
        #DOWNLOADING A SINGLE CHAPTER
        return [chapters[0]]


if __name__ == "__main__":

    print(do_logic())