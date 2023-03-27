# Developing a Unified Platform for Serving TruX Machine Learning Models

This is my Bachelor project, developed during my internship in collaboration with the Interdisciplinary Centre for Security, Reliability and Trust (SnT) at the University of Luxembourg with the TruX research group. Focusing on the deployment of machine learning models created within TruX, in order to provide a more accessible and user-friendly experience of using these models.

## Abstract

Machine learning models seek to accomplish tasks more efficiently. Several steps are required to finally train and make use of such a model. These steps include data collection and preprocessing, model training, evaluation, and deployment. This project focuses precisely on this last step, namely the deployment of the machine learning model to ensure that end users can easily use it. This project includes a total of four already trained models by researchers working at the TruX research group. Among them, is an Android malware detection model that scans Android applications for the presence of malware to prevent a device from being harmed by a malicious application. Another model is a code classification model that classifies a source code into a label from a set of possible classes. Furthermore, the vulnerability detection model checks to determine whether a source code has vulnerability problems. Finally, the code clone detection model compares two given source codes with each other to verify if they are semantic clones, which means that they essentially serve the same purpose, although having a different syntactic structure. These four models are used on a newly created website built with Streamlit. The website, accessible on the internet, provides interactive interfaces for any user to directly test the considered models by just providing the required inputs (e.g. an APK file for Android malware detection).

## Usage

To use the models, simply navigate to the website https://huggingface.co/spaces/oliveira-lionel/Bachelor-Project-Deployment, where the project has been added. From there, you can select the model you want to test and provide the required inputs.
