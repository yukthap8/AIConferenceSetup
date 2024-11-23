from flask import Flask, request, render_template, jsonify
from openai import OpenAI
from utils import get_openai_api_key
import os
from agent import create_crew
from flask_cors import CORS
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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
    logger.debug("Serving index page")
    return render_template('index.html')

@app.route('/upload', methods=['POST', 'OPTIONS'])
def upload():
    if request.method == 'OPTIONS':
        return '', 200
        
    logger.debug("Received upload request")
    if 'audio_data' not in request.files:
        logger.error("No audio file in request")
        return jsonify({'error': 'No audio file provided'}), 400
        
    audio_file = request.files['audio_data']
    
    if not audio_file:
        logger.error("Empty audio file")
        return jsonify({'error': 'No selected file'}), 400

    try:
        audio_path = "audio/recording.webm"
        audio_file.save(audio_path)
        logger.debug(f"Saved audio file to {audio_path}")
        
        with open(audio_path, "rb") as audio_file:
            transcript_response = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )
        logger.debug(f"Transcription complete: {transcript_response}")
            
        crew = create_crew()
        with open('reference.txt', 'r') as file:
            # reference_content = file.read()
            
        result = crew.kickoff(inputs={
            # "topic": ,
            # "reference_content": 
        })
        logger.debug("Crew processing complete")
        
        return jsonify({
            'transcript': transcript_response,
            'blog_post': str(result)
        })
        
    except Exception as e:
        logger.error(f"Error during processing: {str(e)}", exc_info=True)
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    try:
        logger.info("Starting Flask server on port 6000")
        if not os.path.exists('audio'):
            os.makedirs('audio')
        if not os.path.exists('reference.txt'):
            with open('reference.txt', 'w') as f:
                f.write('')
        app.run(debug=True, host='0.0.0.0', port=8000)
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}", exc_info=True)