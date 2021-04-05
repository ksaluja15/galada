---
layout: post
title:  Designing and shipping an ML Feature
date:   2021-04-03 16:03:00 +0300
image:  design_ml.png
tags:   Dual Two screen monitor hdmi wavlink fresco display link
---

What exactly are we trying to accomplish? Will the new model architecture really be a game-changer? 
How much impact will this new dataset have on the model accuracy? 
These are some questions a typical machine learning team deals with on a daily basis. 
But it is important to not get bogged down by the intricacies, and always go back to the first principles approach. 
With the pace at which new research papers are pouring in, 
it is important for ML/Data/CV Scientists to sometimes take a back seat and think about the overall picture a bit more.

![]({{site.baseurl}}/img/design_ml.png)

If we start off with a tiny open-source dataset and loop through this design cycle, we can establish a pretty solid baseline.
The bulk of the work after this should be focused on the finer aspects of the product, the outliers/corner cases in particular.

## Establishing the goals and use-cases
This is perhaps the most important part of this strategy. It involves working closely with the product managers to 
decide the overarching goal, which dictates the key requirements of the product. Any mistake here can prove to be very 
costly, both from employee retention and a financial standpoint. After all, no one likes to work for managers who keep 
shifting the goal post.

Here are some key components of each strategy. I refrained from going into details for each component here, as it's 
mostly self-explanatory. Instead, I wanted to focus more on the vast breadth of issues here, since the finer details 
vary for each team.

## Data Strategy

1. **Data collection** →Using "off the shelf" datasets or creating a dataset from scratch?
2. **Data Labeling** →Manual or Automatic annotation?
3. **Data Backend** →Storage, Indexing, and Delivery. Usually, AWS S3 is used for storage, while teams tend to build 
   their own layer (typically python-based) for serving the data.
   
## Model Strategy

1. Training Framework → Pytorch or Tensorflow?
2. Training Infrastructure → AWS or self-built GPU rigs or both?
3. "Off the shelf" models for establishing baseline (if available)
4. Exploring the Accuracy / Speed TradeOff → This blog details how EfficientNet does exactly that.
5. Neural architecture search → This blog talks about how NAS can be used in specific cases to greatly reduce the 
   network size while maintaining accuracy

### 4. USB-C ports only
You can use multiple HDMI-> USB-C cables.


This is not an exhaustive list by any means. Hope this helps someone.