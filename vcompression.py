from PIL import Image
import PIL
import os
import glob

# Start First Compression
current_working_directory = os.getcwd()
files = os.listdir()

images = [file for file in files if file.endswith(
    ('jpg', 'png')) and '' in file]

# Create "Compressed" folder to put the compressed images into
os.mkdir("Compressed")
for image in images:
    image_name = image.split('.')[0]

    img = Image.open(image)
    img.save("Compressed/" + image, optimized=True, quality=35)


# Start WebP Coversion and Compression
current_working_directory = os.chdir('Compressed')
files = os.listdir()

images = [file for file in files if file.endswith(
    ('jpg', 'png')) and '' in file]

# Creates a "WebP" folder inside the "Compressed" folder to put the WebP conversions into
os.mkdir("WebP")

for image in images:
    image_name = image.split('.')[0]

    img = Image.open(image)
    img.convert('RGB')
    img.save('WebP/' + image_name + '.webp',
             'webp', quality=38)
