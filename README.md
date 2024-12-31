# Image Captioning

This is a simple Streamlit App that performs image captioning using a pretrained model from Hugging Face. The app takes an image as input and generates a caption describing the contents of the image. 

## Features

* Image Upload: Upload an image to the app for caption generation
* Pretrained Model: Uses a pretrained model from Hugging Face to generate captions.
* Instant Results: Get real-time captions as soon as the image is uploaded.

## Demo

Try the app by visiting [app](https://image-caption-generator-hf.streamlit.app).

## Requirements

To run the app locally, some dependencies need to be installed.
* streamlit
* transformers
* torch
* pillow

You can install the dependencies with:
```cmd
pip install -r requirements.txt
```

## Run the app locally

1. Clone the repository
```
git clone https://github.com/SujayMann/Image_Captioning.git
cd Image_Captioning
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Run the app
```
streamlit run app.py
```

## How It Works
1. The app uses a pretrained image captioning model from Hugging Face ([model link](https://huggingface.co/Salesforce/blip-image-captioning-base)).
2. When an image is uploaded, the model processes it and generates a caption.
3. The caption is then displayed below the image.  
