Summary:	EvIE extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia EvIE
Name:		xorg-proto-evieext
Version:	1.1.0
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/evieext-%{version}.tar.bz2
# Source0-md5:	5c74f61d6f77b2e6a083b2b31000be42
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EvIE extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia EvIE.

%package devel
Summary:	EvIE extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia EvIE
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
EvIE extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia EvIE.

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
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/Xeviestr.h
%{_includedir}/X11/extensions/evieproto.h
%{_pkgconfigdir}/evieproto.pc
