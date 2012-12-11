%define name	necpp
%define necpp_snapshot cvs20101121
%define version	1.3.0

Name:		necpp
Version:	1.3.0
Release:	0.%{necpp_snapshot}.2
Summary:	Analysis of the electromagnetic properties of structures
Group:		Sciences/Physics 
License:	GPL
URL:		http://www.physics.otago.ac.nz/research/electronics/nec/index.html
Source0:		http://alioth.debian.org/frs/download.php/2690/necpp.tar.gz
BuildRequires:	pkgconfig(bdw-gc)
BuildRequires:	gcc-gfortran
BuildRequires:	make
BuildRequires:	python
Provides:	nec2++

%description
The Numerical Electromagnetics Code (NEC-2) is a comprehensive 
package for the analysis of the electromagnetic properties of 
structures. It can analyse radiating properties i.e. antenna gain,
as well as scattering properties (radar cross section) of structures.
NEC-2 was originally written in FORTRAN.
NEC2++ is an extensive rewrite of NEC-2 in C++ by Tim Molteno. 
This work was helped tremendously by the work of N. Kyriazis who 
ported NEC-2 to C. The new portions of code are licensed under the 
GNU Public License (GPL). 

%prep
%setup -q -n %{name}

%build
make -f Makefile.cvs   PREFIX=/usr/bin
./configure --without-lapack

make

%install
%makeinstall_std PREFIX=/usr/lib

# make some directories
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_includedir}
install -d %{buildroot}%{_libdir}

# move files to the correct location. The package doesn't provide any PREFIX
mv %{buildroot}/usr/local/bin/nec2++ %{buildroot}%{_bindir}/nec2++
mv %{buildroot}/usr/local/bin/nec2diff %{buildroot}%{_bindir}/nec2diff
mv %{buildroot}/usr/local/include/libnecpp.h %{buildroot}%{_includedir}/libnecpp.h
mv %{buildroot}/usr/local/lib/libnecpp.a %{buildroot}%{_libdir}/libnecpp.a
mv %{buildroot}/usr/local/lib/libnecpp.la %{buildroot}%{_libdir}/libnecpp.la
mv %{buildroot}/usr/local/lib/libnecpp.so %{buildroot}%{_libdir}/libnecpp.so
mv %{buildroot}/usr/local/lib/libnecpp.so.0 %{buildroot}%{_libdir}/libnecpp.so.0
mv %{buildroot}/usr/local/lib/libnecpp.so.0.0.0 %{buildroot}%{_libdir}/libnecpp.so.0.0.0


%files
%doc README ChangeLog COPYING INSTALL
%{_bindir}/nec2++
%{_bindir}/nec2diff
%{_libdir}/libnecpp.a
%{_libdir}/libnecpp.so
%{_libdir}/libnecpp.so.0
%{_libdir}/libnecpp.so.0.0.0
%{_includedir}/libnecpp.h


%changelog
* Tue Nov 23 2010 Thomas Spuhler <tspuhler@mandriva.org> 1.3.0-0.cvs20101121.2mdv2011.0
+ Revision: 599864
- increased rel to 2
- corrected summary
- import necpp

