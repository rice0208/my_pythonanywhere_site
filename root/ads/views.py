from flask import Blueprint, url_for, redirect
from random import choice

bp = Blueprint('ads', 'ads', url_prefix='/ads')

@bp.route('/')
def ads_index():
    return redirect(url_for('index'))

@bp.route('/icons')
def ads_icons():
    # deprecated
    return redirect("ads.ads_silicon")

@bp.route('/silicon')
def ads_silicon():
    return redirect(
        choice([
            "https://i.loli.net/2021/09/22/UqJGVtZFNls7Ibj.png",
            "https://i.loli.net/2021/09/22/3lOBazuvWCDk15e.png"
        ])
    )
