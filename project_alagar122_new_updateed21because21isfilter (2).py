# -*- coding: utf-8 -*-
"""project_alagar122-new-updateed21because21isfilter.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GQXGMDxqn-8G8b9NL-eT1_rEqPw5Lk-Q
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

!mv /content/sajam-10/valid/*.jpg /content/alagar-bot-veeran



import glob, os


dataset_path = '/content/alagar-bot-veeran'

# Percentage of images to be used for the test set
percentage_test = 12;

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
                # Write the convolutional header back to the file
                file.write(line)

                # Get the next line to check the number of filters
                next_line = next(lines_iter, None)
                if next_line and "filters=" in next_line:
                    # Update the filters
                    next_line = f"filters={filters}\n"

                # Write the updated filters line back to the file
                file.write(next_line)

                # Continue writing the rest of the convolutional layer settings
                for _ in range(3):  # Assuming there are three additional settings per convolutional layer
                    file.write(next(lines_iter))

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
            # Update max_batches, steps, and scales
            if line.startswith("max_batches="):
                file.write("max_batches=4000\n")
                continue

            if line.startswith("steps="):
                file.write("steps=500,1000,2000,3000\n")
                continue

            if line.startswith("scales="):
                file.write("scales=0.1,0.1,0.1,0.1\n")  # Adjust this based on your needs
                continue

            # Update filters for convolutional layers before each YOLO layer
            if line.startswith("[convolutional]"):
                # Write the convolutional header back to the file
                file.write(line)

                # Get the next line to check the number of filters
                next_line = next(lines_iter, None)
                if next_line and "filters=" in next_line:
                    # Update the filters
                    next_line = f"filters={filters}\n"

                # Write the updated filters line back to the file
                file.write(next_line)

                # Continue writing the rest of the convolutional layer settings
                for _ in range(3):  # Assuming there are three additional settings per convolutional layer
                    file.write(next(lines_iter))

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

def update_yolo_config(cfg_file_path, num_classes):
    # Filter எண்ணிக்கையை கணக்கிடும் (filters calculation)
    num_anchors = 9
    filters = (num_classes + 5) * num_anchors  # filters = (num_classes + 5) * num_anchors

    # config கோப்பைப் படிக்கவும் (Read the config file)
    with open(cfg_file_path, 'r') as file:
        lines = file.readlines()

    # வரிகளுக்கான итераட்டர் உருவாக்கவும் (Create an iterator for the lines)
    lines_iter = iter(lines)

    with open(cfg_file_path, 'w') as file:
        for line in lines_iter:
            # max_batches, steps, மற்றும் scales இனைப் புதுப்பிக்கவும் (Update max_batches, steps, and scales)
            if line.startswith("max_batches="):
                file.write("max_batches=4000\n")  # Max Batches: 4000
                continue

            if line.startswith("steps="):
                file.write("steps=500,1000,2000,3000\n")  # Steps: 500,1000,2000,3000
                continue

            if line.startswith("scales="):
                file.write("scales=0.1,0.1,0.1,0.1\n")  # Scales: 0.1,0.1,0.1,0.1
                continue

            # convolutional அடுக்குகளில் filters ஐப் புதுப்பிக்கவும் (Update filters in convolutional layers)
            if line.startswith("[convolutional]"):
                file.write(line)  # convolutional header-ஐ மீண்டும் எழுதவும்

                next_line = next(lines_iter, None)
                if next_line and "filters=" in next_line:
                    # filters=13 ஐ சரிபார்க்கவும் (Check for filters=13)
                    if "filters=13" in next_line:
                        next_line = f"filters=13\n"  # filters=13 ஐ உள்ளடக்கவும்
                    else:
                        next_line = f"filters={filters}\n"  # மற்ற filters ஐ புதுப்பிக்கவும்

                file.write(next_line)  # புதுப்பிக்கப்பட்ட filters ஐ எழுதவும்

                # convolutional அடுக்குகளில் உள்ள பிற கட்டுப்பாடுகளை தொடருங்கள் (Continue writing other settings)
                for _ in range(3):  # இங்கு 3 என்று எடுத்துக்கொள்கிறோம்
                    file.write(next(lines_iter))

                continue  # அடுத்த iterationக்கு செல்லவும்

            # YOLO அடுக்குகளில் classes ஐப் புதுப்பிக்கவும் (Update classes in YOLO layers)
            if line.startswith("[yolo]"):
                file.write(line)  # YOLO header-ஐ மீண்டும் எழுதவும்

                for _ in range(8):  # YOLOக்கு பிறகு சில வரிகளை தவிர்க்கவும்
                    next_line = next(lines_iter, None)
                    if next_line and "classes=" in next_line:
                        file.write(f"classes={num_classes}\n")  # classes ஐப் புதுப்பிக்கவும்
                    else:
                        file.write(next_line)  # பிற வரிகளை எழுதவும்
                continue

            # கோப்பில் வரியை எழுதவும் (Write the line back to the file)
            file.write(line)

# உங்கள் configuration கோப்பிற்கு மற்றும் வகுப்புகளின் எண்ணிக்கைக்கு பாதையை குறிப்பிட்டு (Specify the path to your configuration file and the number of classes)
cfg_file_path = "/content/darknet/cfg/yolov7-tiny.cfg"
num_classes = 2

update_yolo_config(cfg_file_path, num_classes)

print(f"Updated {cfg_file_path} for {num_classes} classes with appropriate filters.")

!wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov3-tiny.weights

!./darknet detector train /content/darknet/cfg/coco.data  /content/darknet/cfg/yolov7-tiny.cfg  /content/darknet/yolov7-tiny.weights

!./darknet detector map /content/darknet/cfg/coco.data /content/darknet/cfg/yolov7-tiny.cfg /content/darknet/backup/yolov7-tiny_final.weights



from google.colab import drive
drive.mount('/content/drive')

!mv  /content/darknet/bacckup /content/drive/MyDrive/atomic-model-in-indumathi

!make

!./darknet