%define version 0.1.0
%define release %mkrel 1

%define scim_version       1.4.5
%define libthai_version  0.0.4

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:		scim-thai
Summary:	Scim-thai is a Hangul IMEngine for SCIM
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPL
URL:		http://sourceforge.net/projects/scim/
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:		%{libname} = %{version}
Requires:		scim >= %{scim_version}
BuildRequires:		scim-devel >= %{scim_version}
BuildRequires:		libthai-devel >= %{libthai_version}
BuildRequires:		gettext-devel
BuildRequires:		automake1.9

%description
scim-thai is a Hangul IMEngine for SCIM.


%package common
Summary:	Common files for scim-thai library
Group:		System/Internationalization
Provides:	%{libname_orig} = %{version}-%{release}

%description common
Common files for scim-thai library.

%package -n %{libname}
Summary:	Scim-thai library
Group:		System/Internationalization
Provides:	%{libname_orig} = %{version}-%{release}
Requires:	scim-thai-common

%description -n %{libname}
scim-thai library.

%prep
%setup -q

%build
[[ ! -x configure ]] && ./bootstrap
%configure2_5x --disable-static --disable-rpath
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}
%find_lang skim-scim-thai

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files common -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_datadir}/scim/icons/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/scim-1.0/*/IMEngine/*.la
%{_libdir}/scim-1.0/*/IMEngine/*.so
%{_libdir}/scim-1.0/*/SetupUI/*.la
%{_libdir}/scim-1.0/*/SetupUI/*.so
