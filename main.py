import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

path = 'LungImage_pyfile/'

def extract_images():
    data = np.load(path + 'images_data.npy')

    with open('greyscale.csv', 'r') as f:
        greyscale = f.read().splitlines()

        for index, image in enumerate(data):
            converted_array = []
            for array in image:
                for value in array:
                    value = int(value)
                    for row in greyscale:
                        gs_value, gs_color = row.split(',')
                        if gs_value == str(value):
                            converted_array.append(gs_color)

            # Convert hex color to Image
            converted_array = [x.lstrip('#') for x in converted_array]
            converted_array = [tuple(int(x[i:i+2], 16) for i in (0, 2, 4)) for x in converted_array]

            # Create image
            img = Image.new('RGB', (28, 28))
            img.putdata(converted_array)
            img.save(f'images/image{index}.png')


def extract_labels():
    data = np.load(path + 'labels.npy')
    print(len(data))


def plot():
    path = '/images'

    images = os.listdir(os.curdir + path)

    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle(f'Cancer nodules', fontsize=20)

    for i in range(3):
        k = np.random.randint(0, len(images))
        img = np.array(Image.open(f'.{path}/{images[k]}'))
        ax[i].imshow(img)
        ax[i].axis('off')
    plt.show()



if __name__ == "__main__":
    # extract_images()
    # extract_labels()
    # plot()
    print('Done')