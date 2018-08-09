from setuptools import setup
import os
from setuptools.command.install import install

def install_dmenu():
    print ("INSTALLING dmenu")
    os.system('sudo apt install dmenu')

def install_qt():
    print ("INSTALLING python3-pyqt4")
    os.system('sudo apt install python3-pyqt4')

def install_kdeconnect():
    print ("INSTALLING kdeconnect")
    os.system('sudo apt install kdeconnect indicator-kdeconnect')


def update_mime():
    print ("UPDATING DESKTOP DATABASE")
    os.system('sudo update-desktop-database /usr/share/applications/')

class InstallWithQt(install):
    """Install debdialer with PyQt only"""
    def run(self):
        install_qt()
        install.run(self)

class InstallWithQtDmenu(install):
    """Install debdialer with PyQt and dmenu"""
    def run(self):
        install_qt()
        install_dmenu()
        install_kdeconnect()
        install.run(self)

class InstallWithDmenu(install):
    """Install debdialer with Dmenu only"""
    def run(self):
        install_dmenu()
        install.run(self)

class NormalInstall(install):
    """Install debdialer only."""
    def run(self):
        install.run(self)

with open('README.md') as readme_file:
    readme_contents = readme_file.read()

setup(name='debdialer',
      version='0.26',
      description='Click-to-dial pop-up window.',
      long_description = readme_contents,
      long_description_content_type="text/markdown",
      url='https://salsa.debian.org/comfortablydumb-guest/debdialer',
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
      data_files = [('/etc/',['debdialer.conf']),
                    ('/usr/share/applications/',['debdialer.desktop']),
                    ('/usr/share/icons/hicolor/128x128/apps',['Images/deblogo-128.png']),],
      packages=['debdialer'],
      zip_safe=False,
      cmdclass={
        'full_install': InstallWithQtDmenu,
        'install': NormalInstall,
        'gui_install': InstallWithQt,
        'nogui_install': InstallWithDmenu,
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
