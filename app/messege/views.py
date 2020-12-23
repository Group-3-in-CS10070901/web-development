from flask import redirect, render_template, redirect
from ..models import User, Message
from . import message
from flask_login import login_required, current_user
from flask_moment import datetime

#发送消息
'''
@login_required
@message.route('/sendMessage/<recipe_id>',method=['GET','POST'])
def sendMessage():
    user = User.query.filter_by(id=recipe_id).first()
        form = MessageForm()
        if form.validate_on_submit():
            msg = Message(author=current_user, recipient=user, body=form.message.data)
            db.session.add(msg)
            db.session.commit()
            flash(_('您的消息已被发送'))
            return redirect(url_for('main.user_info', username=recipient))
        return render_template('send_message.html', title=_('发送消息'), form=form, recipient=recipient)
'''

#接收消息
'''
@login_required
@message.route('/messageList', method = ['GET'])
def messageList():
    current_user.last_message_read_time = datetime.utcnow()
    db.session.commit()
    page = request.args.get('page', 1, type=int)
    messages = current_user.messages_received.order_by(
        Message.timestamp.desc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.messages', page=messages.next_num) if messages.has_next else None
    prev_url = url_for('main.messages', page=messages.prev_num) if messages.has_prev else None
    return render_template('messages.html', messages=messages.items, next_url=next_url, prev_url=prev_url, page=page)
'''

