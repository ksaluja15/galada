---
layout: post
title:  2 Screens and 1 HDMI port
date:   2020-12-12 16:03:00 +0300
image:  dual_screen.jpg
tags:   Dual Two screen monitor hdmi wavlink fresco display link
---

I'm surprised that after this long into a lockdown, there aren't many blog posts about how to set up 2 screens with your
laptop(<i>which usually has a single HDMI slot these days</i>). Since I recently set it up, I thought of sharing my literature review. 
Here are some obvious things to try, depending upon your laptop config:

### 1. 1 VGA + 1 HDMI port
No-brainer: get a VGA cable and a HDMI cable

### 2. 1 Display port + 1 HDMI port
Get a HDMI -> Displayport cable and a HDMI cable

### 3. USB port + 1 HDMI port
Get a HDMI -> USB 3.0 cable and a HDMI cable. This is a bit tricky since there are two technologies out there: 
1. ***DisplayLink*** : I used this one (<a href='https://www.amazon.com/gp/product/B01CSG7TUC/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1'>Wavlink USB3.0 to HDMI</a>).
It worked right off the bat with ubuntu 20.04. If it doesn't work for you, you can find the asoociated driver on their <a href='https://www.displaylink.com/downloads'>website</a>.
There are a number of other HDMI to USB convertors on the market. One way to verify this is to look at the associated driver name. 
   If it has the word "DisplayLink" as a substring, then you're good to go.
2. ***Fresco Logic***: Fresco logic is the outdated one, works only on windows, and doesn't seem to work on Linux (Ubuntu 20.04) or Mac.
There is an outdated <a href='https://github.com/FrescoLogic/FL2000'>github repository</a> for the fresco logic driver (fl2000) which needs to be adapted for newer linux versions.

I chose the ***DisplayLink*** option since I have a MSI ubuntu setup and a macbook, and I wanted both laptops to work with the dual screen setup.

### 4. USB-C ports only
You can use multiple HDMI-> USB-C cables.


This is not an exhaustive list by any means. Hope this helps someone.