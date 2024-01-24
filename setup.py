from setuptools import setup


setup(
      name='ICLSubFind',    # This is the name of your PyPI-package.
      version='0.0',
      description='Python package for identifying ICL and BCG star particles in SPH simulations',
      author='Ilaria Marini',
      author_email='ilaria.marini@eso.org',
      url="https://github.com/marinilaria/ICLSubFind",
      packages=['ICLSubFind'],
      install_requires=[
            'joblib'
      ],
)