import unittest
from flask_testing import TestCase
from app import create_app
from models import db, Gunpla

class BaseTestCase(TestCase):
    """A base test case for flask-tracking the application."""

    def create_app(self):
        app = create_app()
        # Enable testing mode and disable CSRF for tests
        app.config.update(
            TESTING=True,
            WTF_CSRF_ENABLED=False,
            # Use in-memory SQLite database for tests
            SQLALCHEMY_DATABASE_URI='sqlite:///:memory:',
        )
        return app

    def setUp(self):
        """Set up test database before each test."""
        db.create_all()

    def tearDown(self):
        """Tear down test database after each test."""
        db.session.remove()
        db.drop_all()


class TestViews(BaseTestCase):
    def test_index_get(self):
        """Test that the index page loads correctly."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Verify that the index template is used (Flask-Testing feature)
        self.assert_template_used('index.html')

    def test_create_gunpla(self):
        """Test creating a new Gunpla model."""
        response = self.client.post(
            '/create',
            data={
                'name': "Test Gunpla",
                'series': "Test Series",
                'grade': "Master Grade",
                'scale': "1/100"
            },
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Gunpla model created successfully!', response.data)

        # Check if the Gunpla entry exists in the database using Session.get()
        gunpla = db.session.get(Gunpla, 1)
        self.assertIsNotNone(gunpla)
        self.assertEqual(gunpla.name, "Test Gunpla")
        self.assertEqual(gunpla.series, "Test Series")
        self.assertEqual(gunpla.grade, "Master Grade")
        self.assertEqual(gunpla.scale, "1/100")

    def test_edit_gunpla(self):
        """Test editing an existing Gunpla model."""
        # Create a Gunpla instance first
        gunpla = Gunpla(name="Old Name", series="Old Series", grade="HG", scale="1/144")
        db.session.add(gunpla)
        db.session.commit()

        # Edit the gunpla
        response = self.client.post(
            f'/edit/{gunpla.id}',
            data={
                'name': "New Name",
                'series': "New Series",
                'grade': "MG",
                'scale': "1/100"
            },
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Gunpla model updated successfully!', response.data)

        # Verify the changes in the database using Session.get()
        updated_gunpla = db.session.get(Gunpla, gunpla.id)
        self.assertEqual(updated_gunpla.name, "New Name")
        self.assertEqual(updated_gunpla.series, "New Series")
        self.assertEqual(updated_gunpla.grade, "MG")
        self.assertEqual(updated_gunpla.scale, "1/100")

    def test_delete_gunpla(self):
        """Test deleting a Gunpla model."""
        # Create a Gunpla instance first
        gunpla = Gunpla(name="Delete Model", series="Delete Series", grade="HG", scale="1/144")
        db.session.add(gunpla)
        db.session.commit()

        # Delete the gunpla using POST
        response = self.client.post(
            f'/delete/{gunpla.id}',
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Gunpla model deleted successfully!', response.data)

        # Verify that the gunpla has been removed from the database using Session.get()
        deleted = db.session.get(Gunpla, gunpla.id)
        self.assertIsNone(deleted)


if __name__ == '__main__':
    unittest.main()