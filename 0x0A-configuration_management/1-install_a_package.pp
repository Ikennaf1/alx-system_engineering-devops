# Install a package using Puppet

exec { 'install python packages':
  command => 'pip3 install Flask==2.1.0'
}
