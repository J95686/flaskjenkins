import unittest
from app import app, items

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_item(self):
        self.app.post('/add', data=dict(item='Test Item'))
        self.assertIn('Test Item', items)

    def test_edit_item(self):
        items.append('Old Item')
        self.app.post('/edit/0', data=dict(item='New Item'))
        self.assertEqual(items[0], 'New Item')

    def test_delete_item(self):
        items.append('Item to delete')
        self.app.get('/delete/0')
        self.assertIn('Item to delete', items)

if __name__ == '__main__':
    unittest.main()
