from setuptools import setup

setup(name='zoopla',
      version='0.5.1',
      description='A simple wrapper for the Zoopla API',
      url='https://github.com/gabalese/zoopla',
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
          'Programming Language :: Python :: 2.7'
      ],
      zip_safe=False)
