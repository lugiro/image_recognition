#!/usr/bin/perl

#Filnavn: piMENY1.pl - hovedmeny

#require '/var/www/cgi-bin/cgi-lib.pl';

print "Content-type: text/html\n\n";

#Leser Systemnr/navn fra fil
open(FIL,"</usr/lib/cgi-bin/pi/text0.txt");
chomp(my @linje = <FIL>);
close(FIL);
$anttegn = length($linje[0]);
$text0 = substr($linje[0],0,$anttegn);

print <<"EOT";

<!DOCTYPE html>
<html>

<head>
<meta http-equiv="Content-Type"
content="text/html; charset=utf-8">
<!--
This is a comment
-->
<meta http-equiv="refresh" content="1">
<meta name="GENERATOR" content="Microsoft FrontPage Express 2.0">
<link rel="icon" type="image/png" href=$IPadr/pi/image/SmartHome1.png sizes="192x192">
<title>robo</title>
<style> 
body {
background-color: white;
background-size: 100% 100%;
background-position:top center; 
}
table {
table-layout:fixed;
}
</style>
</head>

<body>
<p align="center">
<font face = "Verdana" style="font-size: 100pt;">
<!-- <strong> -->
$text0
<!-- </strong> -->
</font>
<br>
<br>

</p>
</body>
</html>

EOT
