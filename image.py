import ffmpeg
import os
import numpy as np
import imageio as io
from scipy.ndimage import rotate
from PIL import Image

def symetrie(image):
    return image[:, ::-1]

def rotation(image, angle):
    return rotate(image, angle, reshape=False, mode='constant', cval=0)

def negative(image):
    return 255 - image

def convertir_en_niveaux_de_gris(image):
    if image.ndim == 3 and image.shape[2] == 3:
        r, g, b = image[:,:,0], image[:,:,1], image[:,:,2]
        y = 0.2126 * r + 0.7152 * g + 0.0722 * b
        image_grise = np.round(y).astype(np.uint8)
        return image_grise
    else:
        print("L'image n'est pas en couleur ou n'a pas le bon format.")
        return image

def convolution(image, kernel):
    output = np.zeros((image.shape[0] - kernel.shape[0] + 1, 
                       image.shape[1] - kernel.shape[1] + 1, 3), dtype=np.float32)
    for color in range(3):
        for y in range(output.shape[0]):
            for x in range(output.shape[1]):
                section = image[y:y+kernel.shape[0], x:x+kernel.shape[1], color]
                output[y, x, color] = np.sum(section * kernel)
    return np.clip(output, 0, 255).astype(np.uint8)

def lissage(image):
    kernel = np.ones((3, 3), dtype=np.float32) / 9
    return convolution(image, kernel)

def contraste(image):
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]], dtype=np.float32)
    return convolution(image, kernel)

def repoussage(image):
    kernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]], dtype=np.float32)
    return convolution(image, kernel)

def traiter_comprimer_image(image_path, effet, output_folder, output_extension, qualite=85, *args):
    image = io.imread(image_path)
    
    image_traitee = None
    if effet == "symetrie":
        image_traitee = symetrie(image)
    elif effet == "rotation":
        angle = args[0] if args else 0
        image_traitee = rotation(image, angle)
    elif effet == "negative":
        image_traitee = negative(image)
    elif effet == "niveaux_de_gris":
        image_traitee = convertir_en_niveaux_de_gris(image)
    elif effet == "lissage":
        image_traitee = lissage(image)
    elif effet == "contraste":
        image_traitee = contraste(image)
    elif effet == "repoussage":
        image_traitee = repoussage(image)
    else:
        print("Effet non reconnu.")
        return
    
    nom_base = os.path.basename(image_path).split('.')[0]
    output_file = f"{output_folder}/{nom_base}_{effet}_compresse.{output_extension}"
    
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder, exist_ok=True)
    
    image_traitee = Image.fromarray(image_traitee)
    image_traitee.save(output_file, format=output_extension.upper(), quality=qualite)
    print(f"L'image compressée a été sauvegardée sous : {output_file}")

if __name__ == '__main__':
    traiter_comprimer_image('D:\Docs\@PAUL\ICAM\I4\Hackhaton\Yubaba\images\crazy squirrel.jpg', 'symetrie', 'converted_images', 'png', 80)