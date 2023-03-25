# ceates a file in temp

file { 'config':
  ensure  => 'present',
  content => 'Host myserver
	User ubuntu
        PasswordAuthentication no
	IdentityFile ~/.ssh/school',
  path    => '/home/torpeedo/.ssh/config',
}
