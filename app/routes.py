import os
from flask import Blueprint, render_template, send_from_directory, jsonify, current_app

bp = Blueprint('routes', __name__)
FILE_DIR = "/data"

@bp.route('/')
def index_view():
    files = os.listdir(FILE_DIR)
    return render_template('index.html', files=files)

@bp.route("/download/<path:filename>")
def download_file(filename):
    return send_from_directory(FILE_DIR, filename, as_attachment=True)


@bp.route('/api/files')
def api_list_files():
    files = os.listdir(FILE_DIR)
    return jsonify(files)
