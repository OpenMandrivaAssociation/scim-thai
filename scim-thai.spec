Name:		scim-thai
Summary:	Thai IMEngine for SCIM
Version:	0.1.3
Release:	2
License:	GPLv2+
Group:		System/Internationalization
Url:		https://linux.thai.net/projects/scim-thai
Source0:	ftp://linux.thai.net/pub/ThaiLinux/software/libthai/%{name}-%{version}.tar.gz
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(libthai)
BuildRequires:	pkgconfig(scim)

%description
Thai IMEngine for SCIM.

%files -f %{name}.lang
%doc AUTHORS COPYING
%{_datadir}/scim/icons/*
%{_libdir}/scim-1.0/*/IMEngine/*.so
%{_libdir}/scim-1.0/*/SetupUI/*.so

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--disable-rpath
%make

%install
%makeinstall_std

%find_lang %{name}

