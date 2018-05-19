# Setup

## Installing SIP
Download from here : https://riverbankcomputing.com/software/sip/download
Installation instructions : http://pyqt.sourceforge.net/Docs/sip4/installation.html

	tar -xvzf sip-4.19.7.tar.gz
	cd sip-4.19.7
	python configure.py
	make
	make install

## Installing PyQt4
Download from here : https://riverbankcomputing.com/software/pyqt/download
Installation instructions : http://pyqt.sourceforge.net/Docs/PyQt4/installation.html

	tar -xvzf PyQt4_gpl_x11-4.12.1.tar.gz
	cd PyQt4_gpl_x11-4.12.1
	python configure.py

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
URI Schemes Wiki : https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Official_IANA-registered_schemes
`tel:` URI documentation : http://www.ietf.org/rfc/rfc3966.txt
`sip:` (or `sips:`) is the official URI scheme for SIP
`callto` is the one used by skype (Source)

Record to be added  : 

	x-scheme-handler/mailto=thunderbird.desktop

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

	> xdg-mime install debdialer-tel.xml
