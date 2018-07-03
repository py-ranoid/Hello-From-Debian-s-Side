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
