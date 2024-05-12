file { '/etc/apache2/mods-available/php7.0.conf':
  ensure  => file,
  content => "
    <FilesMatch \\.php$>
            SetHandler application/x-httpd-php
    </FilesMatch>
    <FilesMatch \\.phps$>
            SetHandler application/x-httpd-php-source
            Require all denied
    </FilesMatch>
    # Running PHP scripts in user directories is a potential security risk.
    # User directories are often used to test .php scripts as the user who owns the directory.
    # This may result in PHP scripts being executed with elevated privileges.
    # Uncomment the following lines to prevent this behavior
    #
    #<Directory /home/*/public_html>
    #        php_admin_value engine Off
    #</Directory>
  ",
}

file { '/etc/apache2/mods-enabled/php7.0.conf':
  ensure  => link,
  target  => '/etc/apache2/mods-available/php7.0.conf',
  require => File['/etc/apache2/mods-available/php7.0.conf'],
}

service { 'apache2':
  ensure  => running,
  enable  => true,
  require => File['/etc/apache2/mods-enabled/php7.0.conf'],
}
