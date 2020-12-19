import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
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
        if not username:
            error = 'failed'
        elif not password:
            error = 'failed'
        else:
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
        if not username:
            error = 'failed'
        elif not password:
            error = 'failed'
        else:
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

@bp.route('/login_admin', methods=('GET', 'POST'))
def login_admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        if not username:
            error = 'failed'
        elif not password:
            error = 'failed'
        else:
            user = db.execute(
                'SELECT * FROM admin WHERE aname = ?', (username, )
            ).fetchone()

            if user is None:
                error = 'failed'
            elif not check_password_hash(user['apwd'], password):
                error = 'failed'

        if error is None:
            return 'success'
        else:
            return error
    else:
        return 'login_admin'

@bp.route('/regit_admin', methods=('GET', 'POST'))
def regit_admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        if not username:
            error = 'failed'
        elif not password:
            error = 'failed'
        else:
            user = db.execute(
                'SELECT * FROM admin WHERE aname = ?', (username, )
            ).fetchone()
        
            if user is not None:
                error = 'repeat'

        if error is None:
            db.execute(
                'INSERT INTO admin (aname, apwd) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return 'success'
        else:
            return error
    else:
        return 'regit_admin'


@bp.route('/login_developer', methods=('GET', 'POST'))
def login_developer():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        if not username:
            error = 'failed'
        elif not password:
            error = 'failed'
        else:
            user = db.execute(
                'SELECT * FROM developer WHERE dname = ?', (username, )
            ).fetchone()

            if user is None:
                error = 'failed'
            elif not check_password_hash(user['dpwd'], password):
                error = 'failed'

        if error is None:
            return 'success'
        else:
            return error
    else:
        return 'login_developer'

@bp.route('/regit_developer', methods=('GET', 'POST'))
def regit_developer():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        if not username:
            error = 'failed'
        elif not password:
            error = 'failed'
        else:
            user = db.execute(
                'SELECT * FROM developer WHERE dname = ?', (username, )
            ).fetchone()
        
            if user is not None:
                error = 'repeat'

        if error is None:
            db.execute(
                'INSERT INTO developer (dname, dpwd) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return 'success'
        else:
            return error
    else:
        return 'regit_developer'


@bp.route('/user/query_userinfo', methods=('GET', 'POST'))
def user_query_userinfo():
    '''用户查询个人信息'''
    if request.method == 'POST':
        username = request.form['username']
        db = get_db()
        error = None
        user = None
        if not username:
            error = 'failed'
        else:
            user = db.execute(
                'SELECT uid,uname,unick,sex,phone,birthday,intro,exper FROM tbuser WHERE uname = ?',
                (username, )
            ).fetchone()
            if user is None:
                error = 'failed'

        if error is None:
            return {
                'uid': user['uid'],
                'uname': user['uname'],
                'unick': user['unick'],
                'sex': user['sex'],
                'phone': user['phone'],
                'birthday': user['birthday'],
                'intro': user['intro'],
                'exper': user['exper']
            };
        else:
            return error
    else:
        return 'user_query_userinfo'


@bp.route('/user/update_userinfo', methods=('GET', 'POST'))
def user_update_userinfo():
    '''用户修改个人信息'''
    if request.method == 'POST':

        uname = request.form['uname']
        unick = request.form['unick']
        sex = request.form['sex']
        phone = request.form['phone']
        birthday = request.form['birthday']
        intro = request.form['intro']
        exper = request.form['exper']

        db = get_db()
        error = None

        if not uname:
            error = 'failed'
        else:
            db.execute(
                'UPDATE tbuser SET unick=?, sex=?, phone=?, birthday=?, \
                intro=?, exper=? WHERE uname=?',
                (unick, sex, phone, birthday, intro, exper, uname)
            )
            db.commit()

        if error is None:
            return 'success'
        else:
            return error
    else:
        return 'user_update_userinfo'


@bp.route('/game/query_all_pub', methods=('GET', 'POST'))
def game_query_all_pub():
    '''查询所有审核通过的游戏'''
    if request.method == 'POST':
        db = get_db()
        error = None
        games = db.execute(
            'SELECT * FROM game WHERE status = 2'
        ).fetchall()

        if len(games) == 0:
            error = 'empty'
        
        url = 'http://127.0.0.1:5000/static/'

        if error is None:
            res_games = []
            for game in games:
                res_game = {}
                res_game['gid'] = game['gid']
                res_game['gname'] = game['gname']
                res_game['name'] = game['name']
                res_game['filename'] = game['filename']
                res_game['fileurl'] = url + 'game' + game['filename']
                res_game['image'] = url + 'image' + game['image']
                res_game['note'] = game['note']
                res_game['version'] = game['version']
                res_game['star'] = game['star']
                res_games.append(res_game)
            return jsonify(res_games)
        else:
            return error
    else:
        return 'game_query_all_pub'
    

@bp.route('/game/add_game', methods=('GET', 'POST'))
def game_add_game():
    '''管理员添加游戏记录，测试数据用'''
    if request.method == 'POST':
        gname = request.form['gname']
        name = request.form['name']
        filename = request.form['filename']
        image = request.form['image']
        note = request.form['note']
        version = request.form['version']
        star = request.form['star']
        status = request.form['status']
        db = get_db()
        error = None
        if not gname or not name:
            error = 'failed'
        else:
            game = db.execute(
                'SELECT * FROM game WHERE gname = ?', (gname, )
            ).fetchone()
        
            if game is not None:
                error = 'repeat'

        if error is None:
            db.execute(
                'INSERT INTO game (gname, name, filename, image, note, version, star, \
                    status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (gname, name, filename, image, note, version, star, status)
            )
            db.commit()
            return 'success'
        else:
            return error
    else:
        return 'game_add_game'