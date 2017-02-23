from setuptools import setup

setup(name='zoopla',
      version='0.5',
      description='A simple wrapper for the Zoopla API',
      url='https://github.com/AnthonyBloomer/zoopla',
      author='Anthony Bloomer',
      keywords=['zoopla', 'api'],
      author_email='ant0@protonmail.ch',
      license='MIT',
      packages=['zoopla'],
      install_requires=[
          'requests',
      ],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          "Topic :: Software Development :: Libraries",
          'Programming Language :: Python :: 2.7'
      ],
      zip_safe=False)
