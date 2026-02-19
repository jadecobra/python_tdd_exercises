import random
import src.learning
import unittest


class TestInfiniteLearningModel(unittest.TestCase):

    def setUp(self):
        self.reality = random.randint(-10**100, 10**100)

    def test_learning_model_when_expectations_are_less_than_reality(self):
        expectations = self.reality - 1

        self.assertGreater(
            src.learning.model(expectations, self.reality),
            self.reality,
            (
                'When expectations are less than reality, '
                'increase expectations until they are greater than reality'
            )
        )

    def test_learning_model_when_expectations_equal_reality(self):
        expectations = self.reality

        self.assertGreater(
            src.learning.model(expectations, self.reality),
            expectations,
            'When expectations equal reality, increase expectations'
        )

    def test_learning_model_when_expectations_are_greater_than_reality(self):
        expectations = self.reality + 1

        self.assertGreater(
            src.learning.model(expectations, self.reality),
            expectations,
            (
                'When expectations are greater than reality, '
                'increase reality until it is greater than expectations'
            )
        )


# Exceptions seen
# AssertionError