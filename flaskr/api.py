import functools
import os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db
from werkzeug.utils import secure_filename

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
    

@bp.route('/user/query_all', methods=('GET', 'POST'))
def user_query_all():
    '''查询所有用户'''
    if request.method == 'POST':
        db = get_db()
        error = None
        
        users = db.execute(
            'SELECT uid,uname,unick,sex,phone,birthday,intro,exper FROM tbuser'
        ).fetchall()

        if len(users) == 0:
            error = 'empty'
        
        if error is None:
            res_users = []
            for user in users:
                res_user = {}
                res_user['uid'] = user['uid']
                res_user['uname'] = user['uname']
                res_user['unick'] = user['unick']
                res_user['sex'] = user['sex']
                res_user['phone'] = user['phone']
                res_user['birthday'] = user['birthday']
                res_user['intro'] = user['intro']
                res_user['exper'] = user['exper']
                res_users.append(res_user)
            return jsonify(res_users)
        else:
            return error
    else:
        return 'user_query_all'

@bp.route('/user/delete', methods=('GET', 'POST'))
def user_delete():
    '''删除某一用户'''
    if request.method == 'POST':
        uname = request.form['uname']
        db = get_db()
        error = None

        if not uname:
            error = 'failed'
        else:
            db.execute(
                'DELETE FROM tbuser WHERE uname = ?',
                (uname, )
            )

        if error is None:
            return 'success'
        else:
            return error
    else:
        return 'user_delete'


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
        
        url = 'http://106.13.236.185:5000/static/'

        if error is None:
            res_games = []
            for game in games:
                res_game = {}
                res_game['gid'] = game['gid']
                res_game['gname'] = game['gname']
                res_game['name'] = game['name']
                res_game['filename'] = game['filename']
                res_game['fileurl'] = url + 'game/' + game['filename']
                res_game['image'] = url + 'image/' + game['image']
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
                'SELECT * FROM game WHERE name = ?', (name, )
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


@bp.route('/game/query_all', methods=('GET', 'POST'))
def game_query_all():
    '''查询所有游戏'''
    if request.method == 'POST':
        db = get_db()
        error = None
        games = db.execute(
            'SELECT * FROM game'
        ).fetchall()

        if len(games) == 0:
            error = 'empty'
        
        url = 'http://106.13.236.185:5000/static/'

        if error is None:
            res_games = []
            for game in games:
                res_game = {}
                res_game['gid'] = game['gid']
                res_game['gname'] = game['gname']
                res_game['name'] = game['name']
                res_game['filename'] = game['filename']
                res_game['fileurl'] = url + 'game/' + game['filename']
                res_game['image'] = url + 'image/' + game['image']
                res_game['note'] = game['note']
                res_game['version'] = game['version']
                res_game['star'] = game['star']
                res_game['status'] = get_game_status(game['status'])
                res_games.append(res_game)
            return jsonify(res_games)
        else:
            return error
    else:
        return 'game_query_all'


@bp.route('/game/check_start', methods=('GET', 'POST'))
def game_check_start():
    '''开始审核某游戏'''
    if request.method == 'POST':

        gid = request.form['gid']

        db = get_db()
        error = None

        if not gid:
            error = 'failed'
        else:
            db.execute(
                'UPDATE game SET status = 1 WHERE gid=?',
                (gid, )
            )
            db.commit()

        if error is None:
            return 'success'
        else:
            return error
    else:
        return 'game_check_start'

@bp.route('/game/check_pass', methods=('GET', 'POST'))
def game_check_pass():
    '''审核通过某游戏'''
    if request.method == 'POST':

        gid = request.form['gid']

        db = get_db()
        error = None

        if not gid:
            error = 'failed'
        else:
            db.execute(
                'UPDATE game SET status = 2 WHERE gid=?',
                (gid, )
            )
            db.commit()

        if error is None:
            return 'success'
        else:
            return error
    else:
        return 'game_check_pass'


@bp.route('/game/check_fail', methods=('GET', 'POST'))
def game_check_fail():
    '''审核失败某游戏'''
    if request.method == 'POST':

        gid = request.form['gid']

        db = get_db()
        error = None

        if not gid:
            error = 'failed'
        else:
            db.execute(
                'UPDATE game SET status = 3 WHERE gid=?',
                (gid, )
            )
            db.commit()

        if error is None:
            return 'success'
        else:
            return error
    else:
        return 'game_check_fail'

@bp.route('/game/delete', methods=('GET', 'POST'))
def game_delete():
    '''删除某一游戏'''
    if request.method == 'POST':
        gid = request.form['gid']
        db = get_db()
        error = None

        if not gid:
            error = 'failed'
        else:
            db.execute(
                'DELETE FROM game WHERE gid = ?',
                (gid, )
            )
            db.commit()

        if error is None:
            return 'success'
        else:
            return error
    else:
        return 'game_delete'

