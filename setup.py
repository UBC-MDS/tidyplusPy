from distutils.core import setup

setup(
    name='tidyplusPy',
    author='Akshi Chaudhary, Yue (Tina) Qian, Xinbin Huang',
    version='v4.0',
    url = 'https://github.com/UBC-MDS/tidyplusPy',
    packages=['tidyplusPy',],
    license='MIT',
    description = 'Extra tools for data wrangling',
    long_description=open('README.txt').read(),
    install_requires = ['numpy','pandas'],
)
