%define version 0.1.1
%define release %mkrel 5

%define scim_version       1.4.5
%define libthai_version  0.0.4

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:		scim-thai
Summary:	Thai IMEngine for SCIM
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPL
URL:		http://linux.thai.net/projects/scim-thai
Source0:	ftp://linux.thai.net/pub/ThaiLinux/software/libthai/%{name}-%{version}.tar.gz
Patch0:		scim-thai-0.1.1-linkage.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:		scim-client = %{scim_api}
BuildRequires:		scim-devel >= %{scim_version}
BuildRequires:		thai-devel >= %{libthai_version}
BuildRequires:		gettext-devel
BuildRequires:		automake
Obsoletes:	%libname

%description
scim-thai is a Thai IMEngine for SCIM.

%prep
%setup -q
%patch0 -p0

%build
[[ ! -x configure ]] && ./bootstrap
%configure2_5x --disable-static --disable-rpath
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

rm -f %buildroot%{_libdir}/scim-1.0/*/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_datadir}/scim/icons/*
%{_libdir}/scim-1.0/*/IMEngine/*.so
%{_libdir}/scim-1.0/*/SetupUI/*.so
