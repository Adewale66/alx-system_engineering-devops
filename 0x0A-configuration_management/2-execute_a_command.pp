# Kill the process killmenow

exec { 'kill process':
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell',
}
