"""
Describes the problem and equation types available in OpenCMISS for use in the graphical interface
"""

class EquationClass:
  def __init__(self,param,name):
    self.param=param
    self.name=name
    self.types=[]

class EquationType:
  def __init__(self,param,name):
    self.param=param
    self.name=name
    self.subtypes=[]

class EquationSubtype:
  def __init__(self,param,name):
    self.param=param
    self.name=name

class ProblemClass:
  def __init__(self,param,name):
    self.param=param
    self.name=name
    self.types=[]

class ProblemType:
  def __init__(self,param,name):
    self.param=param
    self.name=name
    self.subtypes=[]

class ProblemSubtype:
  def __init__(self,param,name):
    self.param=param
    self.name=name
    self.validEquationTypes=[]
    self.validEquationSubtypes=[]

#Problem types
PROBLEM_CLASSICAL_FIELD_CLASS=ProblemClass(4,'Classical field')
PROBLEM_ELASTICITY_CLASS=ProblemClass(1,'Elasticity')

PROBLEM_LAPLACE_EQUATION_TYPE=ProblemType(1,'Laplace\'s equation')
PROBLEM_DIFFUSION_EQUATION_TYPE=ProblemType(5,'Diffusion equation')

PROBLEM_LINEAR_ELASTICITY_TYPE=ProblemType(1,'Linear elasticity')
PROBLEM_FINITE_ELASTICITY_TYPE=ProblemType(2,'Finite elasticity')

PROBLEM_NO_SUBTYPE=ProblemSubtype(0,'No Subtype')

PROBLEM_STANDARD_LAPLACE_SUBTYPE=ProblemSubtype(1,'Standard Laplace\'s equation')
PROBLEM_NO_SOURCE_DIFFUSION_SUBTYPE=ProblemSubtype(1,'No source diffusion')
PROBLEM_LINEAR_SOURCE_DIFFUSION_SUBTYPE=ProblemSubtype(2,'Linear source diffusion')

PROBLEM_QUASISTATIC_FINITE_ELASTICITY_SUBTYPE=ProblemSubtype(1,'Quasistatic Finite Elasticity')

#Equation set types
EQUATIONS_SET_ELASTICITY_CLASS=EquationClass(1,'Elasticity')
EQUATIONS_SET_CLASSICAL_FIELD_CLASS=EquationClass(4,'Classical Field')

EQUATIONS_SET_LINEAR_ELASTICITY_TYPE=EquationType(1,'Linear Elasticity')
EQUATIONS_SET_FINITE_ELASTICITY_TYPE=EquationType(2,'Finite Elasticity')

EQUATIONS_SET_LAPLACE_EQUATION_TYPE=EquationType(1,'Laplace\'s equation')
EQUATIONS_SET_DIFFUSION_EQUATION_TYPE=EquationType(5,'Diffusion equation')

EQUATIONS_SET_NO_SUBTYPE=EquationType(0,'No subtype')

EQUATIONS_SET_MOONEY_RIVLIN_SUBTYPE=EquationSubtype(1,'Mooney-Rivlin constitutive relation')
EQUATIONS_SET_ISOTROPIC_EXPONENTIAL_SUBTYPE=EquationSubtype(2,'Isotropic exponential constitutive relation')

EQUATIONS_SET_STANDARD_LAPLACE_SUBTYPE=EquationSubtype(1,'Standard Laplace\'s equation')
EQUATIONS_SET_NO_SOURCE_DIFFUSION_SUBTYPE=EquationSubtype(1,'No source diffusion')
EQUATIONS_SET_CONSTANT_SOURCE_DIFFUSION_SUBTYPE=EquationSubtype(2,'Constant source diffusion')
EQUATIONS_SET_LINEAR_SOURCE_DIFFUSION_SUBTYPE=EquationSubtype(3,'Linear source diffusion')

#Define the problem type hierarchy
ProblemClasses=[PROBLEM_CLASSICAL_FIELD_CLASS,PROBLEM_ELASTICITY_CLASS]

PROBLEM_CLASSICAL_FIELD_CLASS.types=[PROBLEM_LAPLACE_EQUATION_TYPE,PROBLEM_DIFFUSION_EQUATION_TYPE]
PROBLEM_LAPLACE_EQUATION_TYPE.subtypes=[PROBLEM_STANDARD_LAPLACE_SUBTYPE]
PROBLEM_DIFFUSION_EQUATION_TYPE.subtypes=[PROBLEM_NO_SOURCE_DIFFUSION_SUBTYPE,PROBLEM_LINEAR_SOURCE_DIFFUSION_SUBTYPE]

PROBLEM_ELASTICITY_CLASS.types=[PROBLEM_FINITE_ELASTICITY_TYPE,PROBLEM_LINEAR_ELASTICITY_TYPE]
PROBLEM_FINITE_ELASTICITY_TYPE.subtypes=[PROBLEM_QUASISTATIC_FINITE_ELASTICITY_SUBTYPE]
PROBLEM_LINEAR_ELASTICITY_TYPE.subtypes=[PROBLEM_NO_SUBTYPE]

#Define the equation type hierarchy
EQUATIONS_SET_ELASTICITY_CLASS.types=[EQUATIONS_SET_FINITE_ELASTICITY_TYPE]
EQUATIONS_SET_FINITE_ELASTICITY_TYPE.subtypes=[EQUATIONS_SET_MOONEY_RIVLIN_SUBTYPE,EQUATIONS_SET_ISOTROPIC_EXPONENTIAL_SUBTYPE]

EQUATIONS_SET_CLASSICAL_FIELD_CLASS.types=[EQUATIONS_SET_LAPLACE_EQUATION_TYPE]
EQUATIONS_SET_LAPLACE_EQUATION_TYPE.subtypes=[EQUATIONS_SET_STANDARD_LAPLACE_SUBTYPE]

#Define valid equation types for problems
PROBLEM_STANDARD_LAPLACE_SUBTYPE.validEquationTypes=[EQUATIONS_SET_LAPLACE_EQUATION_TYPE]

PROBLEM_QUASISTATIC_FINITE_ELASTICITY_SUBTYPE.validEquationTypes=[EQUATIONS_SET_FINITE_ELASTICITY_TYPE]
