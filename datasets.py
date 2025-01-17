# ========================================================
#             Media and Cognition
#             Homework 2 Convolutional Neural Network
#             datasets.py - Define the data loader for the traffic sign classification dataset
#             Student ID:
#             Name:
#             Tsinghua University
#             (C) Copyright 2024
# ========================================================

import os

import numpy as np
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder


def get_data_loader(
    data_root, mode, image_size, batch_size, num_workers=0, augment=False
):
    """
    Get the data loader for the specified dataset and mode.
    :param data_root: the root directory of the whole dataset
    :param mode: the mode of the dataset, which can be 'train', 'val', or 'test'
    :param image_size: the target image size for resizing
    :param batch_size: the batch size
    :param num_workers: the number of workers for loading data in multiple processes
    :param augment: whether to use data augmentation
    :return: a data loader
    """ 
    # >>> TODO 1.1: Define the data transform.
    # You should use the `transforms` module from `torchvision`.
    # Docs: https://pytorch.org/vision/stable/transforms.html
    # You can create a list of shared transforms among the training, validation, and testing datasets, and
    # modify the list according to the mode and the `augment` parameter later.
    # The shared transforms include:
    #   (1) resize the images to `image_size`,
    #   (2) convert the images to PyTorch tensors
    #   (3) normalize the pixel values to [-1, 1]
    data_transforms = [
        transforms.Resize(image_size),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),

    ]

    # You should insert some data augmentation techniques to `data_transforms` when `augment` is True
    # for the training dataset.
    # Consider what is an appropriate data augmentation technique for traffic sign classification.
    if mode == "train" and augment:

        data_transforms.extend([
        transforms.RandomRotation(15),      # 随机旋转 (-15, 15) 度
        #transforms.ColorJitter(saturation=0.0000001),  # 随机调整亮度、对比度和饱和度
        transforms.RandomResizedCrop(image_size, scale=(0.9, 1.0), ratio=(0.9, 1.2)),   # 随机裁剪和缩放
    ])  # TODO
        
# 
    # Else, the `data_transforms` should be left unchanged
    # <<< TODO 1.1
    # Use `transforms.Compose` to compose the list of transforms into a single transform
    data_transforms = transforms.Compose(data_transforms)

    # >>> TODO 1.2: Define the dataset.
    # You should build the path to the selected dataset according to the `mode` parameter,
    # and use the `ImageFolder` class from `torchvision.datasets` to load the datasets.
    # Docs: https://pytorch.org/vision/stable/generated/torchvision.datasets.ImageFolder.html
    # The `ImageFolder` class takes in the path to the dataset and the transform to apply to the images.
    # The `ImageFolder` class will automatically load the images and labels for you.
    # The dataset should be loaded from the directory `data_root/mode`.
    # The `ImageFolder` class will automatically load the images and labels for you.
    # The dataset should be loaded from the directory `data_root/mode`.
    dataset = ImageFolder(
        os.path.join(data_root, mode),
        transform=data_transforms,
    )
    # <<< TODO 1.2


    # >>> TODO 1.3: Define the data loader.
    # You should set the `shuffle` parameter to `True` when `mode=='train'`, and `False` otherwise.
    loader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=mode == "train",
        num_workers=num_workers,
    )
    # <<< TODO 1.3

    return loader
