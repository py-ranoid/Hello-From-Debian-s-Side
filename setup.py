from setuptools import setup

setup(name='debdialer',
      version='0.1',
      description='Click-to-dial pop-up window.',
      url='https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side',
      author='Vishal Gupta',
      author_email='vishalg8897@gmail.com',
      license='GNU',
      install_requires=[
          'pytz',
          'phonenumbers',
      ],

      packages=['debdialer'],
      zip_safe=False)
