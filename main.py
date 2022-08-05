from working_logic import do_logic
from downloading import do_download_logic
from making_documents import do_document_logic
from delete_images import delete_images


if __name__ == "__main__":
    
    # asks the user for the needed data
    data = do_logic()
    
    # downloads all the images
    do_download_logic(data)

    # makes the document
    do_document_logic(data)

    # deletes the images after making the document
    delete_images(data)