from setuptools import setup, find_packages

# In terminal
# python.exe boto4/setup.py bdist_egg

setup(
    name="boto4",
    version="0.4",
    install_requires=['pandas', 'boto4', 'io']
    )