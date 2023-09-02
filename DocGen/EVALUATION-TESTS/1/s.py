import os
from datetime import datetime
from PIL import Image
import svgwrite
from svgwrite import cm, mm
import cairosvg

# Convert SVG to PNG
def svg_to_png(svg_path, png_path):
    cairosvg.svg2png(url=svg_path, write_to=png_path)

# Converts an image to SVG
def raster_to_svg(image_path, svg_path):
    img = Image.open(image_path).convert("RGBA")
    dwg = svgwrite.Drawing(svg_path, profile='tiny', size=(img.width, img.height))
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.getpixel((x, y))
            if pixel[3] > 0:  # Skip transparent pixels
                dwg.add(dwg.rect(insert=(x, y), size=(1, 1), fill=svgwrite.rgb(pixel[0], pixel[1], pixel[2], '%')))
    dwg.save()

# Overlay images
def overlay_images(icon_path, overlay_path, output_path, transparency):
    icon = Image.open(icon_path).convert("RGBA")
    overlay = Image.open(overlay_path).convert("RGBA")
    output = Image.new("RGBA", icon.size)

    for x in range(icon.width):
        for y in range(icon.height):
            icon_pixel = icon.getpixel((x, y))
            overlay_pixel = overlay.getpixel((x, y))

            if icon_pixel[3] > 0:
                new_alpha = int((100 - transparency) / 100 * overlay_pixel[3])
                new_pixel = (
                    (icon_pixel[0] + overlay_pixel[0]) // 2,
                    (icon_pixel[1] + overlay_pixel[1]) // 2,
                    (icon_pixel[2] + overlay_pixel[2]) // 2,
                    new_alpha,
                )
            else:
                new_pixel = icon_pixel

            output.putpixel((x, y), new_pixel)

    output.save(output_path)

# List contents of 'mask' folder
mask_folder_path = "mask"
available_masks = [mask for mask in os.listdir(mask_folder_path) if mask.endswith(".png")]

# User input
transparency = int(input("Enter the transparency value (0-100): "))
folder_path = "icons"

def process_mask(mask):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_output_folder = f"output/{mask}_{timestamp}"
    if not os.path.exists(unique_output_folder):
        os.makedirs(unique_output_folder)

    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith((".png", ".svg")):
                full_path = os.path.join(root, filename)
                output_path = os.path.join(unique_output_folder, filename)
                overlay_path = os.path.join(mask_folder_path, mask)

                if filename.endswith(".svg"):
                    temp_png_path = os.path.join(unique_output_folder, "temp.png")
                    temp_svg_path = os.path.join(unique_output_folder, "temp.svg")
                    svg_to_png(full_path, temp_png_path)
                    overlay_images(temp_png_path, overlay_path, temp_png_path, transparency)
                    raster_to_svg(temp_png_path, temp_svg_path)
                    os.rename(temp_svg_path, output_path)
                    os.remove(temp_png_path)
                else:
                    overlay_images(full_path, overlay_path, output_path, transparency)

chosen_mask = input("Enter the filename of the overlay (mask) you want to use or type 'ALL' for bulk processing: ")

if chosen_mask.upper() == "ALL":
    for mask in available_masks:
        process_mask(mask)
else:
    process_mask(chosen_mask)
