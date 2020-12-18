import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/login_user', methods=('GET', 'POST'))
def login_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM tbuser WHERE uname = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'failed'
        elif not check_password_hash(user['upwd'], password):
            error = 'failed'

        if error is None:
            return 'success'
        else:
            return error
    else:
        return 'login_user'

@bp.route('/regit_user', methods=('GET', 'POST'))
def regit_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM tbuser WHERE uname = ?', (username,)
        ).fetchone()
    
        if user is not None:
            error = 'repeat'

        if error is None:
            db.execute(
                'INSERT INTO tbuser (uname, upwd) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return 'success'
        else:
            return error
    else:
        return 'regit_user'