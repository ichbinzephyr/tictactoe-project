import unittest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from src.app import app, game

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Tic-Tac-Toe', response.data)

    def test_move_success(self):
        response = self.app.post('/move', json={'square': [0, 0], 'letter': 'X'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'success')
        self.assertIsNone(response.json['winner'])

    def test_move_failure(self):
        game.make_move((0, 0), 'X')
        response = self.app.post('/move', json={'square': [0, 0], 'letter': 'O'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'failure')

    def test_winner(self):
        game.board = [['X', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        response = self.app.post('/move', json={'square': [0, 2], 'letter': 'X'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'success')
        self.assertEqual(response.json['winner'], 'X')

if __name__ == '__main__':
    unittest.main()
