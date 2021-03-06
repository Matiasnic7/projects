import time
import pyautogui
import mouse
import pytesseract as tess

# tesseract para funcionar necesita el path, es un engine externo, cambiar de acuerdo donde se instaló

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Obtener posición del mouse
def mouse_pos():
    get_mouse_pos = pyautogui.position()
    return get_mouse_pos


# Positions del mouse se guardan en la lista luego se obtiene la primera y última para generar rectángulo de impresión
# Trazar zona rectangular arrastrando mouse, finalizar con click derecho
# Se añadieron correciones al trazado de imagen según pruebas

on_click = True
positions = []
while on_click:
    if mouse.is_pressed(button='left'):
        pos = mouse_pos()
        positions.append(pos)
        first_point = positions[0]
        last_point = positions[-1]

    if mouse.is_pressed(button='right'):
        on_click = False

# Tomar screenshot de la selección
im = pyautogui.screenshot(region=(first_point.x - 20, first_point.y - 20, last_point.x - 360, last_point.y - 450),
                          imageFilename='screenshot.png')
# Imagen a texto
text = tess.image_to_string(im)

# Reemplaza error usual de lectura y saltos de linea

text = text.replace("|", "I").replace("/", "I've")
text = text.replace("\n", " ")
print(text)

# Entrada de texto en el teclado
time.sleep(2)
words_text = text.split()

for words in words_text:
    time.sleep(0.34)
    pyautogui.write(words)
    pyautogui.write(" ")