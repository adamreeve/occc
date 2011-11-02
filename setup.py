from setuptools import setup, find_packages

setup(
  name = 'OpenCMISS Control Centre',
  version = '0.01',
  description = ('Graphical interface for the OpenCMISS computational '
          'modelling package'),
  author = 'Adam Reeve',
  url = 'http://www.opencmiss.org',
  packages = find_packages(),
  package_data = {'occc': ['resources/*']},
  #PySide doesn't use distutils/setup.py so can't be listed here
  install_requires = [],
  entry_points = {
    'console_scripts': [
      'occc = occc.main:main']})
