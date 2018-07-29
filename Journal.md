Note : Find project scrum board [here](https://storm.debian.net/grain/bD3aJdnYLBWo5R3K6GWckn/b/sandstorm/libreboard)

---
# Week 1

---
# Setup

## Installing SIP
Download from here : https://riverbankcomputing.com/software/sip/download
Installation instructions : http://pyqt.sourceforge.net/Docs/sip4/installation.html

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
Installation instructions : http://pyqt.sourceforge.net/Docs/PyQt4/installation.html

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
			<glob pattern="tel:*"/>
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