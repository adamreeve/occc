OpenCMISS Control Centre
========================

Notes for a possible OpenCMISS graphical interface.

Required parts
--------------
 - Graphical interface for setting up OpenCMISS problems and saving them in a job file.
   Can monitor solve progress then visualise the output produced.

 - Application to read job files and run problems using the OpenCMISS library.
   Can be run in parallel with MPI.


Job files
---------
 - XML files? Wouldn't be simple to write jobs by hand.

 - Link to FieldML files for defining meshes, CellML for constitutive laws, analytic boundary conditions.


CMGUI
-----
 - Uses CMGUI to display a view of the mesh when setting up a problem.
   Can select nodes to apply boundary conditions to using the CMGUI window.

 - Currently the CMGUI library isn't ready for this, can't build interactive applications due to lack
   of multithreading? Not sure about this.
   No Qt interface either, but they're supposedly working on this.


Language Options
----------------
 - C++ with Qt for gui.

 - C++/C/Fortran for job running component

 - Python might be nicer for both but it isn't supported by OpenCMISS or CMGUI yet.


Planning
--------
Store problem types with valid subtypes, same for equations in a header?
We'd have to store integers rather than use the type variable names.
Or should the OpenCMISS library have some way to get valid subtypes for a type, get all valid types.

Maybe a description of the problem types etc should be used by the gui and also used to generate the modules
used by OpenCMISS, but have extra info like descriptions that can be used by the gui

Tree view of problem setup.

Can add multiple problems, with output stored for each problem.
