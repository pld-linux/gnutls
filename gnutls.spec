Summary:	The GNU Transport Layer Security Library
Summary(pl.UTF-8):	Biblioteka GNU TLS (Transport Layer Security)
Name:		gnutls
Version:	2.0.0
Release:	2
License:	LGPL v2.1+ (libgnutls), GPL v2+ (extra libs and tools)
Group:		Libraries
Source0:	ftp://ftp.gnutls.org/pub/gnutls/%{name}-%{version}.tar.bz2
# Source0-md5:	181b2ff554a83e6cf85505ea16699d39
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/gnutls/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-devel >= 0.14.5
BuildRequires:	libcfg+-devel
BuildRequires:	libgcrypt-devel >= 1.2.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtasn1-devel >= 1.1
BuildRequires:	libtool >= 2:1.5
BuildRequires:	lzo-devel
BuildRequires:	opencdk-devel >= 0.6.4
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.383
BuildRequires:	texinfo >= 4.8
BuildRequires:	zlib-devel
Requires(post,postun):	/sbin/ldconfig
Requires:	libgcrypt >= 1.2.2
Requires:	libtasn1 >= 1.1
Requires:	opencdk >= 0.6.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuTLS is a project that aims to develop a library which provides a
secure layer, over a reliable transport layer (ie. TCP/IP). Currently
the gnuTLS library implements the proposed standards by the IETF's TLS
working group.

%description -l pl.UTF-8
GnuTLS to projekt mający na celu stworzenie biblioteki udostępniającej
powłokę bezpieczeństwa ponad powłoką transportową (np. TCP/IP).
Aktualnie biblioteka gnuTLS implementuje standardy proponowane przez
grupę roboczą IETF TLS.

%package devel
Summary:	Header files etc to develop gnutls applications
Summary(pl.UTF-8):	Pliki nagłówkowe i inne do gnutls
License:	LGPL v2.1+ (libgnutls), GPL v2+ (extra libs)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgcrypt-devel >= 1.2.2
Requires:	libtasn1-devel >= 1.1
Requires:	opencdk-devel >= 0.6.4
Requires:	zlib-devel

%description devel
Header files etc to develop gnutls applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe i inne do gnutls.

%package static
Summary:	Static gnutls library
Summary(pl.UTF-8):	Biblioteka statyczna gnutls
License:	LGPL v2.1+ (libgnutls), GPL v2+ (extra libs)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gnutls library.

%description static -l pl.UTF-8
Biblioteka statyczna gnutls.

%package c++
Summary:	libgnutlsxx - C++ interface to gnutls library
Summary(pl.UTF-8):	libgnutlsxx - interfejs C++ do biblioteki gnutls
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
libgnutlsxx - C++ interface to gnutls library.

%description c++ -l pl.UTF-8
libgnutlsxx - interfejs C++ do biblioteki gnutls.

%package c++-devel
Summary:	Header files for libgnutlsxx, a C++ interface to gnutls library
Summary(pl.UTF-8):	Pliki nagłówkowe libgnutlsxx - interfejsu C++ do biblioteki gnutls
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
Header files for libgnutlsxx, a C++ interface to gnutls library.

%description c++-devel -l pl.UTF-8
Pliki nagłówkowe libgnutlsxx - interfejsu C++ do biblioteki gnutls.

%package c++-static
Summary:	Static version of libgnutlsxx, a C++ interface to gnutls library
Summary(pl.UTF-8):	Statyczna wersja libgnutlsxx - interfejsu C++ do biblioteki gnutls
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
Static version of libgnutlsxx, a C++ interface to gnutls library.

%description c++-static -l pl.UTF-8
Statyczna wersja libgnutlsxx - interfejsu C++ do biblioteki gnutls.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4 -I gl/m4 -I lgl/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-dependency-tracking

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/certtool
%attr(755,root,root) %{_bindir}/gnutls-*
%attr(755,root,root) %{_bindir}/psktool
%attr(755,root,root) %{_bindir}/srptool
%attr(755,root,root) %{_libdir}/libgnutls.so.*.*.*
%attr(755,root,root) %{_libdir}/libgnutls-extra.so.*.*.*
%attr(755,root,root) %{_libdir}/libgnutls-openssl.so.*.*.*
%{_mandir}/man1/certtool.1*
%{_mandir}/man1/gnutls-*.1*
%{_mandir}/man1/psktool.1*
%{_mandir}/man1/srptool.1*
%{_infodir}/gnutls.info*
%{_infodir}/gnutls-*.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libgnutls-config
%attr(755,root,root) %{_bindir}/libgnutls-extra-config
%attr(755,root,root) %{_libdir}/libgnutls.so
%attr(755,root,root) %{_libdir}/libgnutls-extra.so
%attr(755,root,root) %{_libdir}/libgnutls-openssl.so
%{_libdir}/libgnutls.la
%{_libdir}/libgnutls-extra.la
%{_libdir}/libgnutls-openssl.la
%{_includedir}/gnutls
%exclude %{_includedir}/gnutls/gnutlsxx.h
%{_aclocaldir}/libgnutls.m4
%{_aclocaldir}/libgnutls-extra.m4
%{_pkgconfigdir}/gnutls.pc
%{_pkgconfigdir}/gnutls-extra.pc
%{_mandir}/man3/*gnutls*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnutls.a
%{_libdir}/libgnutls-extra.a
%{_libdir}/libgnutls-openssl.a

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutlsxx.so.*.*.*

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutlsxx.so
%{_libdir}/libgnutlsxx.la
%{_includedir}/gnutls/gnutlsxx.h

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libgnutlsxx.a
