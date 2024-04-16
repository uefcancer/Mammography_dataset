import os
from PIL import Image, ImageDraw
import numpy as np
import json
import tqdm
import matplotlib.pyplot as plt


def prepareMask(width, height, segment):
    # width = 1024
    # height = 1024

    mask = Image.new('L', (width, height), 0)
    # draw the mask
    ImageDraw.Draw(mask).polygon(segment, outline=1, fill=1)
    # convert to numpy array
    mask = np.array(mask).astype(bool)

    return mask


def generateMask(annotation_file, binary_masks_path):
    with open(annotation_file, 'r') as file:
        data = json.load(file)

    print('[INFO] Loaded annotations in  coco format....')

    assert len(data['images']) == len(data['annotations'])

    count = 0

    for i in tqdm.tqdm(range(len(data['annotations']))):
        segmentation = data['annotations'][i]['segmentation']
        file_name = data['images'][i]['file_name']
        width = data['images'][i]['width']
        height = data['images'][i]['height']

        print(file_name)

        mask = prepareMask(width, height, segmentation)
        #cv2.imwrite(os.path.join(binary_masks_path,file_name), mask)
        plt.imsave(os.path.join(binary_masks_path, file_name), mask, cmap='gray')
        count += i

    print('[INFO] Sucessfully generated {} binary masks'.format(count))


#annotation_files = os.listdir('data/annotations')

#for json_file in tqdm.tqdm(annotation_files):
#    generateMask(os.path.join('mias_data/annotations', json_file), 'data/masks')


generateMask('1_5.json', 'masks/')


