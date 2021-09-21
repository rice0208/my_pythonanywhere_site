from flask import Blueprint, Response, render_template, request
from werkzeug.wsgi import FileWrapper
from .icons_v1 import generate_icon_v1
from io import BytesIO
from urllib.parse import quote

bp = Blueprint("icons", "icons", url_prefix="/icons")

@bp.route("/", methods=("GET", "POST"))
def get_index():
    if request.method == 'POST':
        string = request.form['string']
        if string == "":
            return render_template('icons/main.html', url="", has_image=False, string="")
        image_url = "https://rice0208.pythonanywhere.com/icons/v1/" + quote(string)
        return render_template(
            "icons/main.html",
            url = image_url,
            has_image = True,
            string = string,
        )
    return render_template('icons/main.html', url="", has_image=False, string="")

@bp.route("/v1/<string>")
def get_icon(string: str):
    image = generate_icon_v1(
        int(str(int(string.encode("utf-8").hex(), 16) ** 50)[-50:]) ** 3
    )
    img_io = BytesIO()
    image.save(img_io, "PNG")
    img_io.seek(0)
    wrapper = FileWrapper(img_io)
    return Response(
        wrapper,
        mimetype="image/png",
        direct_passthrough=True,
    )
