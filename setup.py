from setuptools import setup
import os
from setuptools.command.install import install

class InstallWithQt(install):
    """Customized setuptools install command - prints a friendly greeting."""
    def run(self):
        print ("INSTALLING python3-pyqt4")
        os.system('sudo apt install python3-pyqt4')
        install.run(self)
        os.system('sudo update-desktop-database /usr/share/applications/')

class NormalInstall(install):
    """Customized setuptools install command - prints a friendly greeting."""
    def run(self):
        install.run(self)

setup(name='debdialer',
      version='0.16',
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
          'vobject'
      ],
      entry_points = {
            'console_scripts': ['debdialer=debdialer:cli_main'],
        },
      data_files = [('/usr/share/applications/',['debdialer.desktop']),
                    ('/usr/share/icons/hicolor/128x128/apps',['Images/deblogo-128.png']),],
      packages=['debdialer'],
      zip_safe=False,
      cmdclass={
        'full-install': InstallWithQt,
        'install': NormalInstall,
        },
      )
