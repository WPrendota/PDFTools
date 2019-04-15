from PyPDF4 import PdfFileReader, PdfFileWriter
from argparse import ArgumentParser
import numpy as np
import glob


class PDFTools:
    __directory_name__ = "/home/witek/Pictures/"
    __extension__ = "*pdf"

    def __init__(self):
        print("Working on PDF files...")

    def pdf_merger(self, array_list_of_pdf_files, merged_pdf_output_name):
        print("Merging PDF files...")
        write_pdf = PdfFileWriter()

        for pdf_file in array_list_of_pdf_files:
            read_pdf = PdfFileReader(open(pdf_file, mode='rb'))
            for page_num in range(read_pdf.getNumPages()):
                write_pdf.addPage(read_pdf.getPage(page_num))

        write_pdf.write(open(merged_pdf_output_name, 'wb'))

    def get_array_list_of_files_names(self, directory, extension):
        print("Reading PDF files...")
        return np.array(glob.glob(directory+extension))


if __name__ == "__main__":
    argp = ArgumentParser()
    argp.add_argument("--m", action='store_true', help="Merge all PDF files in the folder (ascending order).")
    argsp = argp.parse_args()

    if argsp.m:
        pdft = PDFTools()
        pdft.get_array_list_of_files_names(pdft.__directory_name__, pdft.__extension__)

        print(pdft.get_array_list_of_files_names(pdft.__directory_name__, pdft.__extension__))

        PDFTools().pdf_merger(pdft.get_array_list_of_files_names(pdft.__directory_name__, pdft.__extension__),
                              "All_.pdf")