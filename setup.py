from setuptools import setup


setup(
    name='avelunch',
    version='1.0',
    install_requires=[
        'bcrypt',
        'flask_assets',
        'jsmin',
        'flask',
        'avenyn-lunch'
    ],
    packages=[
        'avelunch'
    ],
    entry_points={
        'console_scripts': [
        ]
    }
)
