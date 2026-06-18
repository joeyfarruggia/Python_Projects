#Import necessary libraries
import os
import pandas as pd

#Set the root directory of image dataset
dataset_root = 'C:\\Users\\Joey\\OneDrive\\Documents\\GitHub\\Python_Projects\\CSV_Assignment'

#Initialize an empty DataFrame with columns for image_path and label
image_data = pd.DataFrame(columns=['image_path', 'label'])

#Traverse the dataset directory
for root, dirs, files in os.walk(dataset_root):
    #Iterate over each file in the current directory
    for file in files:
        #Combine the root directory and file name to get the full path of the image
        image_path = os.path.join(root, file)
        #Extract the label from the parent directory name
        label = os.path.basename(root)
        #Create a new DataFrame with the image path and label as values
        row = pd.DataFrame({'image_path': [image_path], 'label': [label]})
        #Concatenate the new row to the existing DataFrame
        image_data = pd.concat([image_data, row], ignore_index=True)
#Save the DataFrame to a CSV file
image_data.to_csv('image_dataset.csv', index=False)
file_path = 'image_dataset.csv'
os.startfile(file_path)
