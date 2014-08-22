#! /bin/sh
wget -q http://pierriko.com/ign/ign.html
xdg-open http://localhost:8686/ign.html
python -m SimpleHTTPServer 8686
