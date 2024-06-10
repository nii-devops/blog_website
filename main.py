
import os
from datetime import date, datetime
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey, desc
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from time import sleep
from typing import List


# from dotenv import load_dotenv, dotenv_values
# load_dotenv()


app = Flask(__name__)
#app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

ckeditor = CKEditor(app)
Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)


# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URI")

db = SQLAlchemy(model_class=Base)
db.init_app(app)


# #######################################
# <-------- CONFIGURE TABLES ---------->
# #######################################

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    f_name: Mapped[str] = mapped_column(String(80), nullable=False)
    l_name: Mapped[str] = mapped_column(String(80), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)

    posts = relationship("BlogPost", back_populates="author", cascade='all, delete')
    comments = relationship("Comment", back_populates="comment_author", cascade='all, delete')


# class Category(db.Model):
#     __tablename__ = 'categories'
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

#     # Relationship with Blog Post
#     #posts = db.relationship('Post', backref='category', lazy=True)
#     posts = relationship("BlogPost", back_populates="name", lazy=True)


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('users.id'))
    author = relationship("User", back_populates='posts')

    category: Mapped[str] = mapped_column(String(250), nullable=False)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    #subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    # Relationship with Post Categories
    #category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    # Parent relationship between with Comments
    comments = relationship("Comment", back_populates='parent_post', cascade='all, delete')


class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # ##### <----- Child relationship with User (parent) ----> #######
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('users.id'))
    comment_author = relationship("User", back_populates="comments")
    
    # ####### <----- Child relationship with BlogPost (parent) ----> #######
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('blog_posts.id'))
    parent_post = relationship('BlogPost', back_populates="comments")

    text: Mapped[str] = mapped_column(Text, nullable=False)


with app.app_context():
    db.create_all()



