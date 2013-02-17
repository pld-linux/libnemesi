#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
#
Summary:	libNeMeSi - the RTSP/RTP client library
Summary(pl.UTF-8):	libNeMeSi - biblioteka klienta RTSP/RTP
Name:		libnemesi
Version:	0.7.0
%define	subver	20101208
Release:	0.%{subver}.1
License:	LGPL v2.1+
Group:		Libraries
# git clone git://git.lscube.org/libnemesi
Source0:	%{name}.tar.xz
# Source0-md5:	1ba1385440e44dde3009a285ae1164aa
Patch0:		%{name}-format.patch
URL:		http://lscube.org/projects/libnemesi_rtsp_rtp_client_library
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
# to generate ChangeLog from git snapshot
BuildRequires:	git-core
BuildRequires:	libsctp-devel
BuildRequires:	libtool
BuildRequires:	netembryo-devel >= 0.1.1
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	netembryo >= 0.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libnemesi lets you add multimedia streaming playback in your
applications in a quick and straightforward way. This software,
derived from the experience matured with NeMeSi is fully compliant
with IETF's standards for real-time streaming of multimedia contents
over Internet. libnemesi implements RTSP - Real-Time Streaming
Protocol (RFC2326) and RTP/RTCP - Real-Time Transport Protocol/RTP
Control Protocol (RFC3550) supporting the RTP Profile for Audio and
Video Conferences with Minimal Control (RFC3551).

%description -l pl.UTF-8
Libnemesi pozwala szybkie i proste dodawanie do aplikacji obsługi
odtwarzania strumieni multimedialnych. Ta biblioteka, wywodząca się z
doświadczenia nabytego przy projekcie NeMeSi, jest w pełni zgodna ze
standardami IETF do przesyłania strumieni treści multimedialnych przez
Internet w czasie rzeczywistym. Zawiera implementacje protokołów RTSP
(Real-Time Stereaming Protocol - RFC2326) oraz RTP/RTCP (RealTime
Transport Protocol/RTP Control Protocol - RFC3550), obsługujące profil
RTP dla konferencji z dźwiękiem i obrazem o minimalnej kontroli (RTP
Profile for Audio and Video Conferences with Minimal Control -
RFC3551).

%package devel
Summary:	Header files for libNeMeSi library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libNeMeSi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	netembryo-devel >= 0.1.1

%description devel
Header files for libNeMeSi library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libNeMeSi.

%package static
Summary:	Static libNeMeSi library
Summary(pl.UTF-8):	Statyczna biblioteka libNeMeSi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libNeMeSi library.

%description static -l pl.UTF-8
Statyczna biblioteka libNeMeSi.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-examples \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libnemesi.la
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libnemesi

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libnemesi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnemesi.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnemesi.so
%{_includedir}/nemesi
%{_pkgconfigdir}/libnemesi.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnemesi.a
