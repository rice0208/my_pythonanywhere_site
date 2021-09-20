from flask import Blueprint
from flask.helpers import send_file
from .icons_v1 import generate_icon
from io import BytesIO

bp = Blueprint('icons', 'icons', url_prefix='/icons')

@bp.route('/v1/<string>')
def get_icon(string: str):
    img_io = BytesIO()
    image = generate_icon(int(string.encode('utf-8').hex()))
    image.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')