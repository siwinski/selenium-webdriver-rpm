
Name:	selenium-server-standalone	
Version:	2.40.0
Release:	1%{?dist}
Summary:	Selenium Webdriver Server
Group:		Applications/System
BuildArch: noarch
License:	Apache 2.0
URL:		http://seleniumhq.org/
Packager:       David Henry
Source0:http://selenium-release.storage.googleapis.com/2.40/selenium-server-standalone-%{version}.jar
#BuildRequires:	
Requires: java >= 1:1.6.0
%description
The Selenium Server is needed in order to run either Selenium RC style scripts or Remote Selenium Webdriver ones. The 2.x server is a drop-in replacement for the old Selenium RC server and is designed to be backwards compatible with your existing infrastructure.

# prevent repacking of jar (not needed)
%define __jar_repack %{nil}

%prep
echo '*preping*'




%build
echo '*building*'
pwd



%install
echo '*installing*'
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/selenium/
pwd
cp selenium-server-standalone/selenium-server-standalone-%{version}.jar $RPM_BUILD_ROOT/usr/lib/selenium/
ln -s /usr/lib/selenium/selenium-server-standalone-%{version}.jar $RPM_BUILD_ROOT/usr/lib/selenium/selenium-server-standalone.jar

%post 

%preun

%postun

%files
/usr/lib/selenium/selenium-server-standalone-%{version}.jar
/usr/lib/selenium/selenium-server-standalone.jar

%changelog
