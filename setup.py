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

with open('README.md') as readme_file:
    readme_contents = readme_file.read()

setup(name='debdialer',
      version='0.20',
      description='Click-to-dial pop-up window.',
      long_description = readme_contents,
      long_description_content_type="text/markdown",
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
    classifiers=(
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications :: Telephony',
        'Topic :: Communications :: Internet Phone',
        'Topic :: Utilities'

    )

      )
