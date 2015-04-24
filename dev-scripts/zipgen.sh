mkdir kinoraw_tools
mkdir kinoraw_tools/imgs
cp *.py kinoraw_tools/
cp imgs/* kinoraw_tools/imgs/
cp README.html kinoraw_tools/
zip -r $1 kinoraw_tools 