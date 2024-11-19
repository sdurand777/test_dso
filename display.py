
import numpy as np
from PIL import Image

# Charger les données
data = np.fromfile('image_dump.bin', dtype=np.float32).reshape((480, 640))

# Normaliser et convertir en uint8
data = ((data - data.min()) / (data.max() - data.min()) * 255).astype(np.uint8)

# Afficher l'image
Image.fromarray(data).show()
