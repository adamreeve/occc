"""
Description of constants from OpenCMISS
"""

class BoundaryConditionTypes:
  free=(0,"Free")
  fixed=(1,"Fixed")
  fixedInlet=(2,"Fixed inlet")
  fixedOutlet=(3,"Fixed outlet")
  fixedWall=(4,"Fixed wall")
  movedWall=(5,"Moved wall")
  freeWall=(6,"Free wall")
  mixed=(7,"Mixed")
  neumannPoint=(8,"Neumann point")
  neumannIntegrated=(9,"Neumann integrated")
  dirichlet=(10,"Dirichlet")
  cauchy=(11,"Cauchy")
  robin=(12,"Robin")
  fixedIncremented=(13,"Fixed incremented")
  pressure=(14,"Pressure")
  pressureIncremented=(15,"Pressure incremented")
  neumannFree=(16,"Neumann free")
  movedWallIncremented=(17,"Moved wall incremented")
  correctionMassIncrease=(18,"Correction mass increase")
  impermeableWall=(19,"Impermeable wall")

class ControlLoopTypes:
  simple=(1,"Simple")
  fixedLoop=(2,"Fixed loop")
  timeLoop=(3,"Time loop")
  whileLoop=(4,"While loop")
  loadIncrementLoop=(5,"Load increment loop")

class FieldTypes:
  geometric=(1,"Geometric")
  fibre=(2,"Fibre")
  general=(3,"General")
  material=(4,"Material")
