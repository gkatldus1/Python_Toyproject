from flask import Blueprint, render_template, request, url_for, session
from model import *
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def home():
    store_list = rabbitStore.query.order_by(rabbitStore.name.asc())
    return render_template('main.html', store_list=store_list)
    # 템 플 릿
    # 서버에서 제공하는 자료를 기반으로 페이지를 새로 만들 수 있어요 -> 재사용이 편합니다.
    # jinja 

@bp.route('/store/<int:store_id>/')
def store_detail(store_id):
    store_info = rabbitStore.query.filter_by(id=store_id).first()
    store_menu = rabbitMenu.query.filter_by(store_id=store_id).all()
    return render_template('store_detail.html', store_info=store_info, store_menu=store_menu)

@bp.route('/login', methods=('GET',))
def login_try():
    return render_template('login.html')

@bp.route('/login', methods=('POST',))
def login():
    id = request.form['user_id']
    password = request.form['password']

    user_data = rabbitUser.query.filter_by(id=id).first()

    if not user_data:
        return "없는 아이디입니다."
    elif password != user_data.password:
        return "로그인 실패"
    else:
        session.clear()
        session['user_id'] = id
        session['nickname'] = user_data.nickname

        return "로그인 성공"

@bp.route('/register')
def join():
    return render_template('register.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.home'))

@bp.route('/register', methods=('POST',))
def register():
    if request.method == 'POST':
        user = rabbitUser.query.filter_by(id=request.form['user_id']).first()
        if not user:
            password = request.form['password']

            user = rabbitUser(id=request.form['user_id'], password=password,
            nickname=request.form['nickname'], telephone=request.form['telephone'])
            db.session.add(user)
            db.session.commit()
            
        else:
            return "이미 가입된 아이디입니다."

        return redirect(url_for('main.home'))