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
                new_alpha = int((100 - transparency) / 100 * overlay_pixel[3])
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
