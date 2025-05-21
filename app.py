from flask import Flask, request, render_template, send_file
import your_video_processing_script  # rename your notebook code to a .py script

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    video = request.files['video']
    video_path = f"./uploads/{video.filename}"
    video.save(video_path)

    output_path = your_video_processing_script.process_video(video_path)
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
