# Installs nginx n stuff
exec { '/usr/bin/env apt-get -y update' : }
-> package { 'nginx':
  ensure => installed,
}
-> file { '/var/www/html/index.html' :
  content => 'Holberton School!',
}
-> file_line { 'add header' :
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'listen \[::\]:80 default_server;',
}
-> file_line { 'add location' :
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}",
  after  => "\tadd_header X-Served-By ${hostname};",
}
-> service { 'nginx':
  ensure => running,
}
-> exec { '/usr/bin/env mkdir -p /data/web_static/releases/test/' : }
-> exec { '/usr/bin/env mkdir -p /data/web_static/shared/' : }
-> exec { '/usr/bin/env echo "Hello Holberton School!" > /data/web_static/releases/test/index.html' : }
-> exec { '/usr/bin/env ln -sf /data/web_static/releases/test/ /data/web_static/current' : }
-> exec { '/usr/bin/env service nginx restart' : }
