# models.py

import enum
from app import db


class Months(enum.Enum):
    JAN = 1
    FEB = 2
    MAR = 3
    APR = 4
    MAY = 5
    JUN = 6
    JUL = 7
    AUG = 8
    SEP = 9
    OCT = 10
    NOV = 11
    DEC = 12


class Professional(db.Model):

    __tablename__ = 'Professionals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        self.name = name


class Payment(db.Model):

    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Enum(Months), nullable=False)
    amount = db.Column(db.Numeric)
    date_payed = db.Column(db.DateTime)

    def __init__(self, month, amount, date_payed):
        self.month = month
        self.amount = amount
        self.date_payed = date_payed


class Patient(db.Model):

    __tablename__ = 'Patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    insurance = db.Column(db.String)
    sessions = db.Column(db.Integer)
    professional_id = db.Column(db.Integer, db.ForeignKey(Professional.id))

    def __init__(self, name, insurance, sessions, professional_id):
        self.name = name
        self.insurance = insurance
        self.sessions = sessions
        self.professional_id = professional_id