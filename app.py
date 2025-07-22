from flask import Flask, render_template, redirect, url_for, flash
from forms import ComplaintForm
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/', methods=['GET', 'POST'])
def register_complaint():
    form = ComplaintForm()
    if form.validate_on_submit():
        complaint_id = f"CMP{random.randint(1000, 9999)}"
        flash(f"Complaint registered successfully! Your complaint number is {complaint_id}.", "success")
        return redirect(url_for('register_complaint'))
    return render_template('complaint.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
