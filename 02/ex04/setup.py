from setuptools import setup

setup(
   name='my_minipack',
   version='1.0.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.com',
   packages=['my_minipack'],  #same as name
   install_requires=['wheel'], #external packages as dependencies
)