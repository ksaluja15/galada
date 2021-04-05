---
layout: post
title:  Detection/Classification metrics
date:   2020-12-22 16:03:00 +0300
image:  det_cov.png
tags:   Metrics F1 AP
usemathjax: true
---

# Problem Statement

 1. Once we've trained multiple detection/classification models, how to choose the best model ?
 2. Once we've chosen the best model, how to choose the optimum operating point (the best threshold) ?

# Solution

There are two metrics which can help us here. If you've come across terms like AP, mAP and F-1 score in research papers, 
these are precisely the metrics that help us with the above mentioned problems. Let's begin by defining precision and recall, 
which are pre-requisities to understanding other metrics.

### Precision and Recall

Let's assume that we've trained a car detector.

{% highlight markdown %}
Precision is the ratio of true positives to total number of predictions. 
For every N predictions made by this detector on an image, 
this metric tells us what percentage of those detections are actually cars.
{% endhighlight %}

$$ Precision = \frac{TP}{TP+FP} $$

{% highlight markdown %}
Recall is the ratio of correct predictions to the number of ground truth 
labels available for the class. Assuming that we have X cars in an image, 
this metric tells us what percentage of those X cars were detected correctly.
{% endhighlight %}

$$ Recall = \frac{TP}{TP+FN} $$


### Average Precision (AP) 

{% highlight markdown %}
Average Precision is the area under the Precision - Recall curve.
{% endhighlight %}
$$ AP = \int_0^1 P(r) \,dr$$

![]({{site.baseurl}}/img/pr.png)

We can use the standard sklearn package to compute the AUC (area under the curve), 
or we can approximate the area, as shown in the figure above.

Mean Average Precision (mAP) is the mean of AP for all classes.

$$ mAP = \sum_0^N \frac{AP(i)}{N}\$$

{% highlight markdown %}
Given N different models, the optimal model choice in *most* situations 
is the one with the highest mAP
{% endhighlight %}

### F1 score

{% highlight markdown %}
F1 score is described as the harmonic mean of precision and recall. 
If we were to calculate the F1 score for every point on the PR curve, 
the point with the highest F1 score is generally chosen as an operating point.
{% endhighlight %}

$$ F1 = \frac{2*P*R}{P+R}\$$

![]({{site.baseurl}}/img/ft.png)

This is also known as the Equal Error Rate (EER) point.


## Code

{% highlight markdown %}
    
    import matplotlib.pyplot as plt
    import numpy as np
    plt.style.use('dark_background')
    
    p = [1, 1, 0.9, 0.8, 0.7, 0.6, 0.4, 0.2, 0.01]
    r = [0, 0.2, 0.4, 0.5, 0.6, 0.66, 0.80, 0.90, 0.99]
    t = [0, 0.2, 0.3, 0.5, 0.6, 0.7, 0.8, 0.85, 0.99]
    
    plt.plot(r, p)
    # plt.axvline(x=0.6, ymin=0, ymax=1, color='r')
    plt.ylabel('Precision')
    plt.xlabel('Recall')
    plt.savefig('pr.png', dpi=1000)
    
    f=[]
    for i in range(len(p)):
      f1 = 2*p[i]*r[i] / (p[i]+r[i] + 1.e-7)
      f.append(f1)
    
    plt.plot(t, f)
    plt.axvline(x=0.6, ymin=0, ymax=1, color='r')
    plt.xlabel('Threshold')
    plt.ylabel('F1 Score')
    plt.savefig('ft.png', dpi=1000)
{% endhighlight %}


## Quick Takeaways

1. For choosing the best model from multiple variants (differing in architecture, 
augmentation or training methodology), use mAP
2. For choosing the best operating threshold, use F1 score.
