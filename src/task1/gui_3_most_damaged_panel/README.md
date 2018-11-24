GUI to Identify 3-most damaged panels
---
# Description
This is a python script that takes in a json file containing the damaged files and the filenames of the relevant images. It then parses the json and moves the images into a folder specified by the user. These images can then be analyzed manually or by using a GUI to identify the 3 most damaged panels.

# Prerequisites
- Python 3

# Usage
The command line arguments are (1) the path of the json file, (2) the path of the folder directory containing the images, and (3) the path of the destination folder. The format is `python3 reading_json.py file.json img_dir output_dir`

Note: The input json file should contain the filenames (ex. `img_0124.jpg`). 

sample usage:
`python3 img_filtering_from_json.py input.json /Users/Sean/GitHub/vision_201819/gui_3_most_damaged_panel/Images /Users/Sean/GitHub/vision_201819/gui_3_most_damaged_panel/GUI_Processing`
