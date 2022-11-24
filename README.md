# Why?

## 4Chan /wg

I found a post on 4chan's /wg board awhile back that had some interesting
edits.
The [link to the original thread](https://boards.4chan.org/wg/thread/7743043)
is now dead, but the original post was:

```
I was fucking around and found a fun way of livening up old and/or low res wallpapers, and I'll be dumping some and sharing the technique. To my knowledge this will require photoshop.

>open your image in PS
>shrink it to exactly half or a quarter of your screen's resolution
>gaussian blur if desired
>save for web as PNG-8 using "Restrictive" color reduction and "Pattern" dithering, setting colors to "Auto" or your desired bit depth
>close, and open your newly exported file
>upscale the image to full res using "Nearest Neighbor" in resampling
>win
```

## Low Tech Magazine

I found [a post on Low tech magazine](https://solar.lowtechmagazine.com/2018/09/how-to-build-a-lowtech-website.html)
that discussed how they redesigned their blog to be more energy efficient.
One of the things they did was dither all images to reduce image size.

## Acerola: The Kuwahara Filter

More recently, I watched a video called ['The Kuwahara Filter'](https://youtu.be/LDhN-JK3U9g?list=LL)
by [Acerola](https://www.youtube.com/@Acerola_t).
In the video, he explains how the Kuwahara filter was created and potential use cases.
One [interesting combination](https://youtu.be/LDhN-JK3U9g?list=LL&t=843)
he mentions is using the Kuwahara filter and then dithering.

## Seph's Blog

On [Seph](https://josephg.com/blog/), Joseph Gentle's blog, his tiled
[background image](https://josephg.com/blog/assets/background.png) looks like
some sort of dithered pixelated pattern.

## All Together

From these sources, I decided that I'd try to emulate the recipe from the 4Chan post
but with Kuwahara filter rather than a Gaussian blur.
I don't know how to use PhotoShop so I'm opting to use [ImageMagick](https://imagemagick.org/)
instead.
I also get the added benefit of creating a simple program instead of having
to go through PhotoShop GUI flows in the future.

I want to create a general filter that looks cool.
I'll then use the filter to create a similar background image to
[Seph's](https://josephg.com/blog/) blog for my own website.
