%define major 1
%define libname %mklibname smacker %{major}
%define devname %mklibname -d smacker

Summary:	Library which can be used for decoding Smacker Video files
Name:		libsmacker
Version:	1.1
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://libsmacker.sourceforge.net
Source0:	http://sourceforge.net/projects/libsmacker/files/libsmacker-%{version}/libsmacker-%{version}r34.tar.gz

%description
libsmacker is a cross-platform C library which can be used for decoding Smacker Video files produced by RAD Game Tools.

%package -n %{libname}
Summary:	Library for accessing USB devices
Group:		System/Libraries

%description -n %{libname}
libsmacker is a cross-platform C library which can be used for decoding Smacker Video files produced by RAD Game Tools.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package includes the development files for %{name}.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{devname}
%{_libdir}/%{name}.so
