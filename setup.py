from distutils.core import setup
import setuptools


setup(
    name='daytflix',
    version='1.0',
    install_requires=[
        'pyfakefs',
        'requests',
        'beautifulsoup4'
    ],
    packages=[
        'cloudmail',
        'dayt',
        'daytflix'
    ],
    entry_points={
        "console_scripts": [
            "daytflix = daytflix.entry_points:search"
        ]
    },
   )
