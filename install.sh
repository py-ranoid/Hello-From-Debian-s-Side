sudo pip3 install debdialer
SALSA_URL=https://salsa.debian.org/comfortablydumb-guest/debdialer/raw/master
sudo wget $SALSA_URL/Images/deblogo-128.png -O /usr/share/icons/hicolor/128x128/apps/deblogo-128.png -nv
sudo wget $SALSA_URL/debdialer.desktop -O /usr/share/applications/debdialer.desktop -nv
sudo wget $SALSA_URL/debdialer.conf -O /etc/debdialer.conf -nv
sudo update-desktop-database /usr/share/applications/
