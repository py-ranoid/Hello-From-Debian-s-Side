from setuptools import setup

setup(name='debdialer',
      version='0.1',
      description='Click-to-dial pop-up window.',
      url='https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side',
      author='Vishal Gupta',
      author_email='vishalg8897@gmail.com',
      license='GNU',
      package_data={'debdialer': ['resources/DialerCodes.json','resources/flags/*']},
      include_package_data=True,
      install_requires=[
          'pytz',
          'phonenumbers',
      ],
      # scripts=['bin/funniest-joke'],
      entry_points = {
            'console_scripts': ['debdialer=debdialer:cli_main'],
        },
      packages=['debdialer'],
      zip_safe=False
      )
