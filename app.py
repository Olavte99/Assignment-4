from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from config import Config
from forms import LoginForm, OrderForm

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from models import User, Order
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.password == form.password.data:
                login_user(user)
                return redirect(url_for('order'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
        return render_template('login.html', form=form)

    @app.route('/order', methods=['GET', 'POST'])
    @login_required
    def order():
        form = OrderForm()
        if form.validate_on_submit():
            order = Order(item=form.item.data, quantity=form.quantity.data, user_id=current_user.id)
            db.session.add(order)
            db.session.commit()
            flash('Your order has been placed!', 'success')
            return redirect(url_for('index'))
        return render_template('order.html', form=form)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
