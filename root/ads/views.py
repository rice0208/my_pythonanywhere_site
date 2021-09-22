from flask import Blueprint, url_for, redirect

bp = Blueprint('ads', 'ads', url_prefix='/ads')

@bp.route('/')
def ads_index():
    return redirect(url_for('index'))

@bp.route('/icons')
def ads_icons():
    return redirect("https://i.loli.net/2021/09/22/UqJGVtZFNls7Ibj.png")