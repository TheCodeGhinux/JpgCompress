import numpy as np
from sklearn.cluster import KMeans
from PIL import Image

def load_image(file_path):
    return np.array(Image.open(file_path))

def flatten_image(image):
    return image.reshape(-1, 3)

def compress_image(image, n_clusters=8):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(image)
    compressed_colors = kmeans.cluster_centers_
    labels = kmeans.labels_
    compressed_image = compressed_colors[labels]
    return compressed_image.reshape(image.shape), compressed_colors

def save_image(image, file_path):
    Image.fromarray(image.astype('uint8')).save(file_path)
