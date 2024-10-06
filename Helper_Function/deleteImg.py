import os

# Directories for images and labels
image_dir = './Hand Keypoint Dataset/images/train'
label_dir = './Hand Keypoint Dataset/labels/train'

# Get the list of image files (assuming the images have a .jpg or .png extension)
image_files = set([f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png'))])

# Get the list of label files (assuming the labels have a .txt extension)
label_files = set([f.replace('.txt', '') for f in os.listdir(label_dir) if f.endswith('.txt')])

# Loop through the images and delete the ones without corresponding label files
for image_file in image_files:
    image_name = os.path.splitext(image_file)[0]  # Get the image name without the extension
    if image_name not in label_files:
        image_path = os.path.join(image_dir, image_file)
        os.remove(image_path)  # Delete the image
        print(f'Deleted: {image_path}')

print("Cleanup complete. Extra images removed.")
