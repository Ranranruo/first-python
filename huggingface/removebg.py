from rembg import remove
from PIL import Image

input_image = Image.open("image.png")

output_image = remove(input_image)

output_image.save("image_no_bg.png")