# server/models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

# Initialize the SQLAlchemy db instance
db = SQLAlchemy()


class Customer(db.Model, SerializerMixin):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # Relationship to Review
    reviews = db.relationship("Review", back_populates="customer", cascade="all, delete-orphan")

    # Association proxy to access items directly from a customer
    items = association_proxy('reviews', 'item')

    # SerializerMixin rules to avoid circular serialization
    serialize_rules = ('-reviews.customer',)


class Item(db.Model, SerializerMixin):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)

    # Relationship to Review
    reviews = db.relationship("Review", back_populates="item", cascade="all, delete-orphan")

    serialize_rules = ('-reviews.item',)


class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String, nullable=False)

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    customer = db.relationship("Customer", back_populates="reviews")
    item = db.relationship("Item", back_populates="reviews")

    serialize_rules = ('-customer.reviews', '-item.reviews')
