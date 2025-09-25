import pytest
from app import app, db
from models import Customer, Item, Review

@pytest.fixture(scope="module")
def app_context():
    with app.app_context():
        yield

class TestSerialization:
    """Test that models are serializable"""

    def test_customer_serialization(self, app_context):
        c = Customer(name="Serialize Me")
        db.session.add(c)
        db.session.commit()

        serialized = c.to_dict()
        assert "name" in serialized
        assert serialized["name"] == "Serialize Me"

        db.session.delete(c)
        db.session.commit()

    def test_item_serialization(self, app_context):
        i = Item(name="Serializable Item", price=15.5)
        db.session.add(i)
        db.session.commit()

        serialized = i.to_dict()
        assert "name" in serialized and "price" in serialized
        assert serialized["price"] == 15.5

        db.session.delete(i)
        db.session.commit()

    def test_review_serialization(self, app_context):
        c = Customer(name="Reviewer")
        i = Item(name="Item", price=30.0)
        r = Review(comment="Loved it!", customer=c, item=i)
        db.session.add_all([c, i, r])
        db.session.commit()

        serialized = r.to_dict()
        assert serialized["comment"] == "Loved it!"
        assert serialized["customer_id"] == c.id
        assert serialized["item_id"] == i.id

        db.session.delete(r)
        db.session.delete(c)
        db.session.delete(i)
        db.session.commit()
