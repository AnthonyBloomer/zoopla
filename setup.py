# -*- coding: utf-8 -*-

from setuptools import setup, Command
import os
import sys
from shutil import rmtree

here = os.path.abspath(os.path.dirname(__file__))

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


class PublishCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        sys.exit()


setup(name='zoopla',
      version='0.6.2',
      description='A Python wrapper for the Zoopla API',
      long_description=long_descr,
      url='https://github.com/anthonybloomer/zoopla',
      author='Anthony Bloomer, Gabriele Alese',
      keywords=['zoopla', 'api'],
      author_email='ant0@protonmail.ch, gabriele@alese.it',
      license='MIT',
      packages=['zoopla'],
      install_requires=[
          'marshmallow==2.13.6',
          'requests==2.11.1'
      ],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          "Topic :: Software Development :: Libraries",
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6'
      ],
      cmdclass={
          'publish': PublishCommand,
      },
      zip_safe=False)
