from gorimboptim import DichotomousLineSearch

class TestDichotomousLineSearch:
    def test_initialization(self):
        def quadratic_func(x):
            return x**2

        interval = [-2, 2]
        ftol = 1e-7
        max_iters = 1e2
        optimizer_obj = DichotomousLineSearch(quadratic_func, interval, ftol,
                                                max_iters)
        assert optimizer_obj.interval == [-2, 2], "interval incorrectly\
        initialized."
        assert optimizer_obj.ftol == 1e-7, "FTol incorrectly\
        initialized."
        assert optimizer_obj.max_iterations == 1e2, "max_iterations incorrectly\
        initialized."
        assert optimizer_obj.cost_function == quadratic_func, "Cost function\
        incorrectly initialized."
        