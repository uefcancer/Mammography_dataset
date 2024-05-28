# Mammogram density assessment dataset

## Overview
This repository presents a new dataset designed to advance research in automated breast density estimation, a critical component in mammogram interpretation. Mammography, a low-dose X-ray technique for breast cancer screening, is significantly influenced by breast density. Dense breast tissue appears white on mammograms, which can obscure tumors and complicate diagnosis. Our dataset, derived from the public VinDr-Mammo dataset, includes 745 mammogram images divided into training and test sets, along with expert radiologist annotations for both the entire breast and dense tissue regions.

Researchers can utilize this dataset for various purposes, including:

Training deep learning models for automated breast density analysis
Refining segmentation methods for accurate delineation of breast tissue
Benchmarking existing and novel breast density estimation algorithms
This resource aims to enhance breast cancer screening through improvements in automated breast density analysis.

## Data Description
The dataset comprises mammogram images and corresponding segmentation masks for dense tissue and breast areas. All annotations were performed by an expert radiologist. The data is available in two compressed archives: train.zip and test.zip.

Contents of the Dataset
train.zip
This archive contains three sub-folders:

images: Contains the original mammogram images in JPG format.
breast_masks: Contains the ground truth segmentation masks for the breast area in JPG format.
dense_masks: Contains the ground truth segmentation masks for the dense tissue in JPG format.
All images and their corresponding masks have dimensions of 2800×3518 pixels.

test.zip
This archive contains only the mammogram images for the test set in JPG format. Ground truth information for the test set is not provided in this archive, as it is reserved for the Breast Density Kaggle Challenge. However, the ground truths will eventually be made public in the dataset repository.

File Lists
Two CSV files accompany the compressed archives:

train.csv: Contains information about the training set with two columns:
Filename: Lists the filename of the corresponding image in the images sub-folder of train.zip.
Density: Provides the ground truth continuous breast density value for each mammogram, intended for the breast density estimation task.
test.csv: Contains a single column, Filename, listing the filenames of the images in the test set found within test.zip.

## Usage
Researchers and developers can use this dataset to train and evaluate their models for automated breast density estimation. To get started, download the dataset archives and extract the files. Use the train.csv and test.csv files to understand the structure of the data and to link the images with their corresponding annotations.

## Acknowledgments
We acknowledge the contributions of the expert radiologists who provided the annotations and the creators of the VinDr-Mammo dataset. This dataset is shared to foster advancements in breast cancer screening and to support the community in developing more accurate and reliable breast density estimation methods.

Contact
For any questions or further information, please contact hamid.behravan@uef.fi.

License: CC BY-NC 4.0

For more details on the Breast Density Kaggle Challenge, visit the Kaggle competition page at https://www.kaggle.com/competitions/breast-density-prediction/data. 

Thank you for your interest in our dataset. We look forward to seeing the advancements and innovations that arise from its use.

## Citation
Please cite the following works if you use this dataset:
1. Gudhe, N.R., Behravan, H., Sudah, M., Okuma, H., Vanninen, R., Kosma, V.M. and Mannermaa, A., 2022. Area-based breast percentage density estimation in mammograms using weight-adaptive multitask learning. Scientific reports, 12(1), p.12060.
2. Behravan, H., Gudhe, N.R., Okuma, H., Sudah, M., & Mannermaa, A. (2024). A dataset for mammography images with area-based density values and dense tissue segmentation masks. (Data in Brief)