@bp.route('/game/upload', methods=('GET', 'POST'))
def game_upload():
    '''开发者上传游戏'''
    if request.method == 'POST':

        # 一个带有 enctype=multipart/form-data 的 <form> 标记，
        # 标记中含有 一个 <input type=file> 。
        # check if the post request has the file part
        if 'image' not in request.files:
            flash('No image file part')
            return 'error'
        file_image = request.files['image']
        if 'game' not in request.files:
            flash('No game file part')
            return 'error'
        file_game = request.files['game']

        gname = request.form['gname']
        name = request.form['name']
        note = request.form['note']
        version = request.form['version']
        filename = name + '.' + file_game.filename.rsplit('.', 1)[1].lower()
        image = name + '.' + file_image.filename.rsplit('.', 1)[1].lower()

        basepath = os.path.abspath(os.path.dirname(__file__))   # 当前文件所在路径

        # if user does not select file, browser also
        # submit an empty part without filename
        if file_image.filename == '':
            flash('No selected file')
            return 'error'
        if file_image and allowed_file(file_image.filename):
            file_image.save(basepath + '\static\image\\' + image)
        
        if file_game.filename == '':
            flash('No selected file')
            return 'error'
        if file_game and allowed_file(file_game.filename):
            file_game.save(basepath + '\static\game\\' + filename)

        db = get_db()
        error = None

        if not gname or not name:
            error = 'failed'
        else:
            game = db.execute(
                'SELECT * FROM game WHERE name = ?', (name, )
            ).fetchone()
        
            if game is not None:
                error = 'repeat'

        if error is None:
            db.execute(
                'INSERT INTO game (gname, name, filename, image, note, version) VALUES (?, ?, ?, ?, ?, ?)',
                (gname, name, filename, image, note, version)
            )
            db.commit()
            return 'success'
        else:
            return error
    else:
        return '''
        <!doctype html>
        <title>开发者上传游戏</title>
        <h1>开发者上传游戏</h1>
        <form method=post enctype=multipart/form-data>
        游戏名：<input type=text name=gname>
        逻辑名：<input type=text name=name>
        简介：<input type=text name=note>
        版本：<input type=text name=version>
        图片：<input type=file name=image>
        Py：<input type=file name=game>
        <input type=submit value=Upload>
        </form>
        '''
        return 'game_upload'


@bp.route('/game/update', methods=('GET', 'POST'))
def game_update():
    '''开发者更新游戏'''
    if request.method == 'POST':

        if 'game' not in request.files:
            flash('No game file part')
            return 'error'
        file_game = request.files['game']

        gid = request.form['gid']
        version = request.form['version']
    
        db = get_db()
        error = None

        game = db.execute(
            'SELECT * FROM game WHERE gid = ?', (gid, )
        ).fetchone()
        filename = game['name'] + '.' + file_game.filename.rsplit('.', 1)[1].lower()

        basepath = os.path.abspath(os.path.dirname(__file__))   # 当前文件所在路径
  
        if file_game.filename == '':
            flash('No selected file')
            return 'error'
        if file_game and allowed_file(file_game.filename):
            file_game.save(basepath + '\static\game\\' + filename)

        if error is None:
            db.execute(
                'UPDATE game SET filename = ?, version = ? WHERE gid = ?',
                (filename, version, gid)
            )
            db.commit()
            return 'success'
        else:
            return error
    else:
        return '''
        <!doctype html>
        <title>开发者更新游戏</title>
        <h1>开发者更新游戏</h1>
        <form method=post enctype=multipart/form-data>
        游戏id：<input type=text name=gid>
        新版本号：<input type=text name=version>
        Py：<input type=file name=game>
        <input type=submit value=Upload>
        </form>
        '''
        return 'game_update'

def get_game_status(status):
    mean = ''
    if status == 0 or status == '0':
        mean = '未审核'
    elif status == 1 or status == '1':
        mean = '审核中'
    elif status == 2 or status == '2':
        mean = '审核通过'
    elif status == 3 or status == '3':
        mean = '审核失败'
    else:
        mean = '审核状态异常:' + status
    return mean

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'py', 'pyw', 'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route('/game/query_by_id', methods=('GET', 'POST'))
def game_query_by_id():
    '''通过编号查询游戏'''
    if request.method == 'POST':
        db = get_db()
        error = None
        gid = request.form['gid']
        db = get_db()
        error = None

        if not gid:
            error = 'failed'
        else:
            game = db.execute(
                'SELECT * FROM game WHERE gid = ?',
                (gid, )
            ).fetchone()
            if game is None:
                error = 'failed'

        url = 'http://106.13.236.185:5000/static/'

        if error is None:
            res_game = {}
            res_game['gid'] = game['gid']
            res_game['gname'] = game['gname']
            res_game['name'] = game['name']
            res_game['filename'] = game['filename']
            res_game['fileurl'] = url + 'game/' + game['filename']
            res_game['image'] = url + 'image/' + game['image']
            res_game['note'] = game['note']
            res_game['version'] = game['version']
            res_game['star'] = game['star']
            res_game['status'] = get_game_status(game['status'])
            return jsonify(res_game)
        else:
            return error
    else:
        return 'game_query_by_id'

@bp.route('/game/update_game', methods=('GET', 'POST'))
def game_update_game():
    '''管理员更新游戏'''
    if request.method == 'POST':
        gid = request.form['gid']
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
        if not gid or not gname or not name:
            error = 'failed'

        if error is None:
            db.execute(
                'UPDATE game SET gname=?, name=?, filename=?, \
                    image=?, note=?, version=?, star=?, \
                    status=? WHERE gid = ?',
                (gname, name, filename, image, note, version, star, status, gid)
            )
            db.commit()
            return 'success'
        else:
            return error
    else:
        return 'game_update_game'