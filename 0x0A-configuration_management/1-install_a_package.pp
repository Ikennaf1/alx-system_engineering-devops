# Install flask using Puppet

exec { 'install flask':
  command => 'pip3 install Flask==2.1.0'
}
