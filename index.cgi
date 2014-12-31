#!/bin/bash
echo Content-type: text/html
echo ""

echo "<HTML><HEAD>"

echo "<SCRIPT>"
echo "function setHref() {"
echo "ho = document.getElementById('modify-me').href;"
echo "ho = ho.split('/').pop();"
echo "document.getElementById('modify-me').href = window.location.protocol + '//' + window.location.hostname + ':8080/' + ho;"
echo "}"

echo "</SCRIPT>"

echo "</HEAD>"
echo "<BODY onload='setHref()'>"
echo "<H3>Main Webpage</H3>"
echo "<UL>"
echo "<LI><A href=man.cgi>Man page</A>"
echo "<LI>Our BodgeIT <A HREF=/bodgeit2 ID='modify-me'>store</A>"
echo "</UL>"
echo "</BODY></HTML>"


