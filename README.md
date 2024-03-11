# Printydoodad

Speech to 3D print using TripoSR

Printydoodad is a project designed to generate custom 3D models and initiate their printing with a single voice command.

This system operates locally, running on a PC rather than a mobile device.

![Alt text](/images/pirate.png "generating a pirate dog")

## How It Works

1. The system first captures the name of the desired item through JavaScript's `recognizeSpeech` function.
2. It then incorporates this name into a JSON workflow and transmits it to ComfyUI to produce an image based on the provided prompt.
3. ComfyUI generates a 3D model from the image, which is displayed on the device and passed to the next script.
4. The model is then processed by Prusaslicer to adjust parameters like rotation and size, and to generate the G-code.
5. Finally, the G-code is uploaded to the printer (Octoprint) using an API key.

## Acknowledgments

Special thanks to:
- Three.js (threejs.org) for its library and examples. Visit [Three.js](https://threejs.org/examples/webgl_loader_obj.html) for more information.
