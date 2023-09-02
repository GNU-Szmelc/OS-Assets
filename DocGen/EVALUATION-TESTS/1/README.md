# EVAL RUN #1

## TOTAL SCORE 100%
## 2 FILES TOTAL
============ PRELIMINARY RESULTS AFTER 3 RUNS ==========
 FILES TOTAL: 2
 - s.py
 - 1.py

== PRELIMINARY ===
 Runs: 3
 Run 1
 - 100% / 100%
 Run 2
 - 100% / 100%
 Run 3
 - 100% /100%
============

======= TEMPLATE USED =========================================================

### Code Snippet Documentation: [Script Name]

**File:** [file_name + extension] (e.g., `script.py`)

**Description:**
A concise description of what the script accomplishes.

#### Usage:
Provide instructions on how to use the script, including required inputs or parameters.

#### Functionality:
Describe the primary functionality and purpose of the script.

#### Notes:
Include any crucial notes or considerations for users regarding the script.

=============================================================================

                          === [CASE 1]:
             
=============================== s.py ========================================

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

=============================== </s.py> ========================================

Generated:

======================================================================

### Code Snippet Documentation: [Script Name]

**File:** s.py

**Description:**
This script allows you to overlay images with a specified mask. It can convert SVG images to PNG, convert raster images to SVG, and overlay images with transparency.

#### Usage:
1. Run the script.
2. Enter the transparency value (0-100) when prompted.
3. Enter the filename of the overlay (mask) you want to use or type 'ALL' for bulk processing.

#### Functionality:
- Converts SVG images to PNG using the `svg_to_png()` function.
- Converts raster images to SVG using the `raster_to_svg()` function.
- Overlays images with transparency using the `overlay_images()` function.
- Lists the contents of the 'mask' folder.
- Processes a single mask or all masks depending on user input.

#### Notes:
- Make sure you have the required Python libraries installed (`os`, `datetime`, `PIL`, `svgwrite`, `cairosvg`).
- The script assumes that the mask folder is named "mask".
- The script assumes that the output folder is named "output" and creates unique subfolders within it for each mask processed.
- The overlay images should have the same dimensions as the icons.
- The script only processes PNG and SVG files in the icons folder.
- If the filename ends with ".svg", the script converts it to PNG and SVG before overlaying.
- If the filename ends with ".png", the script overlays it directly.
- The transparency value should be between 0 and 100 (inclusive).

=============================================================================================

 === [CASE 2]:
=============================== 1.py ========================================

from PIL import Image
import os
from datetime import datetime

def overlay_images(icon_path, overlay_path, output_path, transparency):
    icon = Image.open(icon_path).convert("RGBA")
    overlay = Image.open(overlay_path).convert("RGBA")
    output = Image.new("RGBA", icon.size)

    for x in range(icon.width):
        for y in range(icon.height):
            icon_pixel = icon.getpixel((x, y))
            overlay_pixel = overlay.getpixel((x, y))

            if icon_pixel[3] > 0:
                new_alpha = int((100 - transparency SCORE ) / 100 * overlay_pixel[3])
                new_overlay_pixel = (
                    overlay_pixel[0],
                    overlay_pixel[1],
                    overlay_pixel[2],
                    new_alpha,
                )
                new_pixel = (
                    (icon_pixel[0] + new_overlay_pixel[0]) // 2,
                    (icon_pixel[1] + new_overlay_pixel[1]) // 2,
                    (icon_pixel[2] + new_overlay_pixel[2]) // 2,
                    icon_pixel[3],
                )
            else:
                new_pixel = icon_pixel

            output.putpixel((x, y), new_pixel)

    output.save(output_path)

# List contents of 'mask' folder
mask_folder_path = "mask"
print("Available overlays (masks) in the 'mask' folder:")
available_masks = [mask for mask in os.listdir(mask_folder_path) if mask.endswith(".png")]
for mask in available_masks:
    print(mask)

# Ask user to choose an overlay (mask)
chosen_mask = input("Enter the filename of the overlay (mask) you want to use or type 'ALL' for bulk processing: ")

# User-defined transparency value (0 is opaque, 100 is fully transparent)
transparency = int(input("Enter the transparency value (0-100): "))

# Path to the folder containing the icons
folder_path = "png"

def process_mask(mask):
    # Create a unique folder for each process inside the 'output' folder
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_output_folder = f"output/{mask}_{timestamp}"
    if not os.path.exists(unique_output_folder):
        os.makedirs(unique_output_folder)

    # Loop through each .png file in the folder and apply the overlay
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            icon_path = os.path.join(folder_path, filename)
            output_path = os.path.join(unique_output_folder, filename)
            overlay_path = os.path.join(mask_folder_path, mask)
            overlay_images(icon_path, overlay_path, output_path, transparency)

if chosen_mask.upper() == "ALL":
    for mask in available_masks:
        process_mask(mask)
else:
    process_mask(chosen_mask)


=============================== </1.py> ========================================

Produced:

==============================================================

### Code Snippet Documentation: Overlay Images

**File:** 1.py

**Description:**
This script overlays images with transparent overlays. It allows users to choose an overlay from a folder and apply it to a set of images in another folder. Users can adjust the transparency of the overlay.

#### Usage:
1. Place the images you want to overlay in a folder named "png".
2. Place the overlays (masks) you want to use in a folder named "mask" as `.png` files.
3. Run the script.
4. The script will list the available overlays (masks) in the "mask" folder.
5. Enter the filename of the overlay (mask) you want to use or type "ALL" for bulk processing.
6. Enter the transparency value (0-100) for the overlay.
7. The script will create a unique output folder for each process inside the "output" folder.
8. Images with the overlay applied will be saved in the respective output folders.

#### Functionality:
The script performs the following tasks:
1. Imports necessary modules: `PIL` from `Pillow`, `os`, and `datetime`.
2. Defines a function `overlay_images` to overlay two images.
   - Opens the icon and overlay images as RGBA.
   - Creates a new RGBA image with the size of the icon image.
   - Iterates over each pixel in the icon image.
   - If the alpha value of the icon pixel is greater than 0, a new alpha value is calculated for the overlay pixel.
   - Calculates a new pixel value using a combination of the icon and overlay pixels.
   - Puts the new pixel in the output image at the corresponding location.
   - Saves the output image.
3. Lists the available overlays (masks) in the "mask" folder.
4. Asks the user to choose an overlay (mask) or enter "ALL" for bulk processing.
5. Asks the user to enter the transparency value (0-100).
6. Defines a function `process_mask` to apply the overlay to each image in the "png" folder.
   - Creates a unique output folder for each process inside the "output" folder.
   - Loops through each `.png` file in the "png" folder.
   - Calls the `overlay_images` function to overlay the icon image with the chosen mask.
   - Saves the resulting image in the output folder.
7. If the user chose "ALL", the script calls the `process_mask` function for each overlay.
8. Otherwise, the script calls the `process_mask` function for the chosen overlay.

#### Notes:
- Make sure to place the images you want to overlay in a folder named "png" and the overlays (masks) in a folder named "mask" as `.png` files.
- The output images with the overlays will be saved in unique folders inside the "output" folder. Each output folder will have a name indicating the chosen mask and the timestamp of the process.

==============================================================
