sudo pip3 install debdialer
SALSA_URL=https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side/raw/master
sudo wget $SALSA_URL/Images/deblogo-128.png -O /usr/share/icons/hicolor/128x128/apps/deblogo-128.png
sudo wget $SALSA_URL/debdialer.desktop -O /usr/share/applications/debdialer.desktop
sudo wget $SALSA_URL/debdialer.conf -O /etc/debdialer.conf
sudo update-desktop-database /usr/share/applications/
