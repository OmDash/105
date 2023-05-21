import os
import cv2

path = "/Users/omdash/Desktop/105/PRO-C105-Project-Images-main/Images"  # Replace with the actual path to the Images folder

Images = []

for file in os.listdir(path):
    name, extension = os.path.splitext(file)
    if extension.lower() in ['.jpg', '.jpeg', '.png']:  # Replace with the desired image extensions
        file_name = path + "/" + file
        print(file_name)  # Check if filenames are formed correctly
        Images.append(file_name)

count = len(Images)

frame = cv2.imread(Images[0])
width, height, channels = frame.shape
size = (width, height)

print(size)  # Check the result

out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count):
    image = cv2.imread(Images[i])
    out.write(image)

print("Done")
