import unittest
from models.model import LogisticRegression

class TestModel(unittest.TestCase):
    def test_model_initialization(self):
        model = LogisticRegression()
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()
