from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)

UPLOAD_FOLDERS = {
    'dulles': 'uploads_dulles',
    'wallops': 'uploads_wallops',
    'albany': 'uploads_albany',
    'howard': 'uploads_howard'
}

def get_upload_folder():
    route_name = request.path.strip('/')
    return UPLOAD_FOLDERS.get(route_name)

@app.before_request
def set_upload_folder():
    app.config['UPLOAD_FOLDER'] = get_upload_folder()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dulles')
def dulles():
    folder = get_upload_folder() or 'uploads'  # Default to 'uploads' if no specific folder
    files = os.listdir(os.path.join(app.root_path, app.config['UPLOAD_FOLDER']))
    return render_template('dulles.html', files=files)

@app.route('/wallops')
def wallops():
    return render_template('wallops.html')

@app.route('/albany')
def albany():
    return render_template('albany.html')

@app.route('/howard')
def howard():
    return render_template('howard.html')

@app.route('/download/<filename>')
def download(filename):
    folder = get_upload_folder() or 'uploads'  # Default to 'uploads' if no specific folder
    return send_from_directory(folder, filename)

if __name__ == '__main__':
    app.run(debug=True)
