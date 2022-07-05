from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
	name='my_minipack',
	version='1.0.0',
	description='Howto create a package in python',
	home_page='None',
	long_description=long_description,
	author='arangoni',
	author_email='arangoni@student.42lyon.fr',
	license='GPLv3',
	location=here,
	classifiers=[
        'Development Status :: 3 - Alpha',
        'License ::  OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Topic :: Loading Bar :: Logger :: HowTo :: Package',
		'Intended Audience :: Students',
      ],
	package_dir={"": "my_minipack"},
	py_modules=['logger', 'progress', 'ImageProcessor', 'csvreader'],
	python_requires='>=3',
)