blog_posts = [
    {
        'id': 1,
        'title': 'The Rise of AI: Opportunities and Challenges',
        'author': 'Jane Doe',
        'content': 'Artificial intelligence is transforming industries around the globe. This post explores the opportunities and challenges that AI brings.',
        'date_posted': '2024-05-01'
    },
    {
        'id': 2,
        'title': 'Exploring the Benefits of a Plant-Based Diet',
        'author': 'John Smith',
        'content': 'A plant-based diet offers numerous health benefits. Learn how to transition to a plant-based diet and the positive effects it can have.',
        'date_posted': '2024-05-02'
    },
    {
        'id': 3,
        'title': 'Top 10 Travel Destinations for 2024',
        'author': 'Emily Johnson',
        'content': 'Planning your next vacation? Check out our list of the top 10 travel destinations for 2024.',
        'date_posted': '2024-05-03'
    },
    {
        'id': 4,
        'title': 'How to Improve Your Mental Health',
        'author': 'Michael Brown',
        'content': 'Mental health is crucial for overall well-being. Here are some tips and strategies to improve your mental health.',
        'date_posted': '2024-05-04'
    },
    {
        'id': 5,
        'title': 'The Future of Electric Vehicles',
        'author': 'Sarah Davis',
        'content': 'Electric vehicles are the future of transportation. Discover the latest advancements and trends in the EV industry.',
        'date_posted': '2024-05-05'
    },
    {   'id': 6,
        'title': 'A Guide to Minimalist Living',
        'author': 'David Wilson',
        'content': 'Embrace minimalist living to simplify your life and reduce stress. This guide will help you get started.',
        'date_posted': '2024-05-06'
    },
    {   
        'id': 7,
        'title': 'The Importance of Cybersecurity in Today’s World',
        'author': 'Laura Martinez',
        'content': 'As technology advances, so do cybersecurity threats. Learn why cybersecurity is more important than ever and how to protect yourself.',
        'date_posted': '2024-05-07'
    },
    {
        'id': 8,
        'title': 'Healthy Eating on a Budget',
        'author': 'Robert Garcia',
        'content': 'Eating healthy doesn’t have to be expensive. Find out how you can maintain a nutritious diet without breaking the bank.',
        'date_posted': '2024-05-08'
    },
    {
        'id': 9,
        'title': 'The Benefits of Remote Work',
        'author': 'Jessica Rodriguez',
        'content': 'Remote work offers flexibility and work-life balance. Explore the benefits of remote work and how to make the most of it.',
        'date_posted': '2024-05-09'
    },
    {
        'id': 10,
        'title': 'The Art of Mindfulness: Techniques and Benefits',
        'author': 'Daniel Lee',
        'content': 'Mindfulness can improve your mental and physical health. Learn techniques and benefits of practicing mindfulness.',
        'date_posted': '2024-05-10'
    },
    {
        'id': 11,
        'title': 'Renewable Energy Sources: The Path to a Sustainable Future',
        'author': 'Susan Clark',
        'content': 'Renewable energy is key to combating climate change. Discover different renewable energy sources and their impact on the environment.',
        'date_posted': '2024-05-11'
    },
    {
        'id': 12,
        'title': 'How to Build a Successful Online Business',
        'author': 'James Lewis',
        'content': 'Building an online business can be rewarding and profitable. Follow these steps to create and grow a successful online business.',
        'date_posted': '2024-05-12'
    },
    {
        'id': 13,
        'title': 'The Role of Education in Personal and Professional Growth',
        'author': 'Patricia Walker',
        'content': 'Education is vital for personal and professional development. Learn about the different ways education can impact your life.',
        'date_posted': '2024-05-13'
    },
    {
        'id': 14,
        'title': 'The Impact of Social Media on Society',
        'author': 'Thomas Hall',
        'content': 'Social media has a significant impact on society. Explore the positive and negative effects of social media usage.',
        'date_posted': '2024-05-14'
    },
    {
        'id': 15,
        'title': 'Investing 101: A Beginner’s Guide',
        'author': 'Linda Harris',
        'content': 'Investing can help you build wealth over time. This beginner’s guide will teach you the basics of investing.',
        'date_posted': '2024-05-15'
    },
    {
        'id': 16,
        'title': 'The Evolution of Technology in the Last Decade',
        'author': 'Barbara Young',
        'content': 'Technology has evolved rapidly over the past decade. Take a look at the most significant technological advancements.',
        'date_posted': '2024-05-16'
    },
    {
        'id': 17,
        'title': 'Fitness Tips for a Healthier Lifestyle',
        'author': 'Paul King',
        'content': 'Staying fit is essential for a healthy lifestyle. Here are some fitness tips to help you stay in shape.',
        'date_posted': '2024-05-17'
    },
    {
        'id': 18,
        'title': 'The Importance of Financial Literacy',
        'author': 'Nancy Wright',
        'content': 'Financial literacy is crucial for managing your finances effectively. Learn why financial literacy is important and how to improve yours.',
        'date_posted': '2024-05-18'
    },
    {
        'id': 19,
        'title': 'The Power of Positive Thinking',
        'author': 'Richard Green',
        'content': 'Positive thinking can transform your life. Discover the power of positivity and how to cultivate a positive mindset.',
        'date_posted': '2024-05-19'
    },
    {
        'id': 20,
        'title': 'The Future of Work: Trends and Predictions',
        'author': 'Karen Adams',
        'content': 'The future of work is evolving. Explore the trends and predictions shaping the future of work.',
        'date_posted': '2024-05-20'
    }
]


# Populate Category Table with lit of categories..

"""
def create_categories():
    post_categories = [
        "Art & Culture",
        "DIY & Crafts",
        "Education",
        "Entertainment",
        "Environment & Sustainability",
        "Fashion & Beauty",
        "Finance & Business",
        "Food & Recipes",
        "Health & Wellness",
        "Home & Garden",
        "Lifestyle",
        "News & Politics",
        "Parenting & Family",
        "Personal Development",
        "Pets & Animals",
        "Relationships & Dating",
        "Science & Innovation",
        "Sports & Fitness",
        "Technology",
        "Travel",
        "Others"
        ]

    for cat in post_categories:
        new_cat = Category(
            name=cat
        )
        db.session.add(new_cat)
        db.session.commit()

create_categories()
"""


