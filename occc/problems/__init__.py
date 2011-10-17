from collections import OrderedDict
problem_types = OrderedDict()

try:
    from problems.Laplace import StandardLaplaceProblem
except ImportError:
    from ..problems.Laplace import StandardLaplaceProblem

problem_types = {
    'Classical field': {
        'Laplace': {
            'Standard Laplace': StandardLaplaceProblem
            }
        },
    'Elasticity': {
        'Finite Elasticity': {
            }
        }
    }

