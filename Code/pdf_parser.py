import PyPDF2


class PDFToText():
    def __init__(self, file_path):
        self.pdfFileObj = open(file_path, 'rb')
        self.pdfReader = PyPDF2.PdfFileReader(self.pdfFileObj)
    
    def extractText(self):
        text = ""
        for page in range(self.pdfReader.numPages):
            text += " " + self.pdfReader.getPage(page).extractText()
        return text
        
    def extractAndSaveText(self, file_path):
        text = self.extractText()
        filePtr = open(file_path, "a")
        filePtr.write("Paragraph:\n")
        filePtr.write(text)


def main():
    pdf_reader = PDFToText("../BERT.pdf")
    print(pdf_reader.extractText())


if __name__ == "__main__":
    main()
        
