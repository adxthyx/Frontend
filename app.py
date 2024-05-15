import os
import base64
from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    image_data = request.json.get('image')
    
    # Decode base64 image data
    image_data = image_data.split(',')[1]  # Remove header data
    image_bytes = base64.b64decode(image_data)
    
    # Save image to local directory
    save_dir = 'C:\\Users\\adith\\Desktop\\MiniProject\\kannada-character-recognition\\kannada_dataset'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    image_path = os.path.join(save_dir, 'drawing.png')  # Change the filename as needed
    with open(image_path, 'wb') as f:
        f.write(image_bytes)
    
    print('Image saved to:', image_path)
    
    return 'Image saved successfully', 200

if __name__ == '__main__':
    app.run(debug=True)
