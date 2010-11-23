%define name	necpp
%define necpp_snapshot cvs20101121
%define version	1.3.0
%define rel	1

Name:		%{name}
Version:	%{version}
Release:	%mkrel 0.%{necpp_snapshot}.%{rel}
Summary:	SDCC - Small Device C Compiler
Group:		Sciences/Physics 
License:	GPL
URL:		http://www.physics.otago.ac.nz/research/electronics/nec/index.html
Source:		http://alioth.debian.org/frs/download.php/2690/necpp.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	libgc-devel
BuildRequires:	libstdc++-devel
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
rm -rf %{buildroot}
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


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog COPYING INSTALL
%attr(-,root,root) 
%{_bindir}/nec2++
%{_bindir}/nec2diff
%{_libdir}/libnecpp.a
%{_libdir}/libnecpp.la
%{_libdir}/libnecpp.so
%{_libdir}/libnecpp.so.0
%{_libdir}/libnecpp.so.0.0.0
%{_includedir}/libnecpp.h
