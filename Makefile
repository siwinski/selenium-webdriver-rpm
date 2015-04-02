# vim: tabstop=4:softtabstop=4:shiftwidth=4:noexpandtab

default: rpms

# TARGET: help     Print this information
.PHONY: help
help:
	# Usage:
	#   make <target>
	#
	# Targets:
	@egrep "^# TARGET:" [Mm]akefile | sed 's/^# TARGET:\s*/#   /'

# TARGET: setup    Sets up environment
.PHONY: setup
setup:
	@which rpmbuild >& /dev/null || sudo yum install -y rpm-build
	@(which rpmdev-setuptree && which spectool) >& /dev/null || sudo yum install -y rpmdevtools
	@rpmdev-setuptree

# TARGET: sources  Downloads remote source and copies local sources into build root
.PHONY: sources
sources: setup
	@spectool -g -R ./selenium.spec
	@cp -pr ./sources/* ~/rpmbuild/SOURCES/

# TARGET: rpms     Builds RPMs (DEFAULT TARGET)
.PHONY: rpms
rpms: setup sources
	@rpmbuild -ba ./selenium.spec
