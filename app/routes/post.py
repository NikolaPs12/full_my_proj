from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..extensions import db
from ..models.post import Post
from ..forms import PostForm
from ..models.user import User

posts = Blueprint('post', __name__)

@posts.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        user_id = request.form.get('user_id', current_user.id)
        
        post = Post(title=title, content=content, user_id=user_id)
        try:
            db.session.add(post)
            db.session.commit()
            flash('Пост успешно создан!', 'success')
            return redirect(url_for('main.index')) 
        except Exception as e:
            db.session.rollback()
            flash(f'Ошибка при создании поста: {str(e)}', 'danger')
            return render_template("post/create_post.html") 
    return render_template("post/create_post.html")  

@posts.route('/view_posts', methods=['GET', 'POST'])
def view_posts():
    posts = Post.query.order_by(Post.created_at).limit(200).all()

    return render_template("post/view_posts.html", posts=posts, user=current_user)


@posts.route('/view_post/<int:id>/post_update', methods=['GET', 'POST'])
@login_required
def post_update(id):
    post = Post.query.get(id)
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')

        try:
            db.session.commit()
            flash('Пост успешно обновлен!', 'success')
            return redirect(url_for('post.view_posts'))
        except Exception as e:
            print(str(e))
    return render_template("post/post_update.html", post=post)

@posts.route('/view_post/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete(id):
    post = Post.query.get(id)
    try:
        db.session.delete(post)
        db.session.commit()
        flash('Пост успешно удален!', 'success')
        return redirect(url_for('post.view_posts'))
    except Exception as e:
        print(str(e))
