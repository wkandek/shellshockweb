#!/bin/bash
echo Content-type: text/html
echo ""

echo "<HTML><HEAD>"

echo "<SCRIPT>"
echo "document.addEventListener('click', function(event) {"
echo "  var target = event.target;"
echo "  if (target.tagName.toLowerCase() == 'a')"
echo "  {"
echo "      var port = target.getAttribute('href').match(/^:(\d+)(.*)/);"
echo "      if (port)"
echo "      {"
echo "         target.href = port[2];"
echo "         target.port = port[1];"
echo "      }"
echo "  }"
echo "}, false);"
echo "</SCRIPT>"

echo "</HEAD>"
echo "<BODY>"
echo "<H3>Main Webpage</H3>"
echo "<UL>"
echo "<LI><A href=/cgi-bin/man.cgi>Man page</A>"
echo "<LI>Our BodgeIT <A HREF=:8080/bodgeit2>store</A>"
echo "</UL>"
echo "</BODY></HTML>"


