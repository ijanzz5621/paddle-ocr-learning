from pdf2image import convert_from_path

def run():
    images = convert_from_path("data/sample.pdf")
    print(images)
    
    
