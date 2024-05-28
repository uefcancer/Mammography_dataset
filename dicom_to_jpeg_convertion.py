# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:10:07 2022

@author: rajgudhe
"""

import os
import glob
import SimpleITK as sitk
import matplotlib.pyplot as plt
from tqdm import tqdm


def dicom_to_jpeg(dicom_path, image_dir):
    p_id = os.path.split(dicom_path)[0].split('\\')[-1]
    f_id = os.path.splitext(os.path.split(dicom_path)[-1])[0]
    reader = sitk.ImageFileReader()
    try:
        reader.SetFileName(dicom_path)
        data = reader.Execute()
        img = sitk.GetArrayViewFromImage(data)
        dest_path = os.path.join(image_dir, str(p_id))
        os.makedirs(dest_path, exist_ok=True)    
        plt.imsave(os.path.join(dest_path, str(f_id) + '.jpg'), img[0], cmap='gray')
    except:
        pass
    
    
    
    
    
dicoms = glob.glob('dicom/*/*')

for dicom in tqdm(dicoms):
    dicom_to_jpeg(dicom, 'jpeg_images')
    
