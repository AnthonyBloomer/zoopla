from setuptools import setup

setup(name='zoopla',
      version='0.4',
      description='A simple wrapper for the Zoopla API',
      url='https://github.com/AnthonyBloomer/zoopla',
      author='Anthony Bloomer',
      author_email='ant0@protonmail.ch',
      license='MIT',
      packages=['zoopla'],
      install_requires=[
            'requests',
      ],
      zip_safe=False)
