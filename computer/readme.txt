Robspawn uses the three.js example obj loader as a base:
https://threejs.org/examples/webgl_loader_obj.html

This will generate an image searched from by voice2text. It will then pass this through to comfyui with TripoSR to generate a model before displaying it and passing it through to the final script where it will uploading this to the printer api (octoprint) and start printing
