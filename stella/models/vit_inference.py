import torch
from transformers import ViTImageProcessor, ViTModel
from PIL import Image
import requests

# this script uses the vision transformer (ViT) model for image classification, extracting image features and generating a tensor representation
# it demonstrates how to preprocess an image, run inference with ViT, and handle the output tensor for further use or analysis

# step 1: load ViT model and feature extractor

# using huggingface's ViT model for image classification
model_name = "google/vit-base-patch16-224-in21k"
processor = ViTImageProcessor.from_pretrained(model_name)
model = ViTModel.from_pretrained(model_name)

# step 2: load a test image

# two images for testing purposes
# some random cat image
#image_url = "https://static01.nyt.com/images/2021/09/14/science/07CAT-STRIPES/07CAT-STRIPES-mediumSquareAt3X-v2.jpg"

# another random cat image
image_url = "https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_3x2.jpg"
image = Image.open(requests.get(image_url, stream=True).raw)

# step 3: preprocess the image using ViT image processor
inputs = processor(images=image, return_tensors="pt")

# step 4: run inference and get output tensor
with torch.no_grad():
    outputs = model(**inputs)

output_tensor = outputs.last_hidden_state

# print the output tensor
print("Output tensor shape:", output_tensor.shape)
print("Output tensor:\n", output_tensor)

# so we can save the output tensor as a pt file in our outputs folder
torch.save(output_tensor, "models/outputs/vit_output.pt")
print("Output tensor saved as vit_output.pt")

# this program should output: Output tensor shape: torch.Size([1, 197, 768])
# 1 represents the batch size, 197 represents the number of patches, and 768 represents the hidden size of the model.
# the batch size is number of images processed in parallel
# the number of patches is the number of patches extracted from the image
# the hidden size is the size of the hidden representation of each patch