#Create admin-only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        #Otherwise continue with the route function
        return f(*args, **kwargs)        
    return decorated_function


@app.route("/")
def home():
    return render_template('index.html', title='Home')


@app.route("/login", methods=['get', 'post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        # Check if user exists.
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if user:
            # Check if Password matches that in DB
            if check_password_hash(user.password, password):
                login_user(user)
                flash("Login Successful!", category='success')
                return redirect(url_for('home'))
            else:
                flash("Wrong password! Try again.", category='danger')
        else:
            flash(f"User with email ({email}) does not exist. Register user.", category='danger')
            return redirect(url_for('register'))
    return render_template('login.html', title='Login', form=form)


@app.route("/register", methods=['get', 'post'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        password = form.password.data
        password_2 = form.password_2.data
        if password == password_2:
            new_user = User(
                f_name=form.f_name.data,
                l_name=form.l_name.data,
                email=form.email.data,
                password=generate_password_hash(password, method='scrypt', salt_length=8)
            )
            db.session.add(new_user)
            db.session.commit()
            flash("User Registration Successful", category='success')
            return redirect(url_for('login'))
        else:
            flash("Passwords DO NOT Match. Try Again.", category='danger')
    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/create-post", methods=['get', 'post'])
@login_required
def create_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost( 
            title=form.title.data,
            img_url=form.img_url.data,
            author=current_user,
            category=form.category.data,
            date=date.today().strftime("%B %d, %Y"),
            body=(form.body.data).replace("<p>","").replace("</p>","")
        )
        db.session.add(new_post)
        db.session.commit()
        flash("Post Created Successfully.", category='success')
        return redirect(url_for('posts'))
    return render_template('create-post.html', title='Create Post', form=form)


@app.route('/post/<int:post_id>', methods=['get', 'post'])
def post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    form = CommentForm()
    if form.validate_on_submit():
        # commenter_email = current_user.email
        if not current_user.is_authenticated:
            flash("Submission failed! You need to login or register to comment.", category='warning')
        else:
            comment_time = datetime.now().replace(microsecond=0)
            new_comment = Comment(
                text=(form.text.data).replace("<p>", "").replace("</p>", ""),
                comment_author = current_user,
                parent_post = post
            )
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('post', post_id=post_id, post_time=comment_time))
    result = db.session.execute(db.select(Comment).where(Comment.post_id==post_id))
    comments = result.scalars().all()
    total_comments = len(comments)
    return render_template('post.html', post=post, title=f"Post-{post.id}", form=form, comments=comments, total_comments=total_comments)


@app.route('/posts')
def posts():
    result = db.session.execute(db.select(BlogPost).order_by(desc(BlogPost.id)))
    posts = result.scalars().all()
    return render_template("posts.html", posts=posts, title='All Posts')


@app.route('/cards')
def cards():
    return render_template("cards.html", title='Cards', email='someone@email.com')


@app.route("/purge-database")
def purge_db():
    logout_user()
    result = db.session.execute(db.select(User).order_by(User.id))
    users = result.scalars().all()
    for user in users:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('home'))


@app.route("/delete-comment/<int:comment_id>", methods=['get', 'post'])
@login_required
def delete_comment(comment_id):
    comment = db.get_or_404(Comment, comment_id)
    if comment and comment.comment_author == current_user:
        db.session.delete(comment)
        db.session.commit()
        flash("Comment Deleted Suuccessfully.", category='success')
        return redirect(url_for('posts'))


if __name__ == "__main__":
    app.run(debug=True, port=5050)




