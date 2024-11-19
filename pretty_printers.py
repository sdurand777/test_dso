import gdb
import numpy as np
from PIL import Image

class ImagePrettyPrinter(gdb.Command):
    """Affiche une image dans GDB en utilisant PIL."""

    def __init__(self):
        super(ImagePrettyPrinter, self).__init__("show_image", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        # Récupérer l'adresse de la structure à partir de l'argument
        img = gdb.parse_and_eval(arg)

        # Lire les dimensions
        width = int(img['w'])
        height = int(img['h'])

        # Lire l'adresse des données de l'image
        image_ptr = img['image']

        # Charger les pixels en mémoire
        float_size = gdb.lookup_type("float").pointer().target().sizeof
        pixel_data = gdb.selected_inferior().read_memory(image_ptr, width * height * float_size)

        # Convertir les données en tableau numpy
        pixels = np.frombuffer(pixel_data, dtype=np.float32).reshape((height, width))

        # Normaliser les valeurs pour affichage (0-255)
        pixels_normalized = np.clip(pixels / pixels.max() * 255, 0, 255).astype(np.uint8)

        # Créer une image avec PIL
        img = Image.fromarray(pixels_normalized, mode="L")
        img.show()

# Enregistrer la commande dans GDB
ImagePrettyPrinter()




