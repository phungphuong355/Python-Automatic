#! /bin/bash
rm -rf "index.html"
rm -rf "index1.html"
rm -rf "index2.html"
rm -rf "index3.html"
rm -rf "index4.html"
rm -rf "index5.html"

touch "index.htm"
touch "index_1.htm"
touch "index_2.htm"
touch "index_3.htm"
touch "index_4.htm"
touch "index_5.htm"

for file in *.htm; do
  name=$(basename "$file" .htm)
  mv "$file" "$name.html"
done