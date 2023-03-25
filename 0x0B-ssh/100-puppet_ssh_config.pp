# ceates a file in temp

file { 'config':
  ensure  => 'present',
  content => 'Host *
	PasswordAuthentication no

Host myserver
	User ubuntu
        PasswordAuthentication no
	IdentityFile ~/.ssh/school
	Hostname 34.227.101.5',
  path    => '/home/torpeedo/.ssh/config',
}
