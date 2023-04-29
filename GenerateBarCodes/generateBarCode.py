import barcode
from barcode.writer import ImageWriter
  

def generate_types():
    barcode_formats = barcode.PROVIDED_BARCODES
    for num in barcode_formats:
        print(num,end=", ")
    print("\n")
#Define content of the barcode as a string
def generate_barcode(text,type):
    number = text

    #Get the required barcode format
    barcode_format = barcode.get_barcode_class(type)

    #Generate barcode and render as image
    my_barcode = barcode_format(number, writer=ImageWriter())
    
    #Save barcode as PNG
    my_barcode.save(f"BarCode- {text}")

if __name__=="__main__":
    print("Choose a Barcode Type")
    generate_types()
    type=input()
    while True:
        try:
            text=input()
            if text:
                generate_barcode(text,type)
            else:
                break
            

        except:
            break