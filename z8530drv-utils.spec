Name:         z8530drv-utils
License:      GPL
Group:        Communications
Provides:     z8530drv
Obsoletes:    z8530drv
Version:      3.0.3
Release:      2
Summary:      Linux driver for Z8530 based HDLC cards for AX.25
Source0:      ftp://ftp.ccac.rwth-aachen.de/pub/jr/z8530drv-utils_3.0-3.tar.gz
Patch0:        z8530drv-gcc4.diff
Patch1:       z8530drv-buildserv.diff
URL:          http://yaina.de/jreuter/linux/scc.en.html
# Patch:   z8530drv-utils-3.0.dif

%description
Utilities for the generic Z8530 AX.25 device driver



Authors:
--------
    Joerg Reuter <jreuter@yaina.de>

%prep
%setup -q -n z8530drv-utils-3.0
%patch0 -p0
%patch1 -p1

%build
make dep
make

%install
mkdir -p %{buildroot}/{etc,etc/ax25,usr,usr/sbin,sbin}
make prefix=%{buildroot} install

%files
%doc README
%doc z8530drv-utils-3.0.lsm
%doc doc/Copying.Z8530DRV
%doc doc/FAQ
%doc doc/scc_eng.doc
%doc doc/scc_ger.doc
%dir /etc/ax25
%config /etc/ax25/z8530drv.conf
/sbin/sccstat
/sbin/sccinit
/sbin/sccparam
%{_sbindir}/sccgencfg
%{_sbindir}/kissbridge


%changelog
* Thu May 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.0.3-1
+ Revision: 798058
- imported package z8530drv-utils

