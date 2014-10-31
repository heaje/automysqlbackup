Summary: automysqlbackup
Name: automysqlbackup
Version: 3.0
Release: 1.07%{?dist}
License: GPLv2+
Group: Development/Tools
Source: automysqlbackup-v3.0_rc6.tar.gz
URL: http://sourceforge.net/projects/automysqlbackup/
BuildRoot: %{_tmppath}/
BuildArch: noarch

%description
AutoMySQLBackup with a basic configuration will create Daily, Weekly and Monthly backups of one or more of your MySQL databases from one or more of your MySQL servers.

%prep
%setup -q -n .

%build

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/{etc/automysqlbackup,usr/bin}
install -m 644 automysqlbackup.conf $RPM_BUILD_ROOT/etc/automysqlbackup/
install -m 755 automysqlbackup $RPM_BUILD_ROOT/usr/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%dir  %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/automysqlbackup.conf
%{_bindir}/automysqlbackup

%changelog
* Fri Oct 31 2014 Corey Shaw <corey.shaw@gmail.com>
- Slight modification to original SPEC from http://www.jur-linux.org/rpms/el-updates/6.0/SRPMS/automysqlbackup-3.0-1.07.el6.src.rpm
