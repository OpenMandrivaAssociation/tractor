%undefine _debugsource_packages
Name:           tractor 
Version:        5.0.0
Release:        2
Summary:        Setup an onion routing proxy

License:        GPL-3.0-or-later
URL:            https://framagit.org/tractor/tractor
Source0:        https://framagit.org/tractor/tractor/-/archive/%{version}/tractor-%{version}.tar.bz2

BuildRequires:  gsettings-desktop-schemas
BuildRequires:  pkgconfig(glib-2.0)

Requires:  python-gobject3
Requires:  python-gi
Requires:  python-pysocks
Requires:  python-stem
Requires:  python-fire
Requires:  dconf
Requires:  tor
Requires:  glib2
Requires:  gsettings-desktop-schemas
Recommends:  %{_lib}event2.1_7

%description
Tractor is core app which lets user to setup a proxy with Onion Routing via TOR and optionally obfs4proxy in their user space. 
The goal is to ease the proccess of connecting to TOR and prevent messing up with system files.

%prep
%autosetup -p1 %{name}-%{version} -p1

%build
%py_build

%install
%py_install

install -Dm 0644 src/tractor/tractor.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ || :

%files
%{_bindir}/tractor
%{python_sitelib}/tractor/
%{python_sitelib}/traxtor-%{version}.dist-info
