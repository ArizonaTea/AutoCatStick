# Raspberry Pi 4 Camera Setup

## Hardware Installation

1. There are 2 types of camera: **normal version** (green circuit) and **NoIR version** (black circuit). The latter is used in the total darkness and need to work with infrared light source.

2. Current version of normal Pi camera is based on a high-quality Sony IMX219 image sensor.

3. Installing the camera:

   The camera side:

   ![Camera Side](\Images\Camera_side.PNG)

   The board side:

   ![Board Side](\Images\Board_side.PNG)

## Software Test

1. Go to the Pi Configuration GUI, Interfaces tab, enable the camera. Or you can use following command to enable it through terminal

   > sudo raspi-config

2. Use the following command at terminal to test camera

   > raspistill -o test.jpg

   This is to show a live preview for 5 second, then it will capture a photo and save at home folder with name _test.jpg_

   The following command will rotate the camera with 180 degree and do same as above:

   > raspistill -rot 180 -o test.jpg

3. Using Python to test the camera:

```python
from picamera import PiCamera
from time import sleep
camera = PiCamera()

camera.rotation = 180
camera.start_preview()
sleep(10)
camera.stop_preview()
camera.capture('/home/pi/Desktop/image.jpg')
camera.resolution = (1920,1080)

camera.start_recording('/home/pi/Desktop/video.h264')   # Note that the h264 here only support up to 1920 x 1080
sleep(10)
camera.stop_recording()
```

4. Example: Use button to do a camera/video recorder with preview

Here is button setup:

![Button Setup](\Images\Button_Setup.PNG)

Python Code is:

```python
from picamera import PiCamera
from time import sleep
from gpiozero import Button
camera = PiCamera()
button = Button(2)
camera.start_preview()
frame = 1
while True:
 try:
 button.wait_for_press()
 camera.capture('/home/pi/Desktop/animation/frame%03d.jpg'
% frame)
 frame += 1
 except KeyboardInterrupt:
 camera.stop_preview()
 break
```

The captured photos are all frames. Use following command to convert to video and play:

> avconv -r 1 -i frame%03d.jpg -r 10 animation.h264
>
> omxplayer animation.h264

5. Other useful command:

If you need more control over the Raspberry Pi Camera Module, you can use the Python  picamera library to access various settings. These settings, along with their default values, are  detailed below for inclusion in your own programs. 

> camera.awb_mode = 'auto' 

This sets the automatic white balance mode of the camera, and can be set to any one of  the following modes: off, auto, sunlight, cloudy, shade, tungsten, fluorescent,  incandescent, flash, or horizon. If you find your pictures and videos look a little blue or  yellow, try a different mode.

> camera.brightness = 50 

This sets the brightness of the camera image, from darkest at 0 to brightest at 100. 

> camera.color_effects = None 

This changes the colour effect currently in use by the camera. Normally, this setting should  be left alone, but if you provide a pair of numbers you can alter the way the camera records  colour: try (128, 128) to create a black and white image.

> camera.contrast = 0 

This sets the contrast of the image. A higher number will make things look more dramatic  and stark; a lower number will make things look more washed out. You can use any number  between -100 for minimum contrast and 100 for maximum contrast. 

> camera.crop = (0.0, 0.0, 1.0, 1.0) 

This allows you to crop the image, cutting parts off the sides and tops to capture only the part  of the image you need. The numbers represent X coordinate, Y coordinate, width, and height,  and by default captures the full image. Try reducing the last two numbers – 0.5 and 0.5 is a  good starting point – to see what effect this setting has. 

> camera.exposure_compensation = 0 

This sets the exposure compensation of the camera, allowing you to manually control how much  light is captured for each image. Unlike changing the brightness setting, this actually controls the  camera itself. Valid values range from -25 for a very dark image to 25 for a very bright image. 

> camera.exposure_mode = 'auto' 

This sets the exposure mode, or the logic the Camera Module uses to decide how an image  should be exposed. Possible modes are: off, auto, night, backlight, spotlight,  sports, snow, beach, verylong, fixedfps, antishake, and fireworks. 

> camera.framerate = 30 

This sets the number of images captured to create a video per second, or the frame rate. A  higher frame rate creates a smoother video, but takes up more storage space. Higher frame  rates require a lower resolution to be used, which you can set via camera.resolution. 

> camera.hflip = False 

This flips the camera image across the horizontal, or X, axis when set to True. 

> camera.image_effect = 'none' 

This applies one of a range of image effects to the video stream, which will be visible in the preview  as well as the saved images and videos. Possible effects are: blur, cartoon, colorbalance,  colorpoint, colorswap, deinterlace1, deinterlace2, denoise, emboss, film,  gpen, hatch, negative, none, oilpaint, pastel, posterise, saturation, sketch,  solarize, washedout, and watercolor. 

> camera.ISO = 0 

This changes the ISO setting of the camera, which affects how sensitive it is to light. By default, the  camera adjusts this automatically depending on the available light. You can set the ISO yourself  using one of the following values: 100, 200, 320, 400, 500, 640, 800. The higher the ISO, the better  the camera will perform in low-light environments but the grainier the image or video it captures.

> camera.meter_mode = 'average' 

This controls how the camera decides on the amount of available light when setting its  exposure. The default averages the amount of light available throughout the whole picture;  other possible modes are backlit, matrix, and spot. 

> camera.resolution = (1920, 1080) 

This sets the resolution of the captured picture or video, represented by two numbers for width  and height. Lower resolutions will take up less storage space and allow you to use a higher  frame rate; higher resolutions are better quality but take up more storage space. 

> camera.rotation = 0 

This controls the rotation of the image, from 0 degrees through 90, 180, and 270 degrees.  Use this if you can’t position the camera so that the ribbon cable is coming out of the bottom. 

> camera.saturation = 0 

This controls the saturation of the image, or how vibrant colours are. Possible values range  from -100 to 100. 

> camera.sharpness = 0 

This controls the sharpness of the image. Possible values range from -100 to 100. 

> camera.shutter_speed = 0 

This controls how quickly the shutter opens and closes when capturing images and videos.  You can set the shutter speed manually in microseconds, with longer shutter speeds working  better in lower light and faster shutter speeds in brighter light. This should normally be left on  its default, automatic, setting. 

> camera.vflip = False 

This flips the camera image across the horizontal, or Y, axis when set to True. 

> camera.video_stabilization = False 

When set to True, this turns on video stabilisation. You only need this if the Camera Module  is moving while you’re recording, such as if it’s attached to a robot or being carried, in order to  reduce the shakiness of the captured video. More information on these settings, as well as additional settings not documented here,  can be found at [picamera.readthedocs.io](https://picamera.readthedocs.io).

