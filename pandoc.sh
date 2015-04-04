pandoc -f markdown_github -t html5 -o pre.html README.md
sed -n 's/src="/src="./gpw README.html' pre.html
rm pre.html