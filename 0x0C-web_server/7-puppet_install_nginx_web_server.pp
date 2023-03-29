# installs and configures an Nginx server

class { 'nginx':
  package_ensure => 'installed',
  service_enable => true,
  service_ensure => 'running',
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  mode    => '0644',
}

nginx::resource::server { 'default':
  listen_port         => 80,
  ipv6_listen_options => {
    'listen'          => true,
  },
  locations           => {
    '/redirect_me'    => {
      returns => 301,
      rewrite => ['^ /redirect_me(.*)$ https://www.youtube.com/watch?v=TfgBHC5gvTI$1 permanent'],
    },
  },
  server_name         => '_',
  root                => '/var/www/html',
  index_files         => ['index.html', 'index.htm', 'index.nginx-debian.html'],
}
