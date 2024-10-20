# -*- coding: utf-8 -*-
"""project-alagar.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ns6uVGYSs6RiPjTR4dqhPcXkKR5j_dG4
"""

!nvidia-smi

!git clone https://github.com/AlexeyAB/darknet.git

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="PMqWkCWwzu25tXIe90bo")
project = rf.workspace("data-zygje").project("sajam")
version = project.version(10)
dataset = version.download("darknet")

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/sajam-10

!mv /content/sajam-10/valid/*.txt /content/sajam-10/algarrobot-veeran

import glob, os


dataset_path = '/content/sajamhh/algarrobot-veeran'

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(dataset_path, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test+1:
        counter = 1
        file_test.write(dataset_path + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(dataset_path + "/" + title + '.jpg' + "\n")
        counter = counter + 1

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/darknet

!wget https://master.dl.sourceforge.net/project/darknet-yolo.mirror/yolov4/yolov7-tiny.weights?viasf=1

!ls

!make

!./darknet

def update_yolo_config(cfg_file_path, num_classes):
    # Calculate the number of filters based on the formula
    num_anchors = 9
    filters = (num_classes + 5) * num_anchors

    # Read the config file
    with open(cfg_file_path, 'r') as file:
        lines = file.readlines()

    # Create an iterator for the lines
    lines_iter = iter(lines)

    with open(cfg_file_path, 'w') as file:
        for line in lines_iter:
            # Update filters for convolutional layers before each YOLO layer
            if line.startswith("[convolutional]"):
                # Get the next line to check the number of filters
                next_line = next(lines_iter, None)
                if next_line and "filters=" in next_line:
                    # Update the filters
                    line = next_line
                    line = f"filters={filters}\n"
                # Write the updated line back to the file
                file.write(line)
                # Write the updated filters line back to the file
                file.write(f"filters={filters}\n")
                continue  # Skip to the next iteration

            # Update classes in YOLO layers
            if line.startswith("[yolo]"):
                # Write the YOLO header back to the file
                file.write(line)
                # Look for the classes line and update it
                for _ in range(8):  # Skip the first few lines after [yolo]
                    next_line = next(lines_iter, None)
                    if next_line and "classes=" in next_line:
                        file.write(f"classes={num_classes}\n")
                    else:
                        file.write(next_line)
                continue

            # Write the line back to the file
            file.write(line)

# Specify the path to your configuration file and the number of classes
cfg_file_path = "/content/darknet/cfg/yolov7-tiny.cfg"
num_classes = 2

update_yolo_config(cfg_file_path, num_classes)

print(f"Updated {cfg_file_path} for {num_classes} classes with appropriate filters.")

!wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights

!./darknet detector train /content/darknet/cfg/coco.data  /content/darknet/cfg/yolov4-tiny.cfg  /content/darknet/yolov4-tiny.weights

!make

!./darknet