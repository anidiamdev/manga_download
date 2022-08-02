from fpdf import FPDF

def do_pdf_logic(data):

    pdf_file = create_pdf()
    add_images(data, pdf_file)

    return 0


def create_pdf():

    pdf_file = FPDF()
    pdf_file.set_left_margin(32.0)

    return pdf_file


def add_images(data, pdf_file):

    wScale = 150

    pdf_file.set_font("Arial",size=50)
    pdf_file.set_text_color(0,0,0)

    for key in data["paths_to_downloaded_images"]:

        pdf_file.add_page()
        pdf_file.text(60,50,txt="chapter #{}".format(key))
        pdf_file.add_page()

        for path in data["paths_to_downloaded_images"][key]:

            pdf_file.image(path, w=wScale)
    
    pdf_file.output("test_document.pdf")

    return 