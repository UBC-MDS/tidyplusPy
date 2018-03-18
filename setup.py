from distutils.core import setup
from setuptools import find_packages

setup(
    name='tidyplusPy',
    author='Akshi Chaudhary, Yue (Tina) Qian, Xinbin Huang',
    version='v4.0',
    packages=['tidyplusPy',],
    url = 'https://github.com/UBC-MDS/tidyplusPy',
    license='MIT',
    description = 'Extra tools for data wrangling',
    long_description=open('README.txt').read(),
    
    install_requires = ['numpy','pandas'],
    include_package_data=True,
)
