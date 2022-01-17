from pkg_resources import parse_requirements
from setuptools import setup

install = parse_requirements("requirements.txt")
requirements = [str(ir.req) for ir in install]

setup(
    name='Test',
    version='1.0',
    author='Alina Shevchenko',
    packages=['Calculate'],
    install_requires=requirements,
    scripts=[
        'main.py',
    ]
)
