import cv2
from pyzbar.pyzbar import decode
  
def BarcodeReader(img):  
    detectedBarcodes = decode(img)
      
    if not detectedBarcodes:
        print(f"{img} is damaged")
    else:
       
        for barcode in detectedBarcodes: 
           
            (x, y, w, h) = barcode.rect
             
            cv2.rectangle(img, (x-10, y-10),
                          (x + w+10, y + h+10),
                          (255, 0, 0), 2)
             
            if barcode.data!="":
               
                print("Saved Data- ",barcode.data)
                print("Bar Code Type- ",barcode.type)
                 
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return True
 
if __name__ == "__main__":

    from glob import glob

    barcodes = glob("Img*.png")
    for barcode_file in barcodes:
    # image="Img.jpg"
        img = cv2.imread(barcode_file)
        BarcodeReader(img)
    
    