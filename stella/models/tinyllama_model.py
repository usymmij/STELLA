import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, ViTImageProcessor, ViTModel
from PIL import Image
import requests

# for my understanding:
# this script extracts image features using the vision transformer (ViT) model and passes those features to TinyLlama for generating text-based outputs
# it demonstrates how visual data can be processed into text representations for use in language models

# step 1: load ViT model and feature extractor

# using huggingface's ViT model to extract image features
vit_model_name = "google/vit-base-patch16-224-in21k"
vit_processor = ViTImageProcessor.from_pretrained(vit_model_name)
vit_model = ViTModel.from_pretrained(vit_model_name)

# step 2: load TinyLlama model and tokenizer

# using TinyLlama to process visual features and generate text-based outputs
llama_model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(llama_model_name)
llama_model = AutoModelForCausalLM.from_pretrained(llama_model_name)

# step 3: load a test image

# fetching an image from an external URL
image_url = "https://static01.nyt.com/images/2021/09/14/science/07CAT-STRIPES/07CAT-STRIPES-mediumSquareAt3X-v2.jpg"
image = Image.open(requests.get(image_url, stream=True).raw)

# step 4: preprocess the image using ViT image processor

# converting the image into a tensor representation that the ViT model can understand
inputs = vit_processor(images=image, return_tensors="pt")

# step 5: run ViT inference to extract image features

# disabling gradient calculations since we are only doing inference
with torch.no_grad():
    vit_outputs = vit_model(**inputs)

# step 6: reduce feature size using mean pooling

# taking the mean of all feature vectors to get a single compact representation
image_features = vit_outputs.last_hidden_state.mean(dim=1)  # Shape: [1, 768] → [1, 1]

# step 7: convert image features into text-like format for TinyLlama

# converting the numerical features into a string representation so TinyLlama can process them
feature_text = "Average image feature: " + " ".join(map(str, image_features.flatten().tolist()))

# step 8: tokenize the feature text and pass it to TinyLlama

# converting the text into tokenized format so it can be fed into the language model
inputs = tokenizer(feature_text, return_tensors="pt", truncation=True, max_length=512)

# step 9: generate a response from TinyLlama

# generating text-based output based on the processed image features
with torch.no_grad():
    outputs = llama_model.generate(**inputs, max_new_tokens=50)

# step 10: decode and display the output

# converting tokenized output back into readable text
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("TinyLlama Output (Based on ViT Features):", response)

torch.save(response, "models/outputs/tinyllama_response.txt")
print("TinyLlama output saved as tinyllama_response.txt")

# this program should output a text-based response from TinyLlama
# based on the image features extracted by ViT