# Puppet manifest to kill a process named killmenow

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin'],  # Ensure path to pkill is included
  onlyif  => 'pgrep killmenow',     # Execute only if the process is running
}
