from collections import OrderedDict


problem_types = OrderedDict()
try:
    from problems.laplace import StandardLaplaceProblem
except ImportError:
    from ..problems.laplace import StandardLaplaceProblem

problem_types = {
    'Classical field': {
        'Laplace': {
            'Standard Laplace': StandardLaplaceProblem}},
    'Elasticity': {
        'Finite Elasticity': {}}}
