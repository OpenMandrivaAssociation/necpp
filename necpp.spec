%define necpp_snapshot cvs20101121

%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Analysis of the electromagnetic properties of structures
Name:		necpp
Version:	1.3.0
Release:	0.%{necpp_snapshot}.3
License:	GPLv2+
Group:		Sciences/Physics
Url:		https://www.physics.otago.ac.nz/research/electronics/nec/index.html
Source0:	http://alioth.debian.org/frs/download.php/2690/necpp.tar.gz
Patch0:		necpp-sfmt.patch
BuildRequires:	gcc-gfortran
BuildRequires:	pkgconfig(bdw-gc)
Provides:	nec2++ = %{EVRD}

%description
The Numerical Electromagnetics Code (NEC-2) is a comprehensive package for
the analysis of the electromagnetic properties of structures. It can analyse
radiating properties i.e. antenna gain, as well as scattering properties
(radar cross section) of structures. NEC-2 was originally written in FORTRAN.

NEC2++ is an extensive rewrite of NEC-2 in C++ by Tim Molteno. This work was
helped tremendously by the work of N. Kyriazis who ported NEC-2 to C. The new
portions of code are licensed under the GNU Public License (GPL).

%files
%doc README ChangeLog COPYING INSTALL
%{_bindir}/nec2++
%{_bindir}/nec2diff

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries
Conflicts:	%{name} < 1.3.0-0.cvs20101121.3

%description -n %{libname}
Shared library for %{name}.

%files -n %{libname}
%{_libdir}/libnecpp.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Shared library for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{name} < 1.3.0-0.cvs20101121.3

%description -n %{devname}
Shared library for %{name}.

%files -n %{devname}
%{_includedir}/libnecpp.h
%{_libdir}/libnecpp.so
%{_libdir}/libnecpp.a

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}
%patch0 -p1

find . -name "Makefile*" -o -name "*.m4" -o -name "configure*" |xargs sed -i -e 's,configure.in,configure.ac,g'

%build
make -f Makefile.cvs PREFIX=/usr/bin
#./configure --without-lapack
%configure2_5x \
	--without-lapack
make

%install
%makeinstall_std

