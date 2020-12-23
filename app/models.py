from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from . import db, login_manager


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

#用户存在数据库中的模型
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)#id 主键
    email = db.Column(db.String(64), unique=True, index=True)#注册邮箱
    username = db.Column(db.String(64), unique=True, index=True)#用户名
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))#hash密码
    confirmed = db.Column(db.Boolean, default=False)#是否认证

    nickname=db.Column(db.String(64), unique=True, index=True)#昵称
    main_image_url = db.Column(db.String(80))#头像
    gender = db.Column(db.String(80))#性别
    height = db.Column(db.Integer)#身高
    love_state = db.Column(db.String(80))#感情状态
    sexuality = db.Column(db.String(80))#性取向
    date_of_birth = db.Column(db.Date) #出身年月日
    salary = db.Column(db.Integer) #月薪
    location = db.Column(db.String(80))  #位置
    contact_information = db.Column(db.String(80))  #联系方式
    about_me = db.Column(db.String(80))  #个性签名
    
    #个人相册
    picture_num = db.Column(db.Integer, default=0)
    pictures = db.relationship('Pictures', backref='owner', lazy='select')

    #试图访问密码时报错
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    #生成密码散列
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    #验证密码散列
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    #生成认正令牌
    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id}).decode('utf-8')

    #认证令牌是否一致
    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    #生成重置密码令牌
    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id}).decode('utf-8')

    #重置密码
    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        user = User.query.get(data.get('reset'))
        if user is None:
            return False
        user.password = new_password
        db.session.add(user)
        return True

        
    def __repr__(self):
        return '<User %r>' % self.username

#图片模型
class Pictures(db.Model):
    __tablename__ = 'pictures'
    id = db.Column(db.Integer, primary_key=True)  #id 主键
    resource_url = db.Column(db.String(80))  #图片位置
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
