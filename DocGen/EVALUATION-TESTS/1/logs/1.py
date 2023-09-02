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

