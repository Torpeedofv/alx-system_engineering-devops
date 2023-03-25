# ceates a file in temp

package { 'augeas':
  ensure => installed,
}

augeas { 'Turn off passwd auth':
  context => '/files/etc/ssh/ssh_config',
  changes => [
    'set PasswordAuthentication no',
  ],
}

augeas { 'Declare identity file':
  context => '/files/etc/ssh/ssh_config',
  changes => [
    'set IdentityFile ~/.ssh/school',
  ],
}
