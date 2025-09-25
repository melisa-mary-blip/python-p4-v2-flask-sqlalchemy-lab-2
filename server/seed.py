#!/usr/bin/env python3
 
# seed.py
from app import app, db
from models import Customer, Item, Review

with app.app_context():
    # Clear existing data
    Review.query.delete()
    Customer.query.delete()
    Item.query.delete()
    db.session.commit()

    # Create customers
    customer1 = Customer(name="Tal Yuri")
    customer2 = Customer(name="Ava Smith")
    db.session.add_all([customer1, customer2])

    # Create items
    item1 = Item(name="Laptop Backpack", price=49.99)
    item2 = Item(name="Insulated Coffee Mug", price=9.99)
    db.session.add_all([item1, item2])
    db.session.commit()

    # Create reviews
    review1 = Review(comment="Great backpack!", customer=customer1, item=item1)
    review2 = Review(comment="Love this mug!", customer=customer1, item=item2)
    review3 = Review(comment="Nice mug!", customer=customer2, item=item2)
    db.session.add_all([review1, review2, review3])
    db.session.commit()

    print("Seed data added")
