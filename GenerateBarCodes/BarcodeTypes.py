import barcode

barcode_formats = barcode.PROVIDED_BARCODES

print(barcode_formats)

for num in barcode_formats:
    print(num,end=", ")
# ['codabar', 'code128', 'code39', 'ean', 'ean13', 'ean13-guard', 'ean14', 'ean8',
#  'ean8-guard', 'gs1', 'gs1_128', 'gtin', 'isbn', 'isbn10', 'isbn13', 'issn', 'itf',
#  'jan', 'nw-7', 'pzn', 'upc', 'upca']
