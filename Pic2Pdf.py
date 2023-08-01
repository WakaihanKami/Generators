from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import os

def add_images_to_pdf(pdf_filename, image_filenames):
    # Erstelle ein neues PDF-Dokument mit dem Namen 'pdf_filename'
    pdf_canvas = canvas.Canvas(pdf_filename, pagesize=letter)

    for image_filename in image_filenames:
        # Überprüfe, ob die Bild-Datei existiert
        if not os.path.exists(image_filename):
            # Wenn die Datei nicht existiert, überspringe das Bild und zeige eine Warnung an
            print(f"Warnung: Die Datei {image_filename} wurde nicht gefunden und wird übersprungen.")
            continue

        # Öffne das Bild mit Hilfe von PIL (Python Imaging Library) und erhalte die Bildgröße
        image = Image.open(image_filename)
        img_width, img_height = image.size

        # Berechne das Seitenverhältnis des Bildes, um die Skalierung zu bestimmen
        aspect_ratio = img_height / float(img_width)

        # Setze die maximale Breite für das Bild auf 500 Pixel
        max_width = 500
        # Berechne die Höhe basierend auf dem Seitenverhältnis
        max_height = max_width * aspect_ratio

        # Skaliere das Bild, um sicherzustellen, dass es vollständig in der PDF sichtbar ist
        if max_height > 720:
            max_height = 720
            max_width = max_height / aspect_ratio

        # Zentriere das Bild auf der Seite (horizontal und vertikal)
        x_offset = (letter[0] - max_width) / 2
        y_offset = (letter[1] - max_height) / 2

        # Füge das Bild zur PDF-Seite hinzu
        pdf_canvas.drawImage(image_filename, x_offset, y_offset, width=max_width, height=max_height)

        # Zeige die Seite an und starte eine neue Seite für das nächste Bild
        pdf_canvas.showPage()

    # Speichere und schließe das PDF-Dokument
    pdf_canvas.save()

    # Gib eine Meldung aus, dass die PDF-Datei erfolgreich erstellt wurde
    print(f"PDF '{pdf_filename}' wurde erfolgreich erstellt.")
    
# Die if-Anweisung prüft, ob dieses Skript direkt ausgeführt wird (nicht importiert).
# Wenn das Skript direkt ausgeführt wird, wird der darin enthaltene Code ausgeführt,
# andernfalls wird der Code innerhalb der if-Anweisung übersprungen, wenn das Skript importiert wird.
if __name__ == "__main__": 
    # Dateinamen für die PDF-Datei
    pdf_filename = "mein_pdf.pdf"

    # Liste der Dateinamen
    image_filenames = ["bild1.jpg", "bild2.jpeg", "bild3.jpeg", "bild4.jpeg", "bild5.jpeg", "bild6.jpeg", "bild7.jpeg", "bild8.jpeg"]

    # Rufe die Funktion add_images_to_pdf auf, um die Bilder zur PDF hinzuzufügen
    add_images_to_pdf(pdf_filename, image_filenames)
