#!/bin/bash
echo Content-type: text/html 
echo ""

echo "<HTML><BODY>"
echo "<A href=man.cgi>Back</A>"
echo "<PRE>"
CMD=`echo $QUERY_STRING | sed -n 's/^.*CMD=\([^&]*\).*$/\1/p' | sed 's/%20/ /g'`
man $CMD
echo "</PRE>"
echo "<A href=man.cgi>Back</A>"
echo "</BODY></HTML>"

