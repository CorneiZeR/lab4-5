from flask import Flask, render_template, request
from flask_mail import Mail, Message
from forms import ContactForm
import os
SECRET_KEY = os.urandom(32)


app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'kolosyuk1@gmail.com'
app.config['MAIL_PASSWORD'] = 'tmltpbwxlhqogjov'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if request.method == 'POST':
        msg = Message(subject=f'Питання з сайту від {request.form["name"]}',
                      sender=request.form['email'],
                      recipients=['kolosyuk1@gmail.com'],
                      body=f'{request.form["message"]}\n\n\nЛист відправлено з вашого сайту')

        mail.send(msg)
        return render_template('main.html', form=form)
    else:
        return render_template('main.html', form=form)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/projects")
def projects():
    return render_template('projects.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
