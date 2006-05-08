Summary:	EvIE protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u EvIE i pomocnicze
Name:		xorg-proto-evieext
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/evieext-%{version}.tar.bz2
# Source0-md5:	2507b5d0f4b2848147fbddd155aa6cfe
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%setup -q -n evieext-X11R7.0-%{version}

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/evieproto.pc
