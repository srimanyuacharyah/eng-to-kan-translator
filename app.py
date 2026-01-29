from flask import Flask, render_template, request, jsonify, url_for
import os
import uuid
from deep_translator import GoogleTranslator
from gtts import gTTS

APP_ROOT = os.path.dirname(__file__)
OUTPUT_DIR = os.path.join(APP_ROOT, 'static', 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json() or {}
    text = data.get('text', '').strip()
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    translated = GoogleTranslator(source='auto', target='kn').translate(text)

    filename = f"{uuid.uuid4().hex}.mp3"
    out_path = os.path.join(OUTPUT_DIR, filename)
    tts = gTTS(text=translated, lang='kn')
    tts.save(out_path)

    audio_url = url_for('static', filename=f'outputs/{filename}')
    return jsonify({'translated': translated, 'audio_url': audio_url})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
