from pdfminer.pdfparser import PDFParser, PDFDocument


def parse(filename):
    f = open(filename, 'rb')
    parser = PDFParser(f)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize()

    return doc.info[0]
