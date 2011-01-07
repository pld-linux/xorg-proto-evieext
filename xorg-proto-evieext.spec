Summary:	EvIE extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia EvIE
Name:		xorg-proto-evieext
Version:	1.1.1
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/evieext-%{version}.tar.bz2
# Source0-md5:	98bd86a13686f65f0873070fdee6efc7
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extended Visual Information Extension (XEVIE) defines a protocol for a
client to determine information about core X visuals beyond what the
core protocol provides.

%description -l pl.UTF-8
Rozszerzenie XEVIE (Extended Visual Information Extension) definiuje
protokół pozwalający klientowi poznać informacje o poszczególnych
ekranach X ukrytych za protokołem.

%package devel
Summary:	EvIE extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia EvIE
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Extended Visual Information Extension (XEVIE) defines a protocol for a
client to determine information about core X visuals beyond what the
core protocol provides.

%description devel -l pl.UTF-8
Rozszerzenie XEVIE (Extended Visual Information Extension) definiuje
protokół pozwalający klientowi poznać informacje o poszczególnych
ekranach X ukrytych za protokołem.

%prep
%setup -q -n evieext-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%{_includedir}/X11/extensions/Xeviestr.h
%{_includedir}/X11/extensions/evieproto.h
%{_pkgconfigdir}/evieproto.pc
