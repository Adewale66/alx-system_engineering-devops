#/usr/bin/pup
# Install Flask with pip

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
