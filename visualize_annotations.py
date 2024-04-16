import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def mask_to_rgba(mask, color="red"):
    MASK_COLORS = ["red", "green", "blue", "yellow", "magenta", "cyan"]
    assert color in MASK_COLORS
    assert mask.ndim == 3 or mask.ndim == 2

    h = mask.shape[0]
    w = mask.shape[1]
    zeros = np.zeros((h, w))
    ones = mask.reshape(h, w)
    if color == "red":
        return np.stack((ones, zeros, zeros, ones), axis=-1)
    elif color == "green":
        return np.stack((zeros, ones, zeros, ones), axis=-1)
    elif color == "blue":
        return np.stack((zeros, zeros, ones, ones), axis=-1)
    elif color == "yellow":
        return np.stack((ones, ones, zeros, ones), axis=-1)
    elif color == "magenta":
        return np.stack((ones, zeros, ones, ones), axis=-1)
    elif color == "cyan":
        return np.stack((zeros, ones, ones, ones), axis=-1)


# Visualize the breast and dense tissue segmentation
def visualize_gt_annotations(data_path, file_name):

    image = Image.open(os.path.join(data_path, 'images', file_name))

    breast_mask = Image.open(os.path.join(data_path, 'breast_masks', file_name)).convert('L')
    breast_mask = np.asarray(breast_mask)
    
    dense_mask = Image.open(os.path.join(data_path, 'dense_masks', file_name)).convert('L')
    dense_mask = np.asarray(dense_mask)
    
    fig, axes = plt.subplots(1, 2, figsize=(20, 15), squeeze=False)

    axes[0, 0].set_title('Original image', fontsize=25)
    axes[0, 1].set_title("Breast and dense tissue segmentation", fontsize=25)

    axes[0, 0].imshow(image, cmap='gray')
    axes[0, 0].set_axis_off()

    axes[0, 1].imshow(image, cmap='gray')
    axes[0, 1].imshow(mask_to_rgba(breast_mask, color='red'), cmap='gray', alpha=0.2)
    axes[0, 1].imshow(mask_to_rgba(dense_mask, color='green'), cmap='gray', alpha=0.5)
    axes[0, 1].set_axis_off()


visualize_gt_annotations(data_path=r'data/train',file_name='0a20ec2661573dff6738ff5498faaece.jpg' )
