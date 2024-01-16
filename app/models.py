from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String,nullable=False)
    super_name=db.Column(db.String, nullable=False)
    created_at=db.Column(db.DateTime)
    updated_at=db.Column(db.DateTime, nullable=True)

    powers= db.relationship('HeroPower', back_populates='hero')


class HeroPower(db.Model):
    __tablename__='hero_powers'

    id=db.Column(db.Integer, primary_key=True)
    strength=db.Column(db.String, nullable=False)
    hero_id=db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id=db.Column(db.Integer, db.ForeignKey('powers.id'))
    created_at=db.Column(db.DateTime)
    updated_at=db.Column(db.DateTime, nullable=True)

    hero=db.relationship('Hero', back_populates='powers')
    power=db.relationship('Power', back_populates='heroes')

    @validates('strength')
    def validate_strength(self, key, value):
        assert value in ['Strong', 'Weak', 'Average'], f"Invalid strength value: {value}"
        return value

class Power(db.Model):
    __tablename__='powers'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    description=db.Column(db.String)
    created_at=db.Column(db.DateTime)
    updated_at=db.Column(db.DateTime, nullable=True)

    heroes= db.relationship('HeroPower', back_populates='power')

    @validates('description')
    def validate_description(self, key,  value):
        assert value and len(value) >= 20, "Description must be present and at least 20 characters long"
        return value