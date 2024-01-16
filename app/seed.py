from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db,Hero, Power, HeroPower
from random import choice

from app import app

def seed_powers():
  with app.app_context():
    print("🦸‍♀️ Seeding powers...")
    powers_data=[
      { "name": "super strength", "description": "gives the wielder super-human strengths" },
      { "name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed" },
      { "name": "super human senses", "description": "allows the wielder to use her senses at a super-human level" },
      { "name": "elasticity", "description": "can stretch the human body to extreme lengths" }
    ]
    powers = [Power(**data, created_at=datetime.utcnow(), updated_at=datetime.utcnow()) for data in powers_data]
    db.session.add_all(powers)
    db.session.commit()

def seed_heroes():
  with app.app_context():
    print("🦸‍♀️ Seeding heroes...")
    heroes_data=[
      { "name": "Kamala Khan", "super_name": "Ms. Marvel" },
      { "name": "Doreen Green", "super_name": "Squirrel Girl" },
      { "name": "Gwen Stacy", "super_name": "Spider-Gwen" },
      { "name": "Janet Van Dyne", "super_name": "The Wasp" },
      { "name": "Wanda Maximoff", "super_name": "Scarlet Witch" },
      { "name": "Carol Danvers", "super_name": "Captain Marvel" },
      { "name": "Jean Grey", "super_name": "Dark Phoenix" },
      { "name": "Ororo Munroe", "super_name": "Storm" },
      { "name": "Kitty Pryde", "super_name": "Shadowcat" },
      { "name": "Elektra Natchios", "super_name": "Elektra" }
    ]
    heroes = [Hero(**data, created_at=datetime.utcnow(), updated_at=datetime.utcnow()) for data in heroes_data]
    db.session.add_all(heroes)
    db.session.commit()


def seed_hero_powers():
  with app.app_context():
    print("🦸‍♀️ Adding powers to heroes...")
    strengths = ["Strong", "Weak", "Average"]
    heroes= Hero.query.all()
    for hero in heroes:
      for _ in range(choice([1, 2, 3])):  # Randomly choose 1, 2, or 3 powers for each hero
          power = Power.query.order_by(db.func.random()).first()
          hero_power = HeroPower(hero_id=hero.id, power_id=power.id, strength=choice(strengths), created_at=datetime.utcnow(), updated_at=datetime.utcnow())
          db.session.add(hero_power)
    db.session.commit()


if __name__ == '__main__':
    seed_powers()
    seed_heroes()
    seed_hero_powers()
    print("🦸‍♀️ Done seeding!")
