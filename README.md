# Printydoodad Speak2Print

Speech to 3D print using TripoSR

Printydoodad is a project designed to generate custom 3D models and start them printing with a single voice command.

This system operates locally, running on a PC rather than a mobile device.

Youtube video:
[![Everything Is AWESOME](https://img.youtube.com/vi/n1W-YVuqYB0/0.jpg)](https://www.youtube.com/watch?v=n1W-YVuqYB0 "Everything Is AWESOME")

## How It Works

1. The system first captures the name of the desired item through JavaScript's `recognizeSpeech` function.
2. It then incorporates this name into a JSON workflow and transmits it to ComfyUI to produce an image based on the provided prompt.
3. ComfyUI generates a 3D model from the image, which is displayed on the device and passed to the next script.
4. The model is then processed by Prusaslicer to adjust parameters like rotation and size, and to generate the G-code.
5. Finally, the G-code is uploaded to the printer (Octoprint) using an API key.

# Notes
This was made for myself and is documented here, but this is going to be a fiddly install as folder locations etc are just where they were when I was playing with it, and its janky as are the models it creates. You can change the json to up the quality for the model, and different checkpoints can be better than others

## Setup
Note that you will need three.js downloaded as well as comfyui installed and generating TripoSR models. I can add more on this in future
My (terrible) folder structure is 


H:\XLXL\comfy4 -> ("python -m http.server" from here)
H:\XLXL\comfy4\three.js\examples\dreamthink.html
H:\XLXL\comfy4\ComfyUI_windows_portable_nvidia_cu121_or_cpu\ComfyUI_windows_portable\ComfyUI\output  (...lol..sorry)
You would need to update these references in the code

# KKnown issues
-The timer is not accurate. The bar will go green when loaded, but the slider is just a guesstimate based on the time it normally takes to do them. Feel free to change that
-others. Will fill this in when I know
-Don't run this with access to the net. I had to mess with cors to get it to work, and there is absolutely no input verification. Use at your own risk and all that

## Acknowledgments

Special thanks to:
- Three.js (threejs.org) for its library and examples. Visit [Three.js](https://threejs.org/examples/webgl_loader_obj.html) for more information.


![Alt text](/images/pirate.png "generating a pirate dog")
