from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']

    filename = secure_filename(image.filename)
    image.save(os.path.join('/app/images', filename))

    return jsonify({'success': True}), 200

@app.route('/delete/<filename>', methods=['DELETE'])
def delete(filename):
    filepath = os.path.join('/images', filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found'}), 404

    os.remove(filepath)

    return jsonify({'success': True}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)