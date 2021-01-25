---
layout: post
title:  Semantic Segmentation - DeepLab V3+ 
date:   2021-01-23 16:03:00 +0300
image:  dark_city.jpg
tags:   segmentation deeplab xception aspp depthwise separable encoder decoder
usemathjax: true
---

# Semantic Segmentation
Semantic segmentation involves partitioning/marking regions in the image 
belonging to different objects/classes. Deep learning methods have made a remarkable 
improvement in this field within the past few years. This short article summarises
DeepLab V3+, an elegant extension of DeepLab v3 proposed by the same authors (Chen et al.).


![]({{site.baseurl}}/img/seg.png)
<p style="text-align:center"> Examples of semantic segmentation. Source: <a href="#ref">(1)</a></p>


# Intuition
![]({{site.baseurl}}/img/intuition.png)
<p style="text-align:center"> (a) ASPP style architecture (b) Encoder Decoder style architecture 
(c) Proposed architecture. Source: <a href="#ref">(1)</a></p>

Previously, ASPP (Atrous Spatial Pyramid Pooling) has been used to extract rich multi scale features from images.
The authors of deeplab v3+ try to combine the ASPP module with the good old encoder-decoder architecture 
with skip connections, thereby providing better details in predictions.

## Architecture

![]({{site.baseurl}}/img/seg_arch.png)
<p style="text-align:center"> DeepLab v3+ architecture. Source: <a href="#ref">(1)</a></p>

Here are the key features of this architecture:
* Atrous Depthwise Convolution : The depthwise conv has an added dilation to make it atrous
* ASPP style encoder from DeepLab V3 + UNet style decoder with skip connections
* Modified Xception network as the backbone: This can be replaced by any backbone; HRNet seems 
to be widely used these days

## Results

![]({{site.baseurl}}/img/seg_res.png)
<p style="text-align:center"> The results show different backbones with Bilinear Upsampling(BU) vs a decoder.
 Source: <a href="#ref">(1)</a></p>



## References
<a name="ref"></a>
1. (https://arxiv.org/pdf/1802.02611.pdf) Encoder-Decoder with Atrous Separable Convolution for 
  Semantic Image Segmentation
2. (https://arxiv.org/abs/1610.02357) Xception: Deep Learning with Depthwise Separable Convolutions
3. (https://arxiv.org/pdf/1606.00915v2.pdf) DeepLab: Semantic Image Segmentation with
   Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs
4. (https://arxiv.org/abs/1801.04381) MobileNetV2: Inverted Residuals and Linear Bottlenecks