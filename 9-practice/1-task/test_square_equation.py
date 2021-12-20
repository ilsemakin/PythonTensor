import square_equation as sq

class TestEquation:
    def test_equation_0_0_0(self):
        assert not sq.solve_square_equation(0, 0, 0)

    def test_equation_1_5_6(self):
        solution = sq.solve_square_equation(1, 5, 6)
        assert solution == [-2.0, -3.0]

    def test_equation_1_20_84(self):
        solution = sq.solve_square_equation(1, -20, 84)
        assert solution == [14.0, 6.0]

    def test_equation_1_20_100(self):
        solution = sq.solve_square_equation(1, -20, 100)
        assert solution == [10.0, 10.0]

    def test_equation_1_2_10(self):
        solution = sq.solve_square_equation(1, 2, 10)
        assert solution == [complex(-1.0, 3.0), complex(-1, -3.0)]