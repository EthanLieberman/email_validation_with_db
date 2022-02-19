# controller.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.email import Email


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_email',methods=['post'])
def submit_email():
    if not Email.validate_email(request.form):
        # we redirect to the template with the form.
        return redirect('/')

    Email.save(request.form)
    return redirect('/results')

@app.route('/results')
def show_results():
    return render_template('results.html', emails=Email.get_all())


@app.route('/delete/<int:id>')
def delete_email(id):
    data = {
        'id': id
    }
    Email.delete_email(data)
    return redirect('/results')