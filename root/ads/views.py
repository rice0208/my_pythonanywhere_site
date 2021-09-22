from flask import Blueprint, url_for, redirect

bp = Blueprint('ads', 'ads', url_prefix='/ads')

@bp.route('/')
def ads_index():
    return redirect(url_for('index'))

@bp.route('/icons')
def ads_icons():
    return redirect("https://sm.ms/image/UqJGVtZFNls7Ibj")