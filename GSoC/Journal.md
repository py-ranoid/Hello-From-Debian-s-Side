Note : Find project scrum board [here](https://storm.debian.net/grain/bD3aJdnYLBWo5R3K6GWckn/b/sandstorm/libreboard)

---
# Week 1

---
# Setup

## Installing SIP
Download from here : https://riverbankcomputing.com/software/sip/download
<br/>Installation instructions : http://pyqt.sourceforge.net/Docs/sip4/installation.html

	wget https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.7/sip-4.19.7.tar.gz
	tar -xvzf sip-4.19.7.tar.gz
	cd sip-4.19.7
	python configure.py
	make
	make install

	cd ..
	rm -rf sip-4.19.7
	rm sip-4.19.7.tar.gz

## Installing PyQt4
Download from here : https://riverbankcomputing.com/software/pyqt/download
<br/>Installation instructions : http://pyqt.sourceforge.net/Docs/PyQt4/installation.html

	wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.1/PyQt4_gpl_x11-4.12.1.tar.gz
	tar -xvzf PyQt4_gpl_x11-4.12.1.tar.gz
	cd PyQt4_gpl_x11-4.12.1
	python configure.py
	cd ..
	rm -rf PyQt4_gpl_x11-4.12.1
	rm PyQt4_gpl_x11-4.12.1.tar.gz
Note :
Use `--sipdir ` to specify an sip path
Use `-q` to specify an sip path
For example, here's what worked for me :

	 sudo /usr/bin/python configure.py --sipdir /usr/share/sip -q /home/b/anaconda2/bin/qmake
Make and install  

	make
	make install

## Installing QtDesigner
	$ apt-get install python-qt4 pyqt4-dev-tools qt4-designer
Reference : https://nikolak.com/pyqt-qt-designer-getting-started/

# Making the Dialer

- Open QtDesigner and design the Dialer.
- Save the UI as `designui.ui`
- Convert UI to Python script
	` pyuic4 designui.ui -o design.py`


![](https://py-ranoid.github.io/Hello-From-The-Debian-Side/Images/Screenshot from 2018-03-27 13-12-38.png)


# Mime Handling
URI Schemes Wiki : https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Official_IANA-registered_schemes<br>
`tel:` URI documentation : http://www.ietf.org/rfc/rfc3966.txt<br>
`sip:` (or `sips:`) is the official URI scheme for SIP<br>
`callto` is the one used by skype (Source)

Record to be added  :

	x-scheme-handler/tel=debdialer.desktop

I tried using xdg-mime for this. The end of `man xdg-mime` has a snippet to add a file type description for "shiny"-files. "shinythings-" is used as the vendor prefix. The file type description could look as follows.

           shinythings-shiny.xml:

           <?xml version="1.0"?>
           <mime-info xmlns='http://www.freedesktop.org/standards/shared-mime-info'>
             <mime-type type="text/x-shiny">
               <comment>Shiny new file type</comment>
               <glob pattern="*.shiny"/>
               <glob pattern="*.shi"/>
             </mime-type>
           </mime-info>


	> xdg-mime install shinythings-shiny.xml


### Creating a desktop entry

	/usr/share/applications/debdialer.desktop :

	[Desktop Entry]
	Version=1.0
	Name=Pop-Up Dialer
	Comment=An application to handle tel: URIs and dial numbers
	Exec=/usr/bin/python /home/b/gitpository/DebianDialer/dialer_main.py
	Path=/home/b/gitpository/DebianDialer/
	Icon=/home/b/gitpository/DebianDialer/Images/deblogo.png
	Terminal=false
	Type=Application
	Categories=Utility;Development;

### Setting default application for tel links with xdg-mime

Hence the required XML file for

	debdialer-tel.xml:

	<?xml version="1.0"?>
	<mime-info xmlns='http://www.freedesktop.org/standards/shared-mime-info'>
		<mime-type type="x-scheme-handler/tel=debdialer.desktop">
			<comment>Invoking Debian Dialer</comment>
			<glob pattern="tel:\*"/>
		</mime-type>
	</mime-info>

	>> xdg-mime install debdialer-tel.xml

### Testing the MIME URI
- `xdg-mime query default x-scheme-handler/tel`
- `xdg-open tel:873811`

---
# Week 2

---
# Fetching Phone Number details

## Libraries
### [libphonenumber](https://github.com/googlei18n/libphonenumber)
Google's common Java, C++ and JavaScript library for parsing, formatting, and validating international phone numbers. The Java version is optimized for running on smartphones, and is used by the Android framework since 4.0

### [python-phonenumbers](https://superuser.com/questions/159775/is-there-a-firefox-shortcut-to-copy-the-url-of-thecurrent-page)
This is a Python port of libphonenumber and supports Python 2.5-2.7 and Python 3.x<br>
Installation :
	`pip install phonenumbers`

Created a script called `fetch_details.py` to call methods of `phonenumbers`. These methods are used to fetch details about a phone number. Before performing any operations, we must generate a `PhoneNumber` object from the phone number and the country the phone number is being dialled from (unless the number is in E.164 format, which is globally unique). <br> This presents a new obstacle since a country code now needs to be assigned to the number if it isn't in  E.164 format.
<br>
I plan to display the following details of a phone number (presuming it is in E.164 format)
- Timezone
	- Done
	- Displaying Timezone name and UTC Offset
- Carrier
	- Done
	- Displaying Carrier Name
- Country
	- Incomplete
	- Have not been able to get the two letter country code
	- Once I have the country code, I can also display the flag

# Displaying Phone Number details
## About GUI
- `Ui_Dialog` in `design2.py` contains the structure and components of the GUI and is generated automatically by `pyuic4` from `design2.ui`
- `DialerApp` in `dialer_main.py` inherits `QtGui.QDialog` and generates a PyQt4 Dialog using`Ui_Dialog`.
- Since `design2.py` is over-writted every time the `design2.ui` is compiled, all the methods and functional properties of the Buttons and Textboxes is assigned in `DialerApp`.

## GUI Initialisation
- `object_map` is a dictionary to map key values to GUI components. If the component variable names change in the future, `DialerApp` will remain unaffected with the exception of `objectMapSetup`.
- Numeric buttons are connected to `click_action` with number value as an argument.

## Fetch Details button
- The "**Fetch Details**" button is mapped to the `setDetails` functions which calls other methods to fetch and set details.
- I plan to trigger the button when the contents of "NumTextBox" changes.
- Functionality
	- Formats the number
	- Sets Timezone
	- Sets Carrier

---
# Week 3

---
# Triggering `setDetails`
##### Goal : Format and fetch details about a number implicitly for every change
- This was achieve by connecting a function (`self.num_changed`) to `textChanged` property of `NumTextBox`
- However, since I would also format the Number after fetching details, it would trigger the `textChanged` property again. Hence each change would lead to a recursive loop.
- This was handled by `self.ignore` which acts as a kind of a lock. `setDetails` is called only when `self.ignore` is `False` but after formatting the number, `self.ignore` is set to `True`.

# Setting country details
- `libphonenumber` manages to fetch the `country_code` (dialer code) but does not return the country name or 2-letter code
- To do this, one may need to call the `geocoding` module which takes a lot of memory and is computationally expensive
- Instead, I stored import country codes as a separate json (Derived from [this](https://gist.github.com/Goles/3196253))
- Additionally, I also saved 32px long flags in `flags/` by copying them from [this repository](https://github.com/cristiroma/countries)
- Thus I'm also displaying the country's name and flag.

# Other Updates
- Moved cursor to end of line after in the beginning and formatting it every time.
- Added a **Delete button** to delete the last character
- Forked and ran [kdeconnect's Android project](https://github.com/KDE/kdeconnect-android)

---
# Week 4

---
# Migrating from Python 2.7 to 3.5
- Creating a conda environment
		conda create --name deb python=3.5
- Installing dependencies

		conda install phonenumbers
-
# Packaging
- Figure out installation of PyQt4
- Added `get-pip.py` to install `pip` in case the user does not have it
- Created a package called debdialer
- Added `setup.py` for the package
- Need to add requirements.txt
- Need to work out desktop app addition and MIME handling

---
# Week 5
---
# Sorting out default country
If the number isn't in E.164 format, libphonenumber can't accomplish much with the number.
<br> Hence it's important to assign a default country code in such scenarios.

## Option 1 : Using environment variables
Using `DEBDIALER_COUNTRY`, an environment variable

  	export DEBDIALER_COUNTRY="IN"				
## Option 2 : Using a configuration file
Found it a little redundant to create a config file for a single parameter.

## Option 3 : Using the user's IP address
- Initial approach :
	- Extract the user's inet address from eth or wlo using netifaces *(but I later realized that this wasn't my public IP)*.
	- Use [python-geoip](https://pythonhosted.org/python-geoip/) module to fetch the user's country code from IP address.
There were a problems involved in installing this but it eventually worked it.
- Final approach:
	- Send a request to ipinfo.io.
	- Though the response takes some time but it returns the country as well.

---
# Week 6
---

# Extracting Phone Numbers from files
- Initially tried creating a regex pattern to identify numbers
- Eventually decide to use PhoneNumberMatcher

## Using PhoneNumberMatcher
- Created a function : [parse_file_for_nums](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/blob/master/debdialer/fetch_details.py#L43)
	- Accepts a file Path and country code (default code handled in Week 5)
	- Reads the file
	- Uses `PhoneNumberMatcher(text, country_code)` to parse file for phonenumbers
		```
		# Example

		text = "Call me at 510-748-8230 if it's before 9:30, or on 703-4800500 after 10am."
		country_code = "US"
		matches = PhoneNumberMatcher(text, country_code)
		# matches - a phonenumbers.phonenumbermatcher.PhoneNumberMatcher object
		# Generator, not a list

		for i in matches:
   		print (i)

		# OUT :
		# PhoneNumberMatch [11,23) 510-748-8230
		# PhoneNumberMatch [51,62) 703-4800500

		```
	- Format the number in international format and return list of numbers

```
# Usage
from debdialer.fetch_details import parse_file_for_nums
parse_file_for_nums('matcher_test.txt','IN')

# OUT :
# ['+919176119388', '+914422443565']
```

---
# Week 7
---
# PyQt4 Installation
- I had installed PyQt4 from source, as most guides suggested but @tlevine insisted on installing it with `apt`, which is significantly easier.
- As a result, I am installing PyQt4 with
```
sudo apt install python3-pyqt4
```
- This automatically installs it in `/usr/lib/python3/dist-packages` for all users.
- Cautionary note :
	- If the PyQt4 module cannot be found even after installation,
		- Run `/usr/bin/python3` instead on `python3`<br/> It's likely that you're running python from Anaconda
		- Add `/usr/lib/python3/dist-packages` to `$PATH`

# Packaging
I had started this back in week 4 but I hadn't been able to complete because of some challenges I had encountered.

- Finished porting the application from Python 2.7 to 3.6. (All work I had done in the first 3 weeks was in Python 2.7.)
‌- Added setup.py file to install the package
- Used pkg_resources to access non-code files.
	- Resource files require a path to load
	- Absolute path cannot be determined before installation or generalised since different users may install in different locations
	```
	from pkg_resources import resource_filename
	FLAG_PATH = 'resources/flags/' + code + '-32.png'
	FULL_FLAG_PATH = resource_filename(__name__,FLAG_PATH)
	```
- Added a desktop file to repository and bash commands for the user to add it to local applications
	```
	$ cat debdialer.desktop
		[Desktop Entry]
		Version=1.0
		Name=Pop-Up Dialer
		Comment=An application to handle tel: URIs and dial numbers
		Exec=/usr/bin/python3 DEBDIALER_PATH/dialer_main.py
		Path=DEBDIALER_PATH
		Icon=DEBDIALER_PATH/Images/deblogo.png
		Terminal=false
		Type=Application
		Categories=Utility;Development;

	# Get path of debdialer.desktop after debdialer has been installed
	$ DEBDIALER_PATH=`python3 -c 'import debdialer; print(debdialer.__path__[0])'`

	# Replace path in debdialer.desktop
	$ sed -i "s|DEBDIALER_PATH|$DEBDIALER_PATH|" "debdialer.desktop"

	# Copy debdialer.desktop to /usr/share/applications/
	$ sudo cp debdialer.desktop /usr/share/applications/debdialer.desktop
	```
	This needs to be worked on since running the command in the cloned repository will return the path of `debdialer` in the repository and the globally installed `debdialer`.
- Added an XML file to handle tel: MIME links with xdg-mime. This requires loggin out and in back to refresh MIME links.

```
	<?xml version="1.0"?>
	<mime-info xmlns='http://www.freedesktop.org/standards/shared-mime-info'>
	<mime-type type="x-scheme-handler/tel=debdialer.desktop">
	<comment>Invoking Debian Dialer</comment>
	<glob pattern="tel:*"/>
	</mime-type>
	</mime-info>
```

- Created a README for instructions to set up the above


---
# Weeks 8 & 9
---
One of the key elements of the proposal was to **link the desktop application to the user's phone**, since it's often the **primary device used to place calls** and store phone numbers.

# Experiments with kdeconnect

## About kde-connect
- Developed by KDE
- Github repositories are mirrors. Development on [phabricator](https://phabricator.kde.org/project/view/159/)
- Desktop application
	- Github repository : [https://github.com/KDE/kdeconnect-kde](https://github.com/KDE/kdeconnect-kde)
	- Desktop code: [https://cgit.kde.org/kdeconnect-kde.git](https://cgit.kde.org/kdeconnect-kde.git)
	- Written in C++. Kirigami used for GUI
	- **Installation**
	```
	sudo apt install kdeconnect indicator-kdeconnect
	```
- Android application :
	- Github repository : [https://github.com/KDE/kdeconnect-android](https://github.com/KDE/kdeconnect-android)
	-  Android code: [https://cgit.kde.org/kdeconnect-android.git](https://cgit.kde.org/kdeconnect-android.git)
	- Java, Gradle, Android
- Connects a desktop with one's Android phone using a desktop application and a Android application installed on devices on the same LAN, communicating using a TCP socket.
- Existing features :
	- File sharing
	- Virtual touchpad
	- Notification sync
	- Shared clipboard, etc.

## Features I wanted to add to the KDE-connect App
- Send phone numbers to Android phone to dial
- Add contacts on Android Phone

Note : A part of their application was also supposed to be capable of handling tel links but it wasn't getting installed as a part as the debian package. It seems like a bug. I tried making changes to their desktop application but their debian package is significantly behind their development branch and I had some issues building their desktop application.

## Issues with adding a new plugin to their desktop application
- **Unable to install dependencies**
	- Requires a numbers of libraries from KDE's framework
	- Debian package is at version 1.0, while development is at 1.3.x
	- Hence `sudo apt build-dep kdeconnect` installs v5.18.0 but in order to build the application, I need v5.42.0
	- I tried reducing the minimum version requirements but `build-dep` doesn't download `KF5Wayland` and `KF5` and I get the following error.

	```
	-- The following OPTIONAL packages have not been found:
 	* KF5Wayland (required version >= 5.18.0)

	-- The following REQUIRED packages have not been found:

 	* KF5 (required version >= 5.18.0)

	CMake Error at /usr/share/cmake-3.5/Modules/FeatureSummary.cmake:556 (message):
  feature_summary() Error: REQUIRED package(s) are missing, aborting CMake
  run.
	Call Stack (most recent call first):
  CMakeLists.txt:71 (feature_summary)

	-- Configuring incomplete, errors occurred!
	See also 	"/home/b/gitpository/kdeconnect-kde/build/CMakeFiles/CMakeOutput.log".
	```
- Updated application would have to also be add to debian archives, since build the application is clearly not an ideal options.
- I did try adding a new plugin in vain, but then I couldn't build the application.

## Workaround
- Hence I improvised and used a feature of their cli called `--ping-msg` which was meant to send a String to the android application and display the same with a Notifcation.
- Made changes to their Android application in order to parse ping messages starting with ::DIALER with another function,[ dialer_handler](https://github.com/py-ranoid/kdeconnect-android/blob/master/src/org/kde/kdeconnect/Plugins/PingPlugin/PingPlugin.java#L106).
- I am now sending information through to the android application by seperating arguments with ::
- I tried pushing this change to kdeconnect's Android repository but the admins insisted on making a new plugin on the desktop application, which is cleaner but might take longer, hence I decided to complete this after the GSoC Period.<br>
https://phabricator.kde.org/D14248
- I'm pushing changes to my Github fork of kdeconnect-android : [https://github.com/py-ranoid/kdeconnect-android](https://github.com/py-ranoid/kdeconnect-android)


## Result
```
kdeconnect-cli -d f69e2e8ac00b140d --ping-msg "::DIALER::DIAL::9176119388"
```
Will pop up a notification to dial the number 9176119388, which when clicked, opens a dialer

```
kdeconnect-cli -d f69e2e8ac00b140d --ping-msg "::DIALER::ADD::9176119388::Vishal"
```
Will pop up a notification to add a contact Vishal (9176119388), which when clicked, opens the add contact screen on the user's phone.
<br/>
<br/>
<img src = "http://vishalgupta.me/Hello-From-The-Debian-Side/Images/Screenshot_20180715-190706.jpg" width="400">
---
# Week 10
---
Since I had to write code to get the default country by sending a get request to ipinfo.io, *@tlevine* suggested developing a module with additional functionality.
# [`ipinfo`](https://salsa.debian.org/comfortablydumb-guest/ipinfo)
## About
- Python Module to fetch information about user using IP address
- *Python wrapper for [ipinfo.io](ipinfo.io) API*
- Uses `urllib3` to send requests

## Options
- `cn` : Get Country Name only
- `cc` : Get Country Code only
- `ct` : Get City only
- `rg` : Get Region only
- `ls` : Get location as a string
- `lc` : Get coordinates
- `ip` : Get IP Address only
- `hn` : Get Host Name only
- `a`  : Get all details.

## Usage
- Can be used with **Command Line Interface**
	```
	  $ python3 -m ipinfo
	  {'loc': '13.0833,80.2833', 'country': 'IN', 'org': 'AS24309 Atria Convergence Technologies Pvt. Ltd.  Broadband Internet Service Provider INDIA', 'region': 'Tamil Nadu', 'city': 'Chennai', 'ip': '123.123.123.123', 'postal': '600003'}

	  $ python3 -m ipinfo cc
	  IN

	  $ python3 -m ipinfo ls
	  Tamil Nadu, Chennai, India

	```
- Or **imported as a module**
	```
	from ipinfo.ipinfo import get_country_name,get_all

	print (get_country_name())
	# Chennai

	print (get_all())
	# {'city': 'Chennai',
	# 'region': 'Tamil Nadu',
	# 'ip': '123.123.123.123',
	# 'hostname': 'broadband.actcorp.in',
	# 'org': 'AS24309 Atria Convergence Technologies Pvt. Ltd.  Broadband Internet Service Provider INDIA',
	# 'postal': '600003',
	# 'country': 'IN',
	# 'loc': '13.0833,80.2833'}
	```

## Publishing
- Tried publishing module on pypi by following [this](https://python-packaging.readthedocs.io/en/latest/minimal.html)
- `python3 setup.py register` resulted in `Server response (308): Redirect to Primary Domain`

# Command Line Interfaces for other functions
## Why
- The debdialer application requires Qt5.
- Some users may not comfortable with using a GUI and prefer a terminal-based application, or something with minimal reliance on the mouse
- @tlevine suggeted using

## CLI for phonenumber functions (`pn-cli.py`)

### To parse file for phone numbers
```
$ python3 pn-cli.py -f matcher_test.txt
Parsing matcher_test.txt for numbers. Code : IN
+919176119388
+914422443565
```
### To parse phone number to extract details
```
$ python3 pn-cli.py -p 9176119388
Timezone : Asia/Calcutta | UTC+5.5
Carrier : Vodafone
Country :India(IP)
Flag :/home/b/gitpository/DebianDialer/debdialer/resources/flags/IN-32.png
Formatted :+91 91761 19388
```

---
# Week 11
---
# Adding Licenses

- Added [**GNU Affero General Public License v3.0**](https://choosealicense.com/licenses/agpl-3.0/) to debdialer
	<br> License : https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/blob/master/LICENSE
- Mentioned licenses of modules used in debdialer
	- python-phonenumbers : Used it to parse phone numbers
	- Country Codes : A Github Gist. Used to it get Country Code from Dialer Code
	- countries : A Github repository with data about countries. Used it for flags
	- kdeconnect : Modified android application to send phone numbers and add contacts
	- vobject : Used it to parse .vcf files

- Experimenting with sipclients
	- Ekiga
	- pjsua

# Added MIME-type to desktop file
- Was initially using xdg-mime to setup trigger debdialer
- Added MimeType to desktop file
```
	MimeType=x-scheme-handler/tel;x-scheme-handler/sip;text/x-vCard;
```
	- `x-scheme-handler/tel` : `tel:` links
	- x-scheme-handler/sip : `sip:` links
	- text/x-vCard : `.vcf` files

# Adding `entry_point` for `debdialer`
## Aim
- Create a command-line application for `debdialer`
- `debdialer <args>` instead of `python3 -m debdialer <args>`
- Seperate code so it could be run with `__init__.py` and `__main__.py`
	- `__init__.py` : Run when you import a package into a running python program.
	- `__main__.py` : Run as `'__main__'` when we run package is as the main program (`python -m modulename`).

## Changes made
- Since `DialerApp` and `main()` was in `__main__`, they couldn't be imported
- Moved `DialerApp` and `main()` to a new script : `dialer_main.py`
- Create `__init__` with `cli_main()` that would call `.dialer_main.main`
- Changed `__main__` to would call `.dialer_main.main` when `__name__` was equal to `'__main__'`
- Finally, add a console_script : `debdialer`, that would call `debdialer:cli_main`
```
entry_points = {
			'console_scripts': ['debdialer=debdialer:cli_main'],
	},
```

# Exploring [SoftPhones](https://wiki.voip.ms/article/Softphones)
- `pjsua` :
	- Works from the terminal.
	- No GUI
	- Needs to be installed from source
- `Ekiga` :
	- Installation : `sudo apt install ekiga`
	- GUI for configuration
	- Call URL with ekiga : `ekiga -c URL`
---
# Week 12
---
# vcard parsing
## Aim
- Extracting phone numbers and name from vcard (`.vcf`) file
- Send contact to Android phone

## Execution
- Using a 3rd party module : [vobject](https://github.com/eventable/vobject)
-	Read contents of vcard file to `text`
- Parse vcard contents with `vobject`
	```
	vcard = vobject.readOne(text)
	```
	Each item/value in vcard becomes a child of `vcard` object
- Get value of FullName (`fn`) child
	```
	name = vcard.getChildValue('fn')
	```
-	- Get list of telephone numbers (children) with `vcard.tel_list`
	- Get value of each phone number
```
numbers = [x.value for x in vcard.tel_list]
```

# Connecting GUI buttons to added features
## Adding Contacts to Phone
There are two approaches to sending a sending a contact.
Both use `kdeconnect_utils.dialer_add` to create a contact on a specific device (`device_id`) under a given `name` with given `numbers` (which is a list, 1 <= length <= 3)

### Sending number in Dialer (`Add to Contacts`) ([Screenshots](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/tree/master#adding-number-in-dialer-as-contact-add-to-contacts))
- Read number in `NumTextBox`
- Open a `QInputDialog` to get contact name
- Return if user clicked on *Cancel*
- If user clicked on *OK*, send number to phone with `kdeconnect_utils.dialer_add`

### Sending numbers in a file as contact (`Add vcard to Contacts`) ([Screenshots](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/tree/master#adding-contact-using-vcf-file-add-vcard-to-contacts))
- If file name ends with `.vcf` (ie. vcard file)
	- Call `utils.parse_vcard` to fetch `name` and `numbers` from file
	- Send number to phone with `kdeconnect_utils.dialer_add`
- else,
	- Call `get_file_nums` to parse phone numbers from chosen file
	- Open a `QInputDialog` to get contact name
	- Return if user clicked on *Cancel*
	- If user clicked on *OK*, send number to phone with `kdeconnect_utils.dialer_add`

## Sending number in Dialer to dial on Phone (`DIAL ON ANDROID PHONE`)([Screenshots](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/tree/master#sending-dialer-number-to-android-phone-dial-on-android-phone))
- Read number in `NumTextBox`  using `getDialerNumber()`
- Uses `kdeconnect_utils.dialer_send` to send the given `number` to a specific device (`device_id`)

## Parse phone numbers in a File ([Screenshots](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/tree/master#parsing-numbers-from-file-open-file))
- Calls `print_file_nums`
	- Open a dialog to choose a file
	- Get contents of file and parse for phone numbers
	- Print to STDOUT
	- Wasn't sure how to display a list with the existing GUI
# Publishing `debdialer`
### Setting up your account on PyPi
- If you don't have an account, create one here : [https://pypi.org/account/register/](https://pypi.org/account/register/)
- Adding your credentials on your desktop : Create `~/.pypirc`.
  (Refer [this](https://docs.python.org/3/distutils/packageindex.html#pypirc))
	<br>Contents of ~/.pypirc :
	```
	[distutils]
	index-servers =
	    pypi

	[pypi]
	repository: https://upload.pypi.org/legacy/
	username: vishalgupta
	password: <enter password here>
	```

### Uploading your package
- Make sure you have the latest versions of setuptools and wheel installed:
```
python3 -m pip install --user --upgrade setuptools wheel
```
- Run this command from the same directory where setup.py is located.
```
python3 setup.py sdist bdist_wheel
```
This should have created a `dist/` directory that contains a `.whl` file and `.tar.gz`

		$ ls dist
		debdialer-0.15-py3-none-any.whl  debdialer-0.15.tar.gz
- Install **twine** to upload package
```
python3 -m pip install --user --upgrade twine
```
- Uploading packages with twine
	```
	$ twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

	# If the above command doesn't work, try this (I used the below command)

	$ python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
	Uploading distributions to https://upload.pypi.org/legacy/
	Enter your username: vishalgupta
	Enter your password:
	Uploading debdialer-0.15-py3-none-any.whl
	100%|█████████████████████████████████████████████| 277k/277k [00:04<00:00, 69.2kB/s]
	Uploading debdialer-0.15.tar.gz
	100%|███████████████████████████████████████████| 14.8k/14.8k [00:00<00:00, 15.4kB/s]
	```
