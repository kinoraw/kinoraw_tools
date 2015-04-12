sh dev-scripts/pandoc.sh
sh dev-scripts/zipgen.sh $1
cp $1 ~/sources/kinoraw_repo/
cd ~/sources/kinoraw_repo/
git add $1
git commit -a -m "new kinoraw_tools release"
git push