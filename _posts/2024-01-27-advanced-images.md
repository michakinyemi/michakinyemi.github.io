---
layout: post
title: a post with advanced image components
date: 2024-01-27 11:46:00
description: this is what advanced image components could look like
tags: formatting images
categories: sample-posts
thumbnail: assets/img/9.jpg
images:
  compare: true
  slider: true
---

This is an example post with advanced image components.

## Image Slider

This is a simple image slider. It uses the [Swiper](https://swiperjs.com/) library. Check the [examples page](https://swiperjs.com/demos) for more information of what you can achieve with it.

<swiper-container keyboard="true" height="90" navigation="true" pagination="true" pagination-clickable="true" pagination-dynamic-bullets="true" rewind="true">
  <swiper-slide>{% include figure.liquid loading="eager" path="assets/img/dekosky_lab/polaroids/1.jpg" class="rounded z-depth-1" %}</swiper-slide>
  <swiper-slide>{% include figure.liquid loading="eager" path="assets/img/dekosky_lab/polaroids/2.jpg" class="rounded z-depth-1" %}</swiper-slide>
  <swiper-slide>{% include figure.liquid loading="eager" path="assets/img/dekosky_lab/polaroids/3.jpg" class="rounded z-depth-1" %}</swiper-slide>
  <swiper-slide>{% include figure.liquid loading="eager" path="assets/img/dekosky_lab/polaroids/4.jpg" class="img-fluid rounded z-depth-1" %}</swiper-slide>
</swiper-container>

## Image Comparison Slider

