# setup.py

from setuptools import setup

setup(name='magicmarc',
	version='0.3',
	description="Magic Marc's Big Package",
	author='Magic Marc',
	author_email='bigdaddy79@gmail.com',
	url='http://www.magicmarc.com',
	packages=['magicmarc',],
	install_requires=['matplotlib'],
	test_suite='tests')
