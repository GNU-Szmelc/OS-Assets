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

