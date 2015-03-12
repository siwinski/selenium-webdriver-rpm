SELENIUM_MAJOR_VERSION=2.45
SELENIUM_BUILD=0

all: prepare-build build

install-deps:
	sudo yum install -y rpm-build rpmdevtools readline-devel ncurses-devel gdbm-devel tcl-devel openssl-devel db4-devel byacc libyaml-devel libffi-devel make

prepare-build:
	rpmdev-setuptree
	wget -c http://selenium-release.storage.googleapis.com/${SELENIUM_MAJOR_VERSION}/selenium-server-standalone-${SELENIUM_MAJOR_VERSION}.${SELENIUM_BUILD}.jar
	mv selenium-server-standalone-${SELENIUM_MAJOR_VERSION}.${SELENIUM_BUILD}.jar ~/rpmbuild/SOURCES/
	rsync -av rpmbuild/ ~/rpmbuild/

build:
	rpmbuild -bb rpmbuild/SPECS/selenium-grid-hub.spec
	rpmbuild -bb rpmbuild/SPECS/selenium-grid-node.spec
	rpmbuild -bb rpmbuild/SPECS/selenium-server-standalone.spec
