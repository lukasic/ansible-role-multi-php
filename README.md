Ansible Role: Multi PHP
=========

Ansible role providing multiple PHP versions on Debian.

Changelog
---------

1.6.0

* Support PHP 8.4

1.5.1

* Fix excluding JSON module for PHP 8.0+

1.5.0

* Support PHP 8.3

1.4.0

* Support PHP 8.2

1.3.1

* Remove json module for PHP 7.4+

1.3.0

* Add variable php_remove_unused_modules
  * Default -> false
  * If set to true, removes php modules not specified in `php` var
* Add variable php_remove_unused_versions
  * Default -> false
  * If set to true, removes php versions not specified in `php` var
* Fix: replace <0xa0> characters

1.2.0

* Support PHP 8.1

1.1.2

* Fix php_default_version
* Fix extensions redis and imagick

1.1.1

* Update README
* Fix Ansible Lint errors

1.1.0

* Support installation on Ubuntu, tested Focal

1.0.0

* Support installation of different PHP versions on Debian Buster

Installation
------------

Using `ansible-galaxy`:

```bash
$ ansible-galaxy install lukasic.php
```

Using `requirements.yml`:

```yaml
- src: lukasic.php
```

Requirements
------------

Role requires APT repository [deb.sury.org](https://deb.sury.org), provided by Ondrej Sury.

Role is tested only on Debian Buster and Ubuntu Focal. Other distribution versions should work too - if they have packages in repository.

Role Variables
--------------

Default PHP version:

```yaml
php_default_version: "7.3"
```

List of PHP modules to be installed across all versions:

```yaml
php_default_modules:
 - bcmath
 - bz2
 - curl
 - gd
 - readline
 - json
 - mysql
 - soap
 - opcache
 - xml
 - xmlrpc
 - zip
```

Can be specialized by:

```yaml
php56_default_modules: "{{ php_default_modules }}"
php70_default_modules: "{{ php_default_modules }}"
php71_default_modules: "{{ php_default_modules }}"
php72_default_modules: "{{ php_default_modules }}"
php73_default_modules: "{{ php_default_modules }}"
php74_default_modules: "{{ php_default_modules }}"
php80_default_modules: "{{ php_default_modules }}"
php81_default_modules: "{{ php_default_modules }}"
```

One special super variable:

```yaml
php: []
```

This variable controls installed PHP versions, modules and is used to configure PHP settings. See examples below.


Dependencies
------------

None.

Example Playbook
----------------

Example 1: Just install PHP 5.6 and 7.3

```yaml
- hosts: php
  roles:
     - lukasic.php
  vars:
    php:
      - version: php56
      - version: php73
```

Example 2: Install PHP 5.6, 7.3, 8.0 with extra modules and configures global CLI/FPM settings.

```yaml
- hosts: php
  roles:
     - lukasic.php
  vars:
    # local variable, see below
    common_fpm_ini:
     - { "section": "PHP",     "key": "max_execution_time",             "value": "360"  }
     - { "section": "PHP",     "key": "post_max_size",                  "value": "64MB" }
     - { "section": "PHP",     "key": "upload_max_filesize",            "value": "64MB" }
     - { "section": "opcache", "key": "opcache.enable",                 "value": "1"    }
     - { "section": "opcache", "key": "opcache.memory_consumption",     "value": "512"  }
     - { "section": "opcache", "key": "opcache.max_accelerated_files",  "value": "500"  }
    php:
     - version: php56
       fpm_ini: "{{ common_fpm_ini }}"
       cli_ini:
        - section: "PHP"
          key: "memory_limit"
          value: "2048M"
     - version: php73
       modules_extra: ['pgsql', 'gd']
       fpm_ini: "{{ common_fpm_ini }}"
     - version: php80
       modules_extra: ['pgsql', 'gd']
       fpm_ini: "{{ common_fpm_ini }}"
```

License
-------

WTFPL

Author Information
------------------

The role was created in 2020 by [Lukáš Kasič](https://github.com/lukasic).


