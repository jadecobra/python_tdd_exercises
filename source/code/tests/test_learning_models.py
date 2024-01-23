import learning
import unittest


class TestInfiniteLearningModel(unittest.TestCase):

    def test_learning_model_when_expectations_are_less_than_reality(self):
        '''When expectations are less than reality,
        increase expectations until they are greater than reality'''

        reality = 1
        expectations = reality - 1

        self.assertGreater(
            learning.model(expectations, reality),
            reality
        )

    def test_learning_model_when_expectations_equal_reality(self):
        '''When expectations equal reality, increase expectations'''

        reality = 1
        expectations = reality

        self.assertGreater(
            learning.model(expectations, reality),
            expectations
        )

    def test_learning_model_when_expectations_are_greater_than_reality(self):
        """When expectations are greater than reality,
        increase reality until it is greater than expectations"""

        reality = 0
        expectations = reality + 1

        self.assertGreater(learning.model(expectations, reality), expectations)
