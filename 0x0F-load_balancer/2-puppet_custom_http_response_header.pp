# automates the task of creating a custom HTTP header

exec { 'command':
  command  => 'apt-get update -y;
  apt-get install nginx -y;
  sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,
}
