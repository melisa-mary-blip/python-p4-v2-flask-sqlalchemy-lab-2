import pytest
from app import app, db
from models import Customer, Item, Review

@pytest.fixture(scope="module")
def app_context():
    with app.app_context():
        yield

class TestAssociationProxy:
    """Customer in models.py"""

    def test_has_association_proxy(self, app_context):
        """Customer has association proxy to items"""
        # Create customer and item
        c = Customer(name="Test Customer")
        i = Item(name="Test Item", price=10.0)
        db.session.add_all([c, i])
        db.session.commit()

        # Create review linking them
        r = Review(comment="Great item!", customer=c, item=i)
        db.session.add(r)
        db.session.commit()

        # Assertions
        assert hasattr(c, 'items')
        assert i in c.items

        # Cleanup
        db.session.delete(r)
        db.session.delete(c)
        db.session.delete(i)
        db.session.commit()
