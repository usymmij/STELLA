# import torch
# from transformers import ViTForImageClassification, ViTFeatureExtractor
# from PIL import Image
# import requests

# # Load pre-trained Vision Transformer model and feature extractor
# model_name = "google/vit-base-patch16-224-in21k"  # Example of a pre-trained ViT model
# model = ViTForImageClassification.from_pretrained(model_name)
# feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)

# # Load and preprocess an image
# url = "https://www.gstatic.com/webp/gallery/1.jpg"

# image = Image.open(requests.get(url, stream=True).raw)

# # Preprocess the image
# inputs = feature_extractor(images=image, return_tensors="pt")

# # Perform inference
# with torch.no_grad():
#     outputs = model(**inputs)

# # Get predictions
# logits = outputs.logits
# predicted_class_idx = logits.argmax(-1).item()

# # Print the predicted class
# print(f"Predicted class: {model.config.id2label[predicted_class_idx]}")

# import torch
# from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForImageClassification, AutoFeatureExtractor
# from PIL import Image

# # Load the pre-trained Vision Transformer (ViT) and LLaMA models
# vit_model_name = "google/vit-base-patch16-224-in21k"
# llama_model_name = "meta-llama/Llama-2-7b-chat-hf"

# vit_model = AutoModelForImageClassification.from_pretrained(vit_model_name)
# vit_extractor = AutoFeatureExtractor.from_pretrained(vit_model_name)

# llama_model = AutoModelForCausalLM.from_pretrained(llama_model_name)
# llama_tokenizer = AutoTokenizer.from_pretrained(llama_model_name)


# # Example image loading and processing for ViT
# img_path = "https://www.gstatic.com/webp/gallery/1.jpg"
# img = Image.open(requests.get(img_path, stream=True).raw)
# inputs = vit_extractor(img, return_tensors="pt")

# # Get features from ViT
# vit_outputs = vit_model(**inputs)
# vit_features = vit_outputs.logits  # This is the image's representation

# # Flatten the image features to make them compatible with the LLaMA input (as a "text")
# vit_features = vit_features.view(vit_features.size(0), -1)  # Flatten
# vit_features = vit_features.squeeze().cpu().detach().numpy()  # Convert to numpy for easy handling

# # Convert image features to text or directly pass them as input to LLaMA
# vit_features_text = f"Image features: {vit_features[:100]}"  # Only take first 100 values for brevity

# # Encode the features as input for LLaMA
# inputs_llama = llama_tokenizer(vit_features_text, return_tensors="pt")

# # Generate text with LLaMA
# outputs_llama = llama_model.generate(inputs_llama["input_ids"], max_length=100)
# generated_text = llama_tokenizer.decode(outputs_llama[0], skip_special_tokens=True)

# # Display the generated text based on the image features
# print(f"Generated Text: {generated_text}")



from transformers import AutoTokenizer, AutoModelForImageClassification
from PIL import Image
import torch
import requests

# Load the pre-trained ViT model (ensure you are using the correct model identifier)
model_name = "google/vit-base-patch16-224-in21k"  # Example ViT model for image classification
model = AutoModelForImageClassification.from_pretrained(model_name)

# Prepare the image tokenizer
from transformers import ViTImageProcessor
processor = ViTImageProcessor.from_pretrained(model_name)

# Load an image (make sure to replace this with the path to your own image)

url = "https://www.gstatic.com/webp/gallery/1.jpg"

image = Image.open(requests.get(url, stream=True).raw)

# Preprocess the image (resize and normalize for ViT)
inputs = processor(images=image, return_tensors="pt")

# Get predictions
with torch.no_grad():
    outputs = model(**inputs)
    print(outputs)

# Get the predicted class
logits = outputs.logits
predicted_class_idx = torch.argmax(logits, dim=-1).item()

# Get the label (if the model has a label map)
labels = model.config.id2label
predicted_class_label = labels[predicted_class_idx]


print(f"Predicted class: {predicted_class_label}")



#16 or 32
