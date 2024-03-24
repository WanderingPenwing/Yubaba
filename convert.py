from PIL import Image
import moviepy.editor as mp  #pip install moviepy pydub
from pydub import AudioSegment
import numpy as np  # Importation de Numpy pour le traitement d'images
import matplotlib.pyplot as plt  # Pour l'affichage des images
import imageio as io  # Pour lire et enregistrer des images
from scipy.ndimage import rotate  # Fonction de rotation d'images

TYPE = {
    'IMAGE': ['jpeg', 'jpg', 'png', 'webp'],
    'VIDEO': ['mp4', 'avi', 'mov'],
    'AUDIO': ['mp3', 'wav', 'ogg', 'flac']
}

def find_file_name(input_path):
    name, ext, parent = '', '', ''
    dot, slash = False, False
    
    for _ in range(-1, -len(input_path)-1, -1):
        L = input_path[_]
        if L == '.' and not dot:
            dot = True
            continue
        if L == '/':
            slash = True
        if not dot:
            ext += L
        elif dot and not slash:
            name += L
        elif slash:
            parent += L
    return parent[::-1], name[::-1], ext[::-1]

def convert(input_path, ex_to=str, output_path=''):
    file_conv = None
    parent, file, ex_from = find_file_name(input_path)
    
    if output_path == '':
        output_path = parent + file + "." + ex_to
    else:
        output_path = output_path + file + "." + ex_to

    for KEY in TYPE:
        if ex_from in TYPE[KEY]:
            print(f'You are trying to convert a {KEY}')
            file_conv = KEY
            break
    
    if file_conv == 'IMAGE':
        Image.open(input_path).convert("RGB").save(output_path, ex_to)
    
    elif file_conv == 'VIDEO':
        clip = mp.VideoFileClip(input_path)
        clip.write_videofile(output_path)
    
    elif file_conv == 'AUDIO':
        sound = AudioSegment.from_file(input_path, format=ex_from)
        sound.export(output_path, format=ex_to)
    
    else:
        print("The file you are trying to convert is not supported.")

def symetrie(image):
    """Effectue une symétrie horizontale de l'image."""
    return image[:, ::-1]

def rotation(image, angle):
    """Effectue une rotation de l'image sans changer sa forme."""
    return rotate(image, angle, reshape=False, mode='constant', cval=0)

def negative(image):
    """Convertit une image en son négatif."""
    return 255 - image

def convertir_en_niveaux_de_gris(image):
    """Convertit une image couleur en niveaux de gris selon la luminance."""
    if image.ndim == 3 and image.shape[2] == 3:
        r, g, b = image[:,:,0], image[:,:,1], image[:,:,2]
        # Calcul de la luminance en utilisant la formule de conversion en niveaux de gris
        y = 0.2126 * r + 0.7152 * g + 0.0722 * b
        image_grise = np.round(y).astype(np.uint8)
        return image_grise
    else:
        print("L'image n'est pas en couleur ou n'a pas le bon format.")
        return image  # Retourne l'image inchangée si elle n'est pas en couleur

def convolution(image, kernel):
    """Applique un kernel de convolution sur l'image."""
    output = np.zeros((image.shape[0] - kernel.shape[0] + 1, 
                       image.shape[1] - kernel.shape[1] + 1, 3), dtype=np.float32)
    
    for color in range(3):
        for y in range(output.shape[0]):
            for x in range(output.shape[1]):
                section = image[y:y+kernel.shape[0], x:x+kernel.shape[1], color]
                output[y, x, color] = np.sum(section * kernel)
                
    return np.clip(output, 0, 255).astype(np.uint8)

def lissage(image):
    """Lisse l'image en utilisant un filtre moyen."""
    kernel = np.ones((3, 3), dtype=np.float32) / 9
    return convolution(image, kernel)

def contraste(image):
    """Augmente le contraste de l'image."""
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]], dtype=np.float32)
    return convolution(image, kernel)

def repoussage(image):
    """Applique un effet de repoussage."""
    kernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]], dtype=np.float32)
    return convolution(image, kernel)

if __name__ == '__main__':
    convert('D:\Docs\@PAUL\ICAM\I4\Hackhaton\Yubaba\videos\test.mp4', 'avi')  # Assure-toi de remplacer par le chemin de ton fichier et le format voulu.