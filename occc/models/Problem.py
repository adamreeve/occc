"""
Stores information for a problem to be solved by OpenCMISS
"""

from QtCore import *
from CMConstants import *

class Problem:
  def __init__(self,name,pclass,ptype,psubtype):
    self.name=name
    self.pclass=pclass
    self.ptype=ptype
    self.psubtype=psubtype

    self.fields=[]
    self.groups=[]
    self.boundaryConditions=[]
    self.rootControlLoop=None
    self.setupProblem()

  def setupProblem(self):
    """
    From the problem class,type and subtype, setup the default/required
    equations, control loops and fields
    """
    pass

class ControlLoop:
  def __init__(self,cltype,parent=None):
    self.cltype=cltype
    self.parent=parent
    self.children=[]
    self.time_start=0.0
    self.time_stop=0.0
    self.time_increment=0.0
    self.fixed_start=0
    self.fixed_stop=0
    self.fixed_increment=0
    self.while_max=0 #also used by load increment loop
  def addChild(self,child):
    self.children.append(child)

class BoundaryCondition:
  def __init__(self,name,group,bctype,value):
    self.name=name
    self.group=group
    self.bctype=bctype
    self.value=value

class Field:
  def __init__(self,ftype):
    self.ftype=ftype

