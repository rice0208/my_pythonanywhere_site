from flask import Blueprint
from flask.helpers import send_file
from werkzeug import FileWrapper
from .icons_v1 import generate_icon
from io import BytesIO

bp = Blueprint('icons', 'icons', url_prefix='/icons')

@bp.route('/v1/<string>')
def get_icon(string: str):
    image = generate_icon(int(string.encode('utf-8').hex()))
    img_io = BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    wrapper = FileWrapper(img_io)
    return send_file(wrapper,
                     mimetype='image/png', as_attachment=True, attachment_filename=string+'.png',
                     direct_passthrough=True,
                    )