from flask import render_template,redirect,url_for,abort,request
from . import main
from flask_login import login_required,current_user
from .forms import BlogForm,CommentForm,UpdateForm
from ..models import User,Blog,Comment,Subscriber
from ..request import get_quotes
from .. import db
from ..email import mail_message

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    blogs = Blog.query.all()
    form = UpdateForm()
    return render_template('index.html',blogs = blogs,update_form = form)

@main.route('/contact',methods = ["GET","POST"])
@login_required
def mail():
    form = UpdateForm()
    if form.validate_on_submit():
        sub = Subscriber(email = form.email.data, username = form.username.data)
        db.session.add(sub)
        db.session.commit()

        mail_message("Thank you for subscibing to our email","email/welcome_user",sub.email,sub=sub)

        return redirect(url_for('main.index'))
    return render_template('contact.html',update_form = form)

@main.route('/new/blog', methods = ['GET','POST'])
@login_required
def new_blog():

    form = BlogForm()
    if form.validate_on_submit():
        blog = form.blog.data
        category = form.category.data
        title = form.title.data
        
        
        new_blog = Blog(blog = blog,title = title,category = category)
        new_blog.save_blog()
        
        user = current_user
        mail_message("New Post on the Blog","email/new_post",user.email,user=user,new_blog = new_blog)

        return redirect(url_for('main.index'))

    return render_template('new_blog.html',blog_form = form)

@main.route('/blogs')
def blogs():

    blogs = Blog.query.all()
    return render_template('blog.html',blogs = blogs)

@main.route('/blog/comments/<int:blogs_id>', methods = ['GET','POST'])
@login_required
def comment(blogs_id):
    form = CommentForm()
    blogs = Blog.query.get(blogs_id)
    all_comments = Comment.query.filter_by(blogs_id = blogs_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        blogs_id = blogs_id
        
        new_comment = Comment(comment = comment,blogs_id = blogs_id)
        
        new_comment.save_comment()

        

        return redirect(url_for('.comment',blogs_id = blogs_id))


    return render_template('comment.html',comment_form = form, blogs = blogs, all_comments = all_comments)

@main.route('/about_me')
def about():

    return render_template('about_me.html')

@main.route('/quotes')
def quotes():

    quotes = get_quotes()
    return render_template('quotes.html',quotes = quotes)

@main.route('/collection')
def collection():

    return render_template('collection.html')

@main.route('/blog/delete/<blogs_id>', methods=['GET', 'POST'])
@login_required
def delete_blog(blogs_id):
    blog = Blog.query.get_or_404(blogs_id)
    # if blog.user != current_user:
    #     abort(404)
    blog.delete()
    return redirect(url_for('main.blogs'))

@main.route('/comment/delete/<comments_id>', methods=['GET', 'POST'])
@login_required
def delete_comment(comments_id):
    comment = Comment.query.get_or_404(comments_id)
    # if blog.user != current_user:
    #     abort(404)
    comment.delete()
    return redirect(url_for('main.blogs'))