import math
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


    def test_optim_quadratic(self):
        def quadratic_func(x):
            return x**2

        interval = [-2, 2]
        ftol = 1e-8
        max_iters = 1e2
        optimizer_obj = DichotomousLineSearch(quadratic_func, interval, ftol,
                                                max_iters)
        x_opt = optimizer_obj.optimize()
        x_target = 0
        
        print(x_opt)
        print("iters: ", optimizer_obj.iteration_counter)
        print("fevals: ", optimizer_obj.f_evals)
        assert abs(x_opt - x_target) <= ftol , f"Optimization failed for\
        quadratic_func in {interval}."


    def test_off_interval_optim_quadratic(self):
        def quadratic_func(x):
            return x**2

        interval = [-6, -4]
        ftol = 1e-8
        max_iters = 1e2
        optimizer_obj = DichotomousLineSearch(quadratic_func, interval, ftol,
                                                max_iters)
        x_opt = optimizer_obj.optimize()
        x_target = -4
        pass_condition = abs(x_opt - x_target) <= ftol
        
        print(x_opt)
        print("iters: ", optimizer_obj.iteration_counter)
        print("fevals: ", optimizer_obj.f_evals)
        assert  pass_condition, f"Optimization failed for\
        off-interval quadratic_func in {interval}."


    def test_optim_shifted_quadratic_abs(self):
        def shifted_quadratic_abs_func(x):
            return abs(x-1)**2-2

        interval = [-2, 1.5]
        ftol = 1e-7
        max_iters = 1e2
        optimizer_obj = DichotomousLineSearch(shifted_quadratic_abs_func, 
                                                interval, ftol, max_iters)
        x_opt = optimizer_obj.optimize()
        x_target = 1
        pass_condition = abs(x_opt - x_target) <= ftol
        
        print(x_opt)
        print("iters: ", optimizer_obj.iteration_counter)
        print("fevals: ", optimizer_obj.f_evals)
        assert pass_condition , f"Optimization failed for\
        shifted_quadratic_abs_func in {interval}."
         
         
    def test_optim_exp_func(self):
        def exp_func(x):
            return math.exp(2*x+1)

        interval = [-0.5, 3]
        ftol = 0
        max_iters = 5
        optimizer_obj = DichotomousLineSearch(exp_func, interval, ftol,
                                                max_iters)
        x_opt = optimizer_obj.optimize()
        x_target = -0.5
        pass_condition = abs(x_opt - x_target) <= ftol
        
        print(x_opt)
        print("iters: ", optimizer_obj.iteration_counter)
        print("fevals: ", optimizer_obj.f_evals)
        assert pass_condition , f"Optimization failed for\
         exp_func in {interval}."
         
    # def test_optim_(self):
        # def _func(x):
            # return 

        # interval = []
        # ftol = 1e-8
        # max_iters = 1e2
        # optimizer_obj = DichotomousLineSearch(quadratic_func, interval, ftol,
                                                # max_iters)
        # x_opt = optimizer_obj.optimize()
        # x_target = 0
        # assert abs(x_opt - x_target) <= ftol , f"Optimization failed for\
         # in {interval}."
         
    