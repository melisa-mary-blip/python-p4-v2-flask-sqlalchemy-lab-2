import pytest
from app import app, db
from models import Customer, Item, Review

@pytest.fixture(scope="module")
def app_context():
    with app.app_context():
        yield

class TestReviewModel:
    """Test Review model functionality"""

    def test_create_review(self, app_context):
        # Create customer and item
        c = Customer(name="Reviewer")
        i = Item(name="Item to Review", price=20.0)
        db.session.add_all([c, i])
        db.session.commit()

        # Create review
        r = Review(comment="Excellent!", customer=c, item=i)
        db.session.add(r)
        db.session.commit()

        # Assertions
        assert r.id is not None
        assert r.comment == "Excellent!"
        assert r.customer == c
        assert r.item == i

        # Cleanup
        db.session.delete(r)
        db.session.delete(c)
        db.session.delete(i)
        db.session.commit()
