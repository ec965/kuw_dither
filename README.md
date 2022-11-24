This is an ImageMagick script that does the following:

1. Downscale the image
2. Run the Kuwahara filter 
3. Use ordered dithering with 8 colors
4. Interpolate pixels using the nearest neighbor algorithm with a Box filter
5. Upscale back to the original size

# Usage

Requirements:

- python3
- ImageMagick

```bash
./kuw_dither.py $INPUT_FILE_NAME
```

# Inspiration

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

I found [a post on Low Tech Magazine](https://solar.lowtechmagazine.com/2018/09/how-to-build-a-lowtech-website.html)
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

# Experimentation

After readint the Low Tech Magazine article, I experimented with just dithering
with ImageMagick.
This went okay but I wasn't able to get an effect I liked.

After going through all the above inspiration, I started off experimenting
with different levels of Kuwahara filtering with different dithering algorithms.
The outputs of the Floyd-Steinberg and Riemersma filters produced interesting images
but they weren't as geometric as my original 4Chan inspiration.

## Result

Finally, I figured out that using ordered dithering, I could achieve what I was looking for.
After some experimentation, I settled on using ordered dithering with ordered 8x8 threshold map at level 3.
The final ImageMagick script is:

```bash
convert $INPUT \
    \( -resize 50% )\
    \( -kuwahara 1 \) \
    \( -ordered-dither o8x8,3 -colors 8 \) \
    \( -interpolate Nearest -filter Box \) \
    \( -resize 200% \) \
    $OUTPUT
```

To summarize:

1. Downscale the image
2. Run the Kuwahara filter 
3. Use ordered dithering with 8 colors
4. Interpolate pixels using the nearest neighbor algorithm with a Box filter
5. Upscale back to the original size

## Tweaking Parameters

### Downscale

Tweaking the initial downscale will result in a more obvious filter.
When the Kuwahara filter and dithering effect have fewer pixels to work with,
their effects are more pronounced.

### Kuwahara Filter

Increasing the Kuwahara filter radius will give a more painter like look to the final image.
More areas of color will get splotched together.

### Dithering

Different dithering algorithms will produce different effects.
Using the Floyd-Steinberg algorithm will produce a much less pixelated look.
With Ordered dithering, I was able to produce a much more grid like pixelated look.

Having 8 colors usually produces an image that looks distinctly filtered.
With 16 or 32 colors, I usually will get enough colors that output will still look
fairly close to the input in terms of color.

### Interpolation

Interpolation will give the final result a more pixelated look.
Using the Box or Point filters gives a harsher look while
the Triangle filter results in a softer image.

### Upscale

The final upscale is just to get the image back to it's original size.
I use the inverse of the downscale percentage to do this.
