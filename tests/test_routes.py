import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        os.environ.setdefault('CHAVE_SESSION', 'test')
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index_redirects_to_cadastro(self):
        response = self.client.get('/', follow_redirects=False)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/cadastarTarefa', response.headers['Location'])

    def test_cadastro_route(self):
        response = self.client.get('/cadastarTarefa')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Criar Novo Question\xc3\xa1rio', response.data)

if __name__ == '__main__':
    unittest.main()
