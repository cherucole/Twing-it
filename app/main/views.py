from flask import render_template, request, redirect,url_for, abort, flash
from . import main
from .forms import UpdateProfile
from ..models import  User
from flask_login import login_required, current_user
from .. import db, photos
import markdown2

# INDEX PAGE
@main.route('/')
def index():
    """ View root page function that returns index page """

    title = 'WELCOME TO TWING'
    return render_template('index.html', title = title, )

@main.route('/about')
def about():
    """ View root page function that returns the about page """

    return render_template('about.html')

# VIEWING EACH SPECIFIC PROFILE
@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

# UPDATING PROFILE
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

# UPDATING PICTURE
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

