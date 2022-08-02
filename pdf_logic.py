from fpdf import FPDF

def do_pdf_logic(data):

    pdf_file = create_pdf()
    add_images(data, pdf_file)

    return 0


def create_pdf():

    pdf_file = FPDF()

    return pdf_file


def add_images(data, pdf_file):

    wScale = data["wScale"] or 150

    pdf_file.set_font("Arial",size=50)
    pdf_file.set_text_color(0,0,0)

    for key in data["paths_to_downloaded_images"]:

        pdf_file.add_page()
        pdf_file.text(50,50,txt="chapter #{}".format(key))

        for path in data["paths_to_downloaded_images"][key]:

            print("lol")

            pdf_file.image(path, x=0, w=wScale)
    
    pdf_file.output("test_document.pdf")

    return 