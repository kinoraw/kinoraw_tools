git mv $1 archive/
cp $2 ~/sources/kinoraw_repo/
cd ~/sources/kinoraw_repo/
git add $2
git rm $1
git commit -a -m "new kinoraw_tools release"
git push