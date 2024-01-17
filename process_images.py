from PIL import Image
import os

def process_image(file_path):
    with Image.open(file_path) as img:
        # Calcular la nueva altura manteniendo la proporción
        new_height = int((140.0 / img.width) * img.height)
        img = img.resize((140, new_height), Image.Resampling.LANCZOS)
        img.save(file_path)

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith(('.jpg', '.png')):
            process_image(os.path.join(root, file))

print("Procesamiento de imágenes completado!")
