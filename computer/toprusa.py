#This is a flask script which will send the model through to prusa slicer,  resize and rotate the model then slice it before passing it on to the printer

from flask import Flask
import subprocess
import requests 
from flask import Flask
from flask_cors import CORS  # Import CORS from flask_cors

app = Flask(__name__)
#example meshsave_00502_
CORS(app)  # Enable CORS for all routes
@app.route('/executeslicer/<obj_filename>')
def execute_slicer(obj_filename):
    command = r'"C:\Program Files\Prusa3D\PrusaSlicer\prusa-slicer-console.exe" --export-gcode "H:\XLXL\comfy4\ComfyUI_windows_portable_nvidia_cu121_or_cpu\ComfyUI_windows_portable\ComfyUI\output\{}.obj" --output "H:\XLXL\toprusa" --load "H:\XLXL\toprusa\config.ini" --scale 20 --rotate-x 90'.format(obj_filename)
    subprocess.run(command, shell=True)
    
    upload_gcode(obj_filename)
    return 'Slicer command executed!'

def upload_file_to_octoprint(file_path):
    url = 'http://192.168.0.107/api/files/local'
    headers = {'X-Api-Key': 'xxxxxxxxxxxxxxxx'}  # Replace 'xxx' with your actual API key
    files = {'file': open(file_path, 'rb')}
    data = {'select': 'true', 'print': 'true'}
    response = requests.post(url, files=files, data=data, headers=headers)
    return response



@app.route('/upload_gcode')
def upload_gcode(obj_filename):
    file_path = r"H:\XLXL\toprusa\{}.gcode".format(obj_filename)  
    response = upload_file_to_octoprint(file_path)
    return response.text



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8085)
