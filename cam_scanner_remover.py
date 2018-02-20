from PyPDF2 import PdfFileReader, PdfFileWriter


def remove_watermark(path):
    input_file = PdfFileReader(open(path, 'rb'))
    output = PdfFileWriter()
    for page_number in range(input_file.getNumPages()):
        page = input_file.getPage(page_number)
        page.mediaBox.lowerLeft = (page.mediaBox.getLowerLeft_x(), 20)
        output.addPage(page)
    return output


"""
input_file = PdfFileReader(open('test1.pdf', 'rb'))
output = PdfFileWriter()
page_count = input_file.getNumPages()

for page_number in range(input_file.getNumPages()):
    page = input_file.getPage(page_number)
    page.mediaBox.lowerLeft = (page.mediaBox.getLowerLeft_x(), 20)
    output.addPage(page)

output_stream = open('output.pdf', 'wb')
output.write(output_stream)
"""
