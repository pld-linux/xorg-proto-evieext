Summary:	EvIE protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u EvIE i pomocnicze
Name:		xorg-proto-evieext
Version:	1.0
Release:	0.02
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/proto/evieext-%{version}.tar.bz2
# Source0-md5:	e27f5064bff5c70b728871e176d4b2fa
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
EvIE protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u EvIE i pomocnicze.

%package devel
Summary:	EvIE protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u EvIE i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
EvIE protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u EvIE i pomocnicze.

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/evieproto.pc
