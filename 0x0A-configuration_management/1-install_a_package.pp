# Install Flask with pip

package {'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
