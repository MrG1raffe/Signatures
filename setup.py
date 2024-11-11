from setuptools import setup, find_packages

setup(
   name='signatures',
   version='1.0',
   description='Option pricing models',
   author='MrG1raffe',
   author_email='dimitri.sotnikov@gmail.com',
   packages=find_packages(),
   install_requires=[
      'numpy>=1.23.0',
      'typing',
      'matplotlib',
      'numba>=0.58.1',
   ], #external packages as dependencies
)