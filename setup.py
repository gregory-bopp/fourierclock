from setuptools import setup

setup(
	name='fclock',
	version='0.1dev',
	packages=['fclock',],
	install_requires=[
            'matplotlib==3.1.2',
			'numpy',
			'scipy',
			'scikit-image'
        ],
	license='Creative Commons Attribution-Noncommercial-Share Alike license',
	long_description=open('README.md').read()
	)

