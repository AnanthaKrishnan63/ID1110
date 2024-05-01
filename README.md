## X-Ray Image Classification for Brain Tumor and Pneumonia Detection

This project aims to develop a web application that uses deep learning techniques to classify X-ray images and detect the presence of brain tumors or pneumonia. The application is built using a Convolutional Neural Network (CNN) model trained on a large dataset of X-ray images.

## Project Overview

The primary goal of this project is to provide a user-friendly web interface that allows users to upload X-ray images and receive accurate predictions on whether the images indicate the presence of brain tumors, pneumonia, or neither condition. The web application is designed to assist healthcare professionals and individuals in obtaining quick and reliable diagnoses, potentially leading to timely and effective treatment.

## Features

Image Upload: Users can upload X-ray images in common formats (e.g., JPG, PNG) through the web interface.
Image Classification: The trained CNN model analyzes the uploaded X-ray images and classifies them into three categories: brain tumor, pneumonia, or healthy.
Prediction Results: The application displays the classification results, indicating the predicted condition or a negative result for both conditions.
User-friendly Interface: The web application provides a clean and intuitive interface for seamless user interaction.

## Usage

1. Once the web application is running, navigate to the provided URL in your web browser.
2. Select the model
3. Click the "Upload Image" button and select the X-ray image you want to analyze.
4. After uploading the image, the application will process it and display the classification results.
5. The results will indicate whether the image is classified as showing a  glioma tumor,meningioma tumor,no tumor,pituitary tumor, pneumonia, or no pneumonia depending on what model you choose.

## Dataset

The CNN model was trained on the following datasets:

- **Brain Tumor Dataset**: https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri,https://www.kaggle.com/datasets/thomasdubail/brain-tumors-256x256
- **Pneumonia Dataset**: https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia,https://huggingface.co/datasets/HippoLite/PneumoniaHippo

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


## Acknowledgments

- Tensorflow,Numpy,Keras,Pillow,Flask,Werkzeug
  

