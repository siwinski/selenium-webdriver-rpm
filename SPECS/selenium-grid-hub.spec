# and we don't need multilib anyway: 
%define __jar_repack %{nil}
Name:	selenium-grid-hub	
Version:	2.40.0
Release:	1%{?dist}
Summary:	Selenium Grid Hub

Group:		Applications/System
License:	Apache 2.0
URL:		http://code.google.com/p/selenium/wiki/Grid2
Packager:       David Henry
BuildArch: noarch 
Source0:selenium-grid-hub.json
Source1:selenium-grid-hub
#BuildRequires:	
Requires: selenium-server-standalone = %{version}
%description
Selenium grid hub based on selenium-server-standalone.  The Hub is the central point that will receive all the test request and distribute them the the right nodes. 

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

%post 
chkconfig selenium-grid-hub on
service selenium-grid-hub start

%preun
chkconfig --del selenium-grid-hub
service selenium-grid-hub stop

%postun


%files

/etc/selenium-grid-hub.json
/etc/init.d/selenium-grid-hub
/var/log/selenium

%changelog
