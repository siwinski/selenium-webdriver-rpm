# Prevent repacking of jar
%define __jar_repack %{nil}

%global version_without_build %(echo %{version} | awk -F \. {'print $1 "." $2'})

Name:      selenium
Version:   2.45.0
Release:   2%{?dist}
Summary:   Selenium Webdriver Server

Group:     Applications/System
License:   ASL 2.0
URL:       http://seleniumhq.org/

Source0:   http://selenium-release.storage.googleapis.com/%{version_without_build}/selenium-server-standalone-%{version}.jar
Source1:   selenium-grid-hub.json
Source2:   selenium-grid-hub
Source3:   selenium-grid-node.json
Source4:   selenium-grid-node

BuildArch: noarch

Requires:  java >= 1:1.6.0

Requires(pre): /usr/sbin/useradd

Provides:  selenium-server-standalone = %{version}-%{release}
Obsoletes: selenium-server-standalone < %{version}-%{release}

%description
The Selenium Server is needed in order to run either Selenium RC style scripts
or Remote Selenium Webdriver ones. The 2.x server is a drop-in replacement for
the old Selenium RC server and is designed to be backwards compatible with your
existing infrastructure.

# ------------------------------------------------------------------------------

%package  grid-hub

Summary:  Selenium Grid Hub

Requires: selenium-server-standalone = %{version}

Requires(post):   chkconfig
Requires(preun):  chkconfig
Requires(preun):  initscripts
Requires(postun): initscripts

%description grid-hub
Selenium grid hub based on selenium-server-standalone.  The Hub is the central
point that will receive all the test request and distribute them the the right
nodes.

# ------------------------------------------------------------------------------

%package  grid-node

Summary:  Selenium Grid Node

Requires: selenium-server-standalone = %{version}
Requires: xorg-x11-server-Xvfb

Requires(post):   chkconfig
Requires(preun):  chkconfig
Requires(preun):  initscripts
Requires(postun): initscripts

%description grid-node
%{summary}.

# ##############################################################################

%prep
# Empty prep section, nothing required

%build
# Empty build section, nothing required

%install
# selenium / selenium-server-standalone
## JAR
install -D -p -m 0644 %{SOURCE0} %{buildroot}%{_sharedstatedir}/%{name}/selenium-server-standalone-%{version}.jar
ln -s selenium-server-standalone-%{version}.jar %{buildroot}%{_sharedstatedir}/%{name}/selenium-server-standalone.jar
## Logs
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}

# selenium-grid-hub
## Config
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/selenium-grid-hub.json
## Init
install -D -p -m 0755 %{SOURCE2} %{buildroot}%{_initddir}/selenium-grid-hub

# selenium-grid-node
## Config
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/selenium-grid-node.json
## Init
install -D -p -m 0755 %{SOURCE4} %{buildroot}%{_initddir}/selenium-grid-node

# ##############################################################################

%pre
# Add the "selenium" user
# TODO: Should use "-u ###" to specify a user ID so it is consistent
/usr/sbin/useradd -c "Selenium" -s /sbin/nologin -r \
    -d %{_sharedstatedir}/selenium selenium 2> /dev/null || :

# ##############################################################################

%post grid-hub
/sbin/chkconfig --add selenium-grid-hub

# ------------------------------------------------------------------------------

%post grid-node
/sbin/chkconfig --add selenium-grid-node

# ##############################################################################

%preun grid-hub
# Uninstall
if [ $1 -eq 0 ] ; then
    /sbin/service selenium-grid-hub stop >/dev/null 2>&1
    /sbin/chkconfig --del selenium-grid-hub
fi

# ------------------------------------------------------------------------------

%preun grid-node
# Uninstall
if [ $1 -eq 0 ] ; then
    /sbin/service selenium-grid-node stop >/dev/null 2>&1
    /sbin/chkconfig --del selenium-grid-node
fi

# ##############################################################################

%postun grid-hub
# Upgrade
if [ "$1" -ge "1" ] ; then
    /sbin/service selenium-grid-hub restart >/dev/null 2>&1 || :
fi

# ------------------------------------------------------------------------------

%postun grid-node
# Upgrade
if [ "$1" -ge "1" ] ; then
    /sbin/service selenium-grid-node restart >/dev/null 2>&1 || :
fi

# ##############################################################################

%files
%{_sharedstatedir}/%{name}/selenium-server-standalone-%{version}.jar
%{_sharedstatedir}/%{name}/selenium-server-standalone.jar
%dir %{_localstatedir}/log/%{name}

# ------------------------------------------------------------------------------

%files grid-hub
%config(noreplace) %{_sysconfdir}/selenium-grid-hub.json
%{_initddir}/selenium-grid-hub

# ------------------------------------------------------------------------------

%files grid-node
%config(noreplace) %{_sysconfdir}/selenium-grid-node.json
%{_initddir}/selenium-grid-node

# ##############################################################################

%changelog
* Sat Apr 04 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.45.0-2
- Initial single-spec version
