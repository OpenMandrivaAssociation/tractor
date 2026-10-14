%undefine _debugsource_packages
Name:           tractor
Version:        5.2.0
Release:        1
Summary:        Setup an onion routing proxy
License:        GPL-3.0-or-later
Group:          Networking/Other
URL:            https://framagit.org/tractor/tractor
Source0:        https://framagit.org/tractor/tractor/-/archive/%{version}/tractor-%{version}.tar.bz2

BuildRequires:  gsettings-desktop-schemas
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(flit-core)

Requires:       python%{pyver}dist(pygobject)
Requires:       python%{pyver}dist(pysocks)
Requires:       python%{pyver}dist(stem)
Requires:       python%{pyver}dist(fire)
Requires:  dconf
Requires:  tor
Requires:  glib2
Requires:  gsettings-desktop-schemas
Recommends:  %{_lib}event2.1_7

%description
Tractor is core app which lets user to setup a proxy with Onion Routing via TOR and optionally obfs4proxy in their user space. 
The goal is to ease the proccess of connecting to TOR and prevent messing up with system files.

%prep
%autosetup -p1 -n %{name}-%{version}
# Upstream names the distribution traxtor and ships no build-system table.
printf '%s\n' '[build-system]' 'requires = ["flit_core>=3.4"]' 'build-backend = "flit_core.buildapi"' >> pyproject.toml

%build
%py_build

%install
%py_install

install -Dm 0644 src/tractor/tractor.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/tractor.gschema.xml

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ || :

%files
%{_bindir}/tractor
%{_datadir}/glib-2.0/schemas/tractor.gschema.xml
%{python_sitelib}/tractor/
%{python_sitelib}/traxtor-%{version}.dist-info
