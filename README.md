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
	
	
![](https://py-ranoid.github.io/Hello-From-The-Debian-Side/Images/Screenshot%20from%202018-02-22%2010-50-21.png) 