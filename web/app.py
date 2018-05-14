from flask import Flask
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig


app = Flask(__name__, static_url_path='/static')
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)


from models import *


@app.route('/', methods=['GET', 'POST'])
def professionals():
    if request.method == 'POST':
        name = request.form['name']
        professional = Professional(name)
        db.session.add(professional)
        db.session.commit()
    _professionals = Professional.query.order_by(Professional.name.desc()).all()
    return render_template('professionals.html', professionals=_professionals)


@app.route('/patients/<int:professional_id>', methods=['GET', 'POST'])
def patients(professional_id):
    if request.method == 'POST':
        name = request.form['name']
        insurance = request.form['insurance']
        sessions = request.form['sessions']
        patient = Patient(name, insurance, sessions, professional_id)
        db.session.add(patient)
        db.session.commit()
    _patients = Patient.query.filter(Patient.professional_id == professional_id)
    return render_template('patients.html', patients=_patients, professional_id=professional_id)


if __name__ == '__main__':
    app.run()
