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
