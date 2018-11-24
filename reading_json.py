import os
import shutil
import json
import sys


# FINISH TESTING & DEBUGGING
#
#

def main():

    # getting cmd_line_args in format:
    # "python3 reading_json.py file.json img_dir output_dir"
    cmd_line_args = sys.argv
    print(cmd_line_args)
    num_args = len(cmd_line_args)

    # check for correct num of args (expecting 4 args: reading_json.py, file.json, img dir, output_dir)
    if (num_args != 4):
        # caller has wrong num of args
        print("ERR: Arguments entered incorrectly. Please call with the command: 'python3 reading_json.py file.json img_dir output_dir' ")
        return False

    print("copying images from " + cmd_line_args[2])

    # read input JSON file
    j_file = (open(cmd_line_args[1])).read()

    # parse JSON into a dictionary:
    json_dict = json.loads(j_file)

    # get images

    imgs = []
    for panel in json_dict["damaged"]:
        imgs += [ panel['filename'] ]

    # source file and destination file locations
    src = cmd_line_args[2]
    dest = cmd_line_args[3]

    # getting image file locations and moving them to a destination folder
    #src_files = os.listdir(src)
    for file_name in imgs:
        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name, dest)

    print("Success!")

    return True


if main()==False:
    sys.exit(-1) # so the caller of your program knows that your program didnt exit properly
