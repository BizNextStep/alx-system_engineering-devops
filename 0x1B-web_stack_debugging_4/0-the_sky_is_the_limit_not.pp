# Increases the amount of traffic an Nginx server can handle

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/nginx/nginx.conf',
  path    => '/usr/local/bin/:/bin'
}

# Restart Nginx
exec { 'nginx-restart':
  command => 'service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
} 
