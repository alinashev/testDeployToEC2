from setuptools import setup


setup(
    name='Test',
    version='1.0',
    author='Alina Shevchenko',
    packages=['Calculate'],
    install_requires=[
        'numpy~=1.22.1',
    ],
    scripts=[
        'main.py',
    ]
)
