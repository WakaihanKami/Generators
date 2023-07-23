import qrcode
from PIL import Image
import os

def gen_qr(link, image_path=None, output_folder="./", base_name="Code"):
    # Erstelle einen QR-Code-Objekt
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4) # QRCode-Objekt mit Version 1, einer Fehlerkorrekturstufe von 30%, einer Box-Größe von 10 Pixeln und einem Rand von 4 Boxen.
    
    # Füge den Link zum QR-Code hinzu
    qr.add_data(link)
    
    # Generiere den QR-Code
    qr.make(fit=True)

    # Erstelle ein Image-Objekt des QR-Codes
    qr_img = qr.make_image(fill_color="black", back_color="white")  # Standardmäßig weißer Hintergrund
    
    if image_path:
        # Öffne das Bild, das in den QR-Code eingefügt werden soll
        img = Image.open(image_path)
        
        # Erhalte die Größe des Bildes und des QR-Codes
        img_size = img.size
        qr_size = qr_img.size
        
        # Berechne das Verhältnis von QR-Code zu Bild (1:50)
        scaling_factor = qr_size[0] / (img_size[0] * 50)
        new_img_size = (int(img_size[0] * scaling_factor), int(img_size[1] * scaling_factor))
        
        # Skaliere das Bild entsprechend
        img = img.resize(new_img_size, Image.ANTIALIAS)
        
        # Berechne die Position, um das Bild in der Mitte des QR-Codes zu platzieren
        position = ((qr_size[0] - new_img_size[0]) // 2, (qr_size[1] - new_img_size[1]) // 2)
        
        # Füge das Bild in den QR-Code ein
        qr_img.paste(img, position)

    # Zähler für die generierten QR-Codes
    count = 1

    # Speichere den QR-Code als PNG-Datei mit entsprechendem Dateinamen
    while True:
        file_name = f"{output_folder}{base_name}{count}.png"
        if not os.path.exists(file_name):
            qr_img.save(file_name)
            break
        count += 1
# Der Zähler count wird so lange erhöht, bis ein eindeutiger Dateiname gefunden wird
# Beispielaufruf ohne Angabe einer PNG/JPEG-Datei
gen_qr("Link", output_folder="./", base_name="Code")
