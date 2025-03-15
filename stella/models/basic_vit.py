import torch
import torch.nn as nn
from timm.models.vision_transformer import VisionTransformer

class ViT(nn.Module):
    def __init__(self, image_size=336, patch_size=16, embed_dim=768, num_heads=12):
        super(ViT, self).__init__()
        
        self.vit = VisionTransformer(img_size=image_size, patch_size=patch_size, embed_dim=embed_dim, 
                                     depth=12, num_heads=num_heads, mlp_ratio=4.0, num_classes=0)

    def forward(self, img1, img2):
        feat1 = self.vit.forward_features(img1) 
        feat2 = self.vit.forward_features(img2)

        feat1 = feat1[:, 1:, :]
        feat2 = feat2[:, 1:, :]

        patch_embeddings = torch.cat((feat1, feat2), dim=0)

        return patch_embeddings

# model = ViT()
# img1 = torch.randn(4, 3, 336, 336)
# img2 = torch.randn(4, 3, 336, 336)

# output = model(img1, img2)
# print(output.shape)