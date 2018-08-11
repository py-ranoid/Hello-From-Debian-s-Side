# Click To Dial Popup Window for the Linux Desktop

## Links :
- debdialer
  - [Debian Salsa Repository ](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/tree/master)
  - [Github Mirror](https://github.com/py-ranoid/debdialer)
- GSoc
  - [GSoC Proposal](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/blob/master/GSoC/GSoC%20Proposal.pdf)
  - [Weekly Journal](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/blob/master/GSoC/Journal.md)
- About me :
  - Github : [/py-ranoid](https://github.com/py-ranoid)
  - Email : [vishalg8897@gmail.com](mailto:vishalg8897@gmail.com)

## Workflow and purpose
<img src = "http://vishalgupta.me/debdialer/Images/workflow.png" align="center">
There are multiple applications and options to handle phone-numbers. Hence, everything on the left and on the right already exist. However the MIME action (clicking a number in a browser) doesn't "know" if the user wants to call the number or save it for later. The popup will let the user make that choice. The aim is to develop the component in the middle so that it can interact with each of the things on the right. The user can
configure the options the actions further at `/etc/debdialer.conf`

## Overview of DebDialer

<img src = "http://vishalgupta.me/debdialer/Images/PrimaryDesk.png" align="center">

debdialer is an Application for handling tel: URLs and (phone numbers in general) on the Linux Desktop. It is written in [Python 3.5.2](https://www.python.org/downloads/release/python-352/) and uses [PyQt4](http://pyqt.sourceforge.net/Docs/PyQt4/introduction.html#pyqt4-components) to display a popup window. Alternatively, there is also a `no-gui` option that uses [dmenu](https://wiki.archlinux.org/index.php/Dmenu) for input and terminal for output. There is also a [modified apk](tiny.cc/ddial-kdeconnect) of [KDE-Connect](https://phabricator.kde.org/project/view/159/) to link debdialer with the user's Android Phone. The pop-up window has numeric and delete buttons, so the user can either use the GUI or keyboard to modify numbers.
#### Installation
Installing with `pip` installs the python package but does not set up the desktop file. Hence, the following script needs to be run.
```
# Optional dependencies. Atleast one of them is required.
sudo apt install dmenu
sudo apt install python3-pyqt4

curl -L https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/raw/master/install.sh -s | bash
```
#### Features ([Screenshots and how-to]([https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side#usage]))
- Adds contact using .vcf file (`Add vcard to Contacts`)
- Adds number in dialer as contact (`Add to Contacts`)
- Sending dialer number to Android phone (`DIAL ON ANDROID PHONE`)
- Parsing numbers from file (`Open File`)
- Automatic formatting of numbers and setting of details


## Summary of Weekly Progress

- [Week 1](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/blob/master/GSoC/Journal.md#week-1)
	- Setup
		- Installing SIP
		- Installing PyQt4
		- Installing QtDesigner
	- Making the Dialer
	- Mime Handling
		- Creating a desktop entry
		- Setting default application for tel links with xdg-mime
		- Testing the MIME URI
- [Week 2](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/blob/master/GSoC/Journal.md#week-2)
	- Fetching Phone Number details
		- Libraries
			- [libphonenumber](https://github.com/googlei18n/libphonenumber)
			- [python-phonenumbers](https://superuser.com/questions/159775/is-there-a-firefox-shortcut-to-copy-the-url-of-thecurrent-page)
	- Displaying Phone Number details
		- About GUI
		- GUI Initialisation
		- Fetch Details button
- [Week 3](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/blob/master/GSoC/Journal.md#week-3)
	- Triggering `setDetails`
	- Setting country details
	- Other Updates
- [Week 4](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/blob/master/GSoC/Journal.md#week-4)
	- Migrating from Python 2.7 to 3.5
	- Packaging
- [Week 5](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/blob/master/GSoC/Journal.md#week-5)
	- Sorting out default country
		- Option 1 : Using environment variables
		- Option 2 : Using a configuration file
		- Option 3 : Using the user's IP address
- [Week 6](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/blob/master/GSoC/Journal.md#week-6)
	- Extracting Phone Numbers from files
		- Using PhoneNumberMatcher
- [Week 7](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/blob/master/GSoC/Journal.md#week-7)
	- PyQt4 Installation
	- Packaging
- [Weeks 8 & 9](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/blob/master/GSoC/Journal.md#weeks-8-9)
	- Experiments with kdeconnect
		- About kde-connect
		- Features I wanted to add to the KDE-connect App
		- Issues with adding a new plugin to their desktop application
		- Workaround
		- Result
- [Week 10](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/blob/master/GSoC/Journal.md#week-10)
	- [`ipinfo`](https://salsa.debian.org/comfortablydumb-guest/ipinfo)
		- About
		- Options
		- Usage
		- Publishing
	- Command Line Interfaces for other functions
		- Why
		- CLI for phonenumber functions (`pn-cli.py`)
			- To parse file for phone numbers
			- To parse phone number to extract details
- [Week 11](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/blob/master/GSoC/Journal.md#week-11)
	- Adding Licenses
	- Added MIME-type to desktop file
	- Adding `entry_point` for `debdialer`
		- Aim
		- Changes made
	- Exploring [SoftPhones](https://wiki.voip.ms/article/Softphones)
- [Week 12](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/blob/master/GSoC/Journal.md#week-12)
	- vcard parsing
		- Aim
		- Execution
	- Connecting GUI buttons to added features
		- Adding Contacts to Phone
			- Sending number in Dialer (`Add to Contacts`) ([Screenshots](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/tree/master-adding-number-in-dialer-as-contact-add-to-contacts))
			- Sending numbers in a file as contact (`Add vcard to Contacts`) ([Screenshots](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/tree/master-adding-contact-using-vcf-file-add-vcard-to-contacts))
		- Sending number in Dialer to dial on Phone (`DIAL ON ANDROID PHONE`)([Screenshots](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/tree/master-sending-dialer-number-to-android-phone-dial-on-android-phone))
		- Parse phone numbers in a File ([Screenshots](https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/tree/master-parsing-numbers-from-file-open-file))
	- Publishing `debdialer`
		- Setting up your account on PyPi
		- Uploading your package
	- Desktop File changes
	- Experimenting with bash-based GUI
		- bashrun
		- dmenu
			- Installation
			- Usage
			- Applying dmenu for `--no-gui` with debdialer
	- Configuration file
		- `.json` config file
		- `.conf` config file
