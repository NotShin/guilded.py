from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 1 - Planning',
  'Intended Audience :: Developers',
  'Natural Language :: English',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3',
  'Topic :: Software Development :: Libraries',
  'Topic :: Software Development :: Libraries :: Python Modules'
]

setup(
  name='guilded',
  version='0.0.4',
  description='A Python wrapper for the Guilded API',
  long_description=open('README.rst').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type='text/x-rst',
  url='https://github.com/NotShin/guilded.py',
  author='NotShin',
  license='MIT',
  python_requires='>=3.5.3',
  classifiers=classifiers,
  keywords='Guilded', 
  packages=find_packages(),
  install_requires=[''] 
)