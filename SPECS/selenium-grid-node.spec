# and we don't need multilib anyway: 
%define __jar_repack %{nil}
Name:	selenium-grid-node	
Version:	2.43.1
Release:	1%{?dist}
Summary:	Selenium Grid node

Group:		Applications/System
License:	Apache 2.0
URL:		http://code.google.com/p/selenium/wiki/Grid2
Packager:       David Henry
BuildArch: noarch 
Source0:selenium-grid-node.json
Source1:selenium-grid-node
#BuildRequires:	
Requires: selenium-server-standalone = %{version}
%description
Selenium grid node based on selenium-server-standalone.  The node is the central point that will receive all the test request and distribute them the the right nodes. 

%prep
echo '*preping*'




%build
echo '*building*'



%install
echo '*installing*'
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/init.d/

cp %{SOURCE0} $RPM_BUILD_ROOT/etc/
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/init.d/
chmod +x $RPM_BUILD_ROOT/etc/init.d/*
mkdir -p $RPM_BUILD_ROOT/var/log/selenium

%pre
#create a non-root system user for XVFB to use
/usr/sbin/useradd -M -r -d /usr/lib/selenium -s /bin/bash -c "Selenium Grid Node" selenium-grid-user > /dev/null 2>&1 || :

%post 
chkconfig selenium-grid-node on
#service selenium-grid-node start

%preun
chkconfig --del selenium-grid-node
service selenium-grid-node stop

%postun


%files

/etc/selenium-grid-node.json
/etc/init.d/selenium-grid-node
/var/log/selenium

%changelog
