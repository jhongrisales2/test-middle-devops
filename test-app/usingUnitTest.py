from unittest import TestCase

class Math:
    def sum(num1: int, num2: int) -> int:
        return num1 + num2

class TestMath(TestCase):
    def setUp(self):
        # Este código se ejecutará antes de cada test, y nos ayuda a preparar
        # nuestro un escenario genérico sobre el que ejecutar nuestro testing.
        self.math = Math()

    def test_sum_is_working(self):
        self.assertEqual(self.math.sum(1, 2), 3)