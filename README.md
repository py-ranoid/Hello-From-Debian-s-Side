### How to install
```
# Installing Qt4
sudo apt install python3-pyqt4

# Installing pip (optional)
python get-pip.py

pip3 install .
```

### Creating a desktop application
```
DEBDIALER_PATH=`python3 -c 'import debdialer; print(debdialer.__path__[0])'`
sed -i "s|DEBDIALER_PATH|$DEBDIALER_PATH|" "debdialer.desktop"
sudo cp debdialer.desktop /usr/share/applications/debdialer.desktop
```
### Adding a MIME link for `tel:` links
```
xdg-mime install debdialer-tel.xml
```
Note : If the MIME link doesn't work, try logging out and back in.<br>
#### To test the MIME link
```
xdg-open tel:873811
```
### Setting default country code
```
export DEBDIALER_COUNTRY='<2 letter country code>'

# For example
export DEBDIALER_COUNTRY='IN'
```

## Licenses and Copyright information
### [python-phonenumbers](https://github.com/daviddrysdale/python-phonenumbers) (*Python port of Google's [libphonenumber](https://github.com/googlei18n/libphonenumber) library*)
- License : [Apache-2.0](https://github.com/daviddrysdale/python-phonenumbers/blob/dev/LICENSE)
-Copyright : 2009-2015 The Libphonenumber Authors

### Country Codes (*Country and Dial or Phone codes in JSON format*)
- Source : [Github Gist](https://gist.github.com/Goles/3196253)
- Author : [Nicolas Goles](https://gist.github.com/Goles)

### [Country Flags](https://github.com/cristiroma/countries)
- License : [GPL-3.0](https://github.com/cristiroma/countries/blob/master/LICENSE)
- Copyright : 2011 Cristian Romanescu

### [kdeconnect](https://github.com/KDE/kdeconnect-android/)
- License : [GPL-2.0](https://github.com/KDE/kdeconnect-android/blob/master/COPYING)
