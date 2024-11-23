from flask import Flask, request, render_template, jsonify
from openai import OpenAI
from utils import get_openai_api_key
import os
from agent import create_crew
from flask_cors import CORS

api_key = get_openai_api_key()
client = OpenAI(api_key=api_key)
app = Flask(__name__)
CORS(app)

if not os.path.exists('audio'):
    os.makedirs('audio')

ALLOWED_EXTENSIONS = {'flac', 'm4a', 'mp3', 'mp4', 'mpeg', 'mpga', 'oga', 'ogg', 'wav', 'webm'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST', 'OPTIONS'])
def upload():
    if request.method == 'OPTIONS':
        return '', 200
        
    if 'audio_data' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400
        
    audio_file = request.files['audio_data']
    
    if not audio_file:
        return jsonify({'error': 'No selected file'}), 400

    try:
        audio_path = "audio/recording.webm"
        audio_file.save(audio_path)
        
        with open(audio_path, "rb") as audio_file:
            transcript_response = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )
            
        with open('reference.txt', 'r') as file:
            reference_content = file.read()
            
        crew = create_crew(transcript_response, reference_content)
        result = crew.kickoff()
        
        return jsonify({
            'transcript': transcript_response,
            'blog_post': str(result)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    try:
        if not os.path.exists('audio'):
            os.makedirs('audio')
        if not os.path.exists('reference.txt'):
            with open('reference.txt', 'w') as f:
                f.write('')
        app.run(debug=True, host='0.0.0.0', port=8000)
    except Exception as e:
        pass