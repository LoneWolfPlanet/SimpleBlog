import functools
import requests
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


from db import get_db

from service.Request import *

#bp = Blueprint('lone', __name__, url_prefix='/lone')
bp = Blueprint('lone', __name__)

@bp.route('/index', methods=('GET', 'POST'))
def index():
   # Request.startMock()
    if request.method == 'POST':
        pass
    resp = Request.getMethod1('')
    return render_template('lone/index.html')


    
@bp.route('/contact', methods=('GET', 'POST'))
def contact():
    if request.method == 'POST':
        pass

    return render_template('lone/contact.html')

@bp.route('/single', methods=('GET', 'POST'))
def single():
    if request.method == 'POST':
        pass

    return render_template('lone/single.html')

@bp.route('/about', methods=('GET', 'POST'))
def about():
    if request.method == 'POST':
        pass

    return render_template('lone/about.html')


@bp.route('/work', methods=('GET', 'POST'))
def work():
    if request.method == 'POST':
        pass

    return render_template('lone/work.html')