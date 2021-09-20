from flask import Blueprint, Response
from werkzeug import FileWrapper
from .icons_v1 import generate_icon
from io import BytesIO

bp = Blueprint('icons', 'icons', url_prefix='/icons')

@bp.route('/v1/<string>')
def get_icon(string: str):
    image = generate_icon(int(string.encode('utf-8').hex(), 16))
    img_io = BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    wrapper = FileWrapper(img_io)
    return Response(wrapper,
                     mimetype='image/png',
                     direct_passthrough=True,
                    )