OpenCMISS Control Centre
========================

Notes on a possible OpenCMISS graphical interface and trying some things out with
PySide, the Qt bindings for Python.

Requirements
------------

 - Graphical interface for setting up OpenCMISS problems, applying boundary conditions, setting solver options.

 - Apply boundary conditions by selecting faces, nodes with CMGUI.

 - Can configure jobs to run over a network on multiple machines with MPI, or with MPI locally.

 - Can monitor solve progress then visualise the output produced using CMGUI.

 - Will need either an application that reads and runs OpenCMISS jobs or could just use Python
   scripts with the OpenCMISS Python bindings.

 - Link to FieldML files for defining meshes, and CellML for constitutive laws and analytic boundary conditions.

Planning
--------

For different problem types, could use Jinja2 templates to create a Python script to solve the problem.

Tree view of problem setup, under each problem have geometry, boundary conditions, generated scripts, outputs.

Can add multiple problems, with output stored for each problem. Maybe set a working directory for each problem.
