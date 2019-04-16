from PyPDF4 import PdfFileReader, PdfFileWriter
from argparse import ArgumentParser
import numpy as np
import glob


class PDFTools:

    def __init__(self, arg_parser=None):
        self.parser = self.arg_parse(arg_parser)
        print(self.parser)
        if self.parser.m:
            print("Working on PDF files...")
            self.directory_name = self.parser.m[0]
            self.extension = self.parser.m[1]
            self.save_directory_name = self.parser.m[2]

            self.is_file_exist(self.parser.m[2])

            self.pdf_merger(self.get_array_list_of_files_names(self.directory_name, self.extension),
                                  self.save_directory_name)
            print("Done.")

    def arg_parse(self, arg_parser):
        if arg_parser is None:
            print("Welcome to the PDF Tools. Use '-h' argument to get the information about the commands.")

            argp = ArgumentParser()
            argp.add_argument("-m", nargs=3, type=str, help="Merge all PDF files in the folder (ascending order). "
                                                            "Requires three arguments: directory_path, files extension "
                                                            "(i.e. *pdf) and save_dir_path")

            return argp.parse_args()
        else:
            return arg_parser

    def is_file_exist(self, file_name):
        try:
            PdfFileReader(open(file_name, mode='rb'))
            print("The file exist. Please input different output file name.")
            return True
            exit(0)
        except FileNotFoundError:
            print("The output file name is correct. There is no file with same name.")
            return False

    def get_array_list_of_files_names(self, directory, extension):
        print("Reading PDF files...")
        return np.array(glob.glob(directory+extension))

    def sort_array_list_of_files_names(self, array_list_of_pdf_files):
        array_list_of_pdf_files.sort()

        return array_list_of_pdf_files

    def pdf_merger(self, array_list_of_pdf_files, merged_pdf_output_name):
        print("Merging PDF files...")
        write_pdf = PdfFileWriter()

        for pdf_file in self.sort_array_list_of_files_names(array_list_of_pdf_files):
            read_pdf = PdfFileReader(open(pdf_file, mode='rb'))
            for page_num in range(read_pdf.getNumPages()):
                write_pdf.addPage(read_pdf.getPage(page_num))

        write_pdf.write(open(merged_pdf_output_name, 'wb'))

if __name__ == "__main__":
    PDFTools()