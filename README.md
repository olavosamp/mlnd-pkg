# mlnd-pkg
Small distribution building and PyPi packaging experiment

## Usage
gorimboptim module implements DichotomousLineSearch class, a line search optimizer using the Dichotomous Search algorithm.

`from gorimboptim import DichotomousLineSearch`

Constructor arguments include cost function, optimization interval, f (x<up>*</up>) tolerance, and iteration limit.

Method `optimize()` returns optimum point x<up>*</up> for a given cost function and interval.
