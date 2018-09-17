# from flask import render_template, request, redirect,url_for, abort, flash
# from . import main
# from .forms import BlogpostForm, UpdateProfile, CommentForm
# from ..models import Blogpost, User, Comment
# from flask_login import login_required, current_user
# from .. import db, photos
# import markdown2
#
# # INDEX PAGE
# @main.route('/')
# def index():
#     """ View root page function that returns index page """
#
#     # category = Category.get_categories()
#     blogposts = Blogpost.query.all()
#
#     title = 'WELCOME TO BLOGPOST'
#     return render_template('index.html', title = title, blogposts=blogposts)
#
# @main.route('/about')
# def about():
#     """ View root page function that returns the about page """
#
#     return render_template('about.html')
#
# # VIEWING EACH SPECIFIC PROFILE
# @main.route('/user/<uname>')
# @login_required
# def profile(uname):
#     user = User.query.filter_by(username = uname).first()
#
#     if user is None:
#         abort(404)
#
#     return render_template("profile/profile.html", user = user)
#
# # UPDATING PROFILE
# @main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
# def update_profile(uname):
#     user = User.query.filter_by(username=uname).first()
#     if user is None:
#         abort(404)
#
#     form = UpdateProfile()
#
#     if form.validate_on_submit():
#         user.bio = form.bio.data
#
#         db.session.add(user)
#         db.session.commit()
#
#         return redirect(url_for('.profile',uname=user.username))
#
#     return render_template('profile/update.html',form =form)
#
# # UPDATING PICTURE
# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))
#
#
# def check_admin():
#     """
#     Prevent non-admins from accessing the page
#     """
#     if not current_user.is_admin:
#         abort(403)
#
#
# # ADDING A NEW BLOGPOST
# @main.route('/blogpost/new', methods=['GET','POST'])
# @login_required
# def new_blogpost():
#     """
#         Add a department to the database
#         """
#     check_admin()
#     new_blogpost = True
#     form = BlogpostForm()
#     if form.validate_on_submit():
#
#         title=form.title.data
#         content=form.content.data
#         category_id=form.category_id.data
#         blogpost = Blogpost(title=title,
#                       content=content,
#                       category_id=category_id,
#                       user=current_user)
#
#         db.session.add(blogpost)
#         db.session.commit()
#
#         # blogpost.save_blogpost(blogpost)
#         print('kasambuli')
#
#         flash('Your blogpost has been created!', 'success')
#
#         return redirect(url_for('main.single_blogpost',id=blogpost.id))
#
#     return render_template('newblogpost.html',
#                            title='New Post',
#                            blogpost_form=form,
#                            new_blogpost=new_blogpost,
#                            action="Add",
#                            legend='New Post')
#
# # VIEW INDIVIDUAL BLOGPOST
# @main.route('/blogpost/new/<int:id>')
# def single_blogpost(id):
#     blogpost = Blogpost.query.get(id)
#     return render_template('singleblogpost.html',
#                            blogpost = blogpost)
#
#
# @main.route('/allblogposts')
# def blogpost_list():
#     # Function that renders all the blogposts and its content
#
#     blogposts = Blogpost.query.all()
#
#     return render_template('blogposts.html', blogposts=blogposts)
#
#
# # VIEWING A blogpost WITH COMMENTS AND COMMENTFORM
# @main.route('/blogpost/<int:blogpost_id>/',methods=["GET","POST"])
# def blogpost(blogpost_id):
#     blogpost = Blogpost.query.get(blogpost_id)
#     form = CommentForm()
#     if form.validate_on_submit():
#         title = form.title.data
#         comment = form.comment.data
#         new_blogpost_comment = Comment(post_comment=comment,
#                                        blogposts=blogpost_id,
#                                     # user_id=current_user.id,
#                                     user=current_user)
#         # new_post_comment.save_post_comments()
#
#         db.session.add(new_blogpost_comment)
#         db.session.commit()
#     # comments = Comment.query.all()
#     # blogpost_id = id
#
#     comments = Comment.get_comments(blogpost_id)
#     return render_template('blogpostlink.html', title=blogpost.title,
#                            blogpost=blogpost,
#                            blogpost_form=form,
#                            comments=comments)
#
#
# # DELETING A BLOGPOST
#
# @main.route('/blogpost/delete/<int:blogpost_id>' ,methods=['GET', 'POST'])
# @login_required
# def delete_blogpost(blogpost_id):
#     """
#         Delete a department from the database
#         """
#     check_admin()
#
#     blogpost = Blogpost.query.get_or_404(blogpost_id)
#
#     # blogpost = Blogpost.query.filter_by(blogpost_id).one()
#     db.session.delete(blogpost)
#     db.session.commit()
#
#     flash('You have successfully deleted the department.')
#
#     return redirect(url_for('main.blogpost_list', blogpost_id=blogpost.id))
#
#
# # DELETING A COMMENT INSIDE A BLOGPOST
# @main.route('/comment/delete/<int:blogpost_id>' ,methods=['GET', 'POST'])
# @login_required
# def delete_comment(blogpost_id):
#     """
#         Delete a comment from a specific blogpost
#         """
#     check_admin()
#
#     blogposts = Blogpost.query.filter_by(id=blogpost_id).first()
#     comment= Comment.query.filter_by(blogposts=blogpost_id).first()
#
#     db.session.delete(comment)
#     db.session.commit()
#
#     print('deleted')
#
#     flash('You have successfully deleted the comment!')
#
#     return redirect(url_for('main.index'))
#
# # ADDING A NEW COMMENT TO A blogpost
# @main.route('/blogpost/comment/new/<int:id>', methods = ['GET','POST'])
# @login_required
#
# def new_comment(id):
#     '''
#     view category that returns a form to create a new comment
#     '''
#     form = CommentForm()
#     blogpost = Blogpost.query.filter_by(id = id).first()
#
#     if form.validate_on_submit():
#         title = form.title.data
#         comment = form.comment.data
#
#         # comment instance
#         new_comment = Comment(blogpost_id = blogpost.id,
#                               post_comment = comment,
#                               title=title,
#                               user = current_user)
#
#         # save comment
#         new_comment.save_comment()
#
#         return redirect(url_for('.blogposts', id = blogpost.id ))
#
#     title = f'{blogpost.title} comment'
#     return render_template('newcomment.html',
#                            title = title,
#                            comment_form = form,
#                            blogpost = blogpost)
#
# # EDIT A BLOGPOST
# @main.route('/blogpost/edit/<int:id>', methods=['GET', 'POST'])
# @login_required
# def edit_blogpost(id):
#     """
#     Edit a blogpost
#     """
#     check_admin()
#
#     new_blogpost = False
#
#     blogpost = Blogpost.query.get_or_404(id)
#     form = BlogpostForm(obj=blogpost)
#     if form.validate_on_submit():
#         blogpost.title = form.title.data
#         blogpost.content = form.content.data
#         db.session.commit()
#         flash('You have successfully edited the blogpost.')
#
#         # redirect to the departments page
#         return redirect(url_for('main.blogpost_list', blogpost_id=blogpost.id))
#
#     form.content.data = blogpost.content
#     form.title.data = blogpost.title
#     return render_template('newblogpost.html', action="Edit",
#                            new_blogpost=new_blogpost,
#                            blogpost_form=form,
#                            blogpost=blogpost, title="Edit Department")
#
#
# @main.route('/dashboard')
# @login_required
# def dashboard():
#     """
#     Render the dashboard template on the /dashboard route
#     """
#     return render_template('dashboard.html', title="Dashboard")
#
# @main.route('/admin/dashboard')
# @login_required
# def admin_dashboard():
#     # prevent non-admins from accessing the page
#     if not current_user.is_admin:
#         abort(403)
#
#     return render_template('admin_dashboard.html', title="Dashboard")