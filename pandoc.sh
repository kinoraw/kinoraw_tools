pandoc -f markdown_github -t html5 -o README.html README.md
touch README.bak
sed -i README.bak -e 's/src="/src="./g' README.html
rm README.bak