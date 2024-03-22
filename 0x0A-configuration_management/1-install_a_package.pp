# Define a class to manage the Flask package
class { 'python::pip': }

# Install Flask with specific version
package { 'Flask':
  ensure => installed,
  provider => 'pip3',
  require => Class['python::pip'],
  # Specify the exact version
  version => '2.1.0',
}
