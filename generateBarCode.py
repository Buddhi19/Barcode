import barcode
from barcode.writer import ImageWriter
  
#Define content of the barcode as a string
number = 'helloworld-1234'

#Get the required barcode format
barcode_format = barcode.get_barcode_class('code39')

#Generate barcode and render as image
my_barcode = barcode_format(number, writer=ImageWriter())
  
#Save barcode as PNG
my_barcode.save("BarCode")
