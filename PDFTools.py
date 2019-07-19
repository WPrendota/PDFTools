from PyPDF4 import PdfFileReader, PdfFileWriter
from argparse import ArgumentParser
from datetime import datetime
import numpy as np
import glob


class PDFTools:

    def __init__(self, arg_parser=None):
        self.parser = self.arg_parse(arg_parser)
        print(self.parser)

        if self.parser.m:
            print("Working on PDF files...")
            self.directory_name = self.parser.m[0]
            self.save_directory_name = self.parser.m[1]

            self.pdf_merger(self.get_array_list_of_files_names(self.directory_name),
                                  self.save_directory_name)
            print("Done.")

        if self.parser.s:
            print("Working on PDF files...")

            self.pdf_splitting(self.parser.s[0], self.parser.s[1])

            print("Done.")

        if self.parser.r:
            print("Working on PDF files...")

            self.pdf_pages_rotation(self.parser.r[0], self.parser.r[1], int(self.parser.r[2]), self.parser.r[3])

            print("Done.")

        if self.parser.d:
            print("Working on PDF files...")

            self.pdf_pages_delete(self.parser.d[0], self.parser.d[1], self.parser.d[2])

            print("Done.")

    def arg_parse(self, arg_parser):
        if arg_parser is None:
            print("Welcome to the PDF Tools. Use '-h' argument to get the information about the commands.")

            argp = ArgumentParser()
            argp.add_argument("-m", nargs=2, type=str, help="Merge all PDF files in the folder (ascending order)."
                                                            "Requires two arguments: directory_path and save_dir_path")
            argp.add_argument("-s", nargs=2, type=str, help="Splits PDF file into single-page PDF files."
                                                            "Requires two arguments: file_name and save_dir_path")
            argp.add_argument("-r", nargs=4, type=str, help="Rotates PDF file pages."
                                                            "Requires four arguments: file_name, pages range, "
                                                            "angle and save_dir_path")
            argp.add_argument("-d", nargs=3, type=str, help="Delete PDF file pages."
                                                            "Requires three arguments: file_name, pages range "
                                                            "and save_dir_path")

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
            print("The output file name is correct. There is no file with the same name.")
            return False

    def get_array_list_of_files_names(self, directory):
        print("Reading PDF files...")
        print(glob.glob(directory+'*.pdf'))
        return np.array(glob.glob(directory+'*.pdf'))

    def sort_array_list_of_files_names(self, array_list_of_pdf_files):
        array_list_of_pdf_files.sort()
        print(array_list_of_pdf_files)
        return array_list_of_pdf_files

    def pdf_merger(self, array_list_of_pdf_files, merged_pdf_output_name):
        print("Merging PDF files...")
        write_pdf = PdfFileWriter()

        for pdf_file in self.sort_array_list_of_files_names(array_list_of_pdf_files):
            read_pdf = PdfFileReader(open(pdf_file, mode='rb'))
            for page_num in range(read_pdf.getNumPages()):
                write_pdf.addPage(read_pdf.getPage(page_num))

        write_pdf.write(open(merged_pdf_output_name, 'wb'))

    def pdf_splitting(self, file_name, output_directory):
        print("Splitting PDF file...")

        self.check_if_str(file_name, 'file_name')
        self.check_if_str(output_directory, 'output_directory')

        read_pdf = PdfFileReader(open(file_name, mode='rb'))

        for page_num in range(read_pdf.getNumPages()):
            read_pdf = PdfFileReader(open(file_name, mode='rb'))
            write_pdf = PdfFileWriter()
            write_pdf.addPage(read_pdf.getPage(page_num))
            write_pdf.write(open(output_directory + str(page_num) + '.pdf', 'wb'))

    def pdf_pages_rotation(self, file_name, pages_range, angle, output_directory):
        print("Rotating PDF file pages...")

        read_pdf = PdfFileReader(open(file_name, mode='rb'))
        write_pdf = PdfFileWriter()

        self.check_if_int(angle, 'angle')
        self.check_if_str(file_name, 'file_name')
        self.check_if_str(pages_range, 'pages_range')
        self.check_if_str(output_directory, 'output_directory')

        for page_num in range(read_pdf.getNumPages()):
            if page_num >= int(pages_range[0])-1 and page_num <= int(pages_range[-1])-1:
                write_pdf.addPage(read_pdf.getPage(page_num).rotateClockwise(angle))
            else:
                write_pdf.addPage(read_pdf.getPage(page_num))

        write_pdf.write(open(output_directory + 'Rotated_' + str(datetime.now().strftime("%y_%m_%d_%H_%M_%S")) + '.pdf', 'wb'))

    def check_if_int(self, value, parameter_name):
        if int(value) == value:
            return True
        else:
            print(parameter_name+" must be integer.")
            exit(0)

    def check_if_str(self, value, parameter_name):
        if str(value) == value:
            return True
        else:
            print(parameter_name + " must be str.")
            exit(0)

    def pdf_pages_delete(self, file_name, pages_range, output_directory):
        print("Delete PDF file pages...")

        read_pdf = PdfFileReader(open(file_name, mode='rb'))
        write_pdf = PdfFileWriter()

        self.check_if_str(file_name, 'file_name')
        self.check_if_str(pages_range, 'pages_range')
        self.check_if_str(output_directory, 'output_directory')

        for page_num in range(read_pdf.getNumPages()):
            if page_num >= int(pages_range[0]) - 1 and page_num <= int(pages_range[-1]) - 1:
                pass
            else:
                write_pdf.addPage(read_pdf.getPage(page_num))

        write_pdf.write(open(output_directory + 'Deleted_' + str(datetime.now().strftime("%y_%m_%d_%H_%M_%S")) + '.pdf', 'wb'))


if __name__ == "__main__":
    PDFTools()