selenium-webdriver-rpm
======================


# What is this spec?

This spec is a first attempt for packaging selenium standalone server (see http://seleniumhq.org/), and some init.d scripts I hacked together for running a selenium grid (see https://code.google.com/p/selenium/wiki/Grid2) as RPMS  for install on RHEL, Fedora, and other RPM based Linux systems.

My goal is to eventually submit this to EPEL and become a package maintainer.  I have a long way to go ;)

DISCLAIMER: I MAKE NO CLAIM THAT I KNOW WHAT I AM DOING.  USE AT YOUR OWN RISK!  Watch this space for improved and refined versions as I learn more about how to properly package RPMs and daemons.  I welcome and appreciate your feedback, assistance, or patches.

### How to build

#### Fedora/RHEL/CentOS

    make install-deps # only once, it uses sudo to install the build requirements
    make

### What do these 3 .rpm files provide?
+ selenium-server-standalone rpm packaged version of selenium-server-standalone jar from http://seleniumhq.org/download/
+ selenium-grid-hub rpm packaged daemon script that will start a selenium grid hub.  Configuration files can be found in /etc/selenium/
+ selenium-grid-node rpm packaged daemon script that will start a selenium grid node.  Browsers will be run in an XVFB session. Configuration files can also be found in /etc/selenium/


### Work to do, problems to fix:

+ selenium-server-standalone is packaged from a downloaded binary.  As I understand, it will need to be built from source to meet EPEL packaging standards.
+ selenium-grid-hub and selenium-grid-node /etc/init.d scripts are not very fault tolerant.  They sometimes leave lockfiles in place or don't properly stop the selenium thread.
+ Documentation in this file is not sufficient.  I would like to add man files to the RPMS.

###


### Distro support

Tested on:

* RHEL 6.4
* Fedora 19



