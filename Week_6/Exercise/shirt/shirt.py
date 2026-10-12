
import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

input_ext = os.path.splitext(input_file)[1].lower()
output_ext = os.path.splitext(output_file)[1].lower()

valid_extensions = [".jpg", ".jpeg", ".png"]

if input_ext not in valid_extensions:
    sys.exit("Invalid input")

if output_ext not in valid_extensions:
    sys.exit("Invalid output")

if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

try:
    with Image.open(input_file) as photo:
        with Image.open("shirt.png") as shirt:
            fitted = ImageOps.fit(photo, shirt.size)
            fitted.paste(shirt, shirt)
            fitted.save(output_file)

except FileNotFoundError:
    sys.exit("Input does not exist")
