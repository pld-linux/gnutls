#
# Conditional build:
%bcond_with	gcrypt	# use gcrypt crypto backend instead of nettle (withdrawn?)
%bcond_without	dane	# libdane (DANE with DNSSEC certificate verification)
%bcond_with	tpm	# TPM support in gnutls (cannot be used with GPL programs)
#
Summary:	The GNU Transport Layer Security Library
Summary(pl.UTF-8):	Biblioteka GNU TLS (Transport Layer Security)
Name:		gnutls
Version:	3.2.1
Release:	1
License:	LGPL v3+ (libgnutls), GPL v3+ (openssl library and tools)
Group:		Libraries
Source0:	ftp://ftp.gnutls.org/gcrypt/gnutls/v3.2/%{name}-%{version}.tar.lz
# Source0-md5:	157386119a90f458fecf8303584f9417
Patch0:		%{name}-info.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-pl.po-update.patch
URL:		http://www.gnutls.org/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.11.3
BuildRequires:	gettext-devel >= 0.18
BuildRequires:	gtk-doc >= 1.1
BuildRequires:	guile-devel >= 5:2.0
BuildRequires:	libcfg+-devel
%{?with_gcrypt:BuildRequires:	libgcrypt-devel >= 1.4.0}
BuildRequires:	libidn-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtasn1-devel >= 2.14
BuildRequires:	libtool >= 2:1.5
BuildRequires:	lzip
%{!?with_gcrypt:BuildRequires:	nettle-devel >= 2.7}
# miniopencdk is included in sources and currently maintained
# as part of gnutls, not external package
#BuildRequires:	opencdk-devel >= 0.6.6
BuildRequires:	p11-kit-devel >= 0.11
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.383
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo >= 4.8
%{?with_tpm:BuildRequires:	trousers-devel}
%{?with_dane:BuildRequires:	unbound-devel}
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
%{?with_dane:Requires:	%{name}-dane = %{version}-%{release}}
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

%package libs
Summary:	GnuTLS shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone GnuTLS
Group:		Libraries
%{?with_gcrypt:Requires:	libgcrypt >= 1.4.0}
Requires:	libtasn1 >= 2.14
%{!?with_gcrypt:Requires:	nettle >= 2.7}
#Requires:	opencdk >= 0.6.6
Requires:	p11-kit >= 0.11
Conflicts:	gnutls < 3.2.0

%description libs
GnuTLS shared libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone GnuTLS.

%package devel
Summary:	Header files etc to develop gnutls applications
Summary(pl.UTF-8):	Pliki nagłówkowe i inne do gnutls
License:	LGPL v2.1+ (libgnutls), GPL v3+ (openssl library)
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
%{?with_gcrypt:Requires:	libgcrypt-devel >= 1.4.0}
Requires:	libtasn1-devel >= 2.14
%{!?with_gcrypt:Requires:	nettle-devel >= 2.7}
#Requires:	opencdk-devel >= 0.6.6
Requires:	p11-kit-devel >= 0.11
%{?with_tpm:Requires:	trousers-devel}
Requires:	zlib-devel

%description devel
Header files etc to develop gnutls applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe i inne do gnutls.

%package static
Summary:	Static gnutls library
Summary(pl.UTF-8):	Biblioteka statyczna gnutls
License:	LGPL v2.1+ (libgnutls), GPL v3+ (openssl library)
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
Requires:	%{name}-libs = %{version}-%{release}

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

%package dane
Summary:	DANE security library
Summary(pl.UTF-8):	Biblioteka bezpieczeństwa DANE
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description dane
DANE security library.

%description dane -l pl.UTF-8
Biblioteka bezpieczeństwa DANE.

%package dane-devel
Summary:	Header file for DANE security library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki bezpieczeństwa DANE
Group:		Development/Libraries
Requires:	%{name}-dane = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	unbound-devel

%description dane-devel
Header file for DANE security library.

%description dane-devel -l pl.UTF-8
Plik nagłówkowy biblioteki bezpieczeństwa DANE.

%package dane-static
Summary:	Static DANE security library
Summary(pl.UTF-8):	Statyczna biblioteka bezpieczeństwa DANE
Group:		Development/Libraries
Requires:	%{name}-dane-devel = %{version}-%{release}

%description dane-static
Static DANE security library.

%description dane-static -l pl.UTF-8
Statyczna biblioteka bezpieczeństwa DANE.

%package -n guile-gnutls
Summary:	Guile bindings for GnuTLS
Summary(pl.UTF-8):	Wiązania Guile do GnuTLS
License:	LGPL v2.1+
Group:		Development/Languages
Requires:	%{name}-libs = %{version}-%{release}
Requires:	guile >= 5:2.0

%description -n guile-gnutls
Guile bindings for GnuTLS.

%description -n guile-gnutls -l pl.UTF-8
Wiązania Guile do GnuTLS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%{__rm} po/stamp-po

# remove it when "linking libtool libraries using a non-POSIX archiver ..." warning is gone
# (after gnutls or libtool change)
%{__sed} -i -e '/AM_INIT_AUTOMAKE/s/-Werror//' configure.ac

%build
%{__libtoolize}
%{__aclocal} -I m4 -I gl/m4 -I src/libopts/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-heartbeat-support \
	--with-default-trust-store-file=/etc/certs/ca-certificates.crt \
	%{?with_gcrypt:--with-libgcrypt} \
	%{?with_tpm:--with-tpm}

# docs build is broken with -jN
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# although libgnutls.la is obsoleted by pkg-config, there is
# .pc file missing for libgnutls-openssl, and it needs libgnutls.la

# guile module - dynamic only
%{__rm} $RPM_BUILD_ROOT%{_libdir}/guile/2.0/guile-gnutls-*.{la,a}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%post	-n guile-gnutls -p /sbin/ldconfig
%postun	-n guile-gnutls -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/certtool
%attr(755,root,root) %{_bindir}/crywrap
%attr(755,root,root) %{_bindir}/gnutls-*
%attr(755,root,root) %{_bindir}/ocsptool
%attr(755,root,root) %{_bindir}/p11tool
%attr(755,root,root) %{_bindir}/psktool
%attr(755,root,root) %{_bindir}/srptool
%{?with_tpm:%attr(755,root,root) %{_bindir}/tpmtool}
%{_mandir}/man1/certtool.1*
%{_mandir}/man1/gnutls-*.1*
%{_mandir}/man1/ocsptool.1*
%{_mandir}/man1/p11tool.1*
%{_mandir}/man1/psktool.1*
%{_mandir}/man1/srptool.1*
%{_mandir}/man1/tpmtool.1*
%{_infodir}/gnutls.info*
%{_infodir}/gnutls-*.png
%{_infodir}/pkcs11-vision.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutls.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnutls.so.28
%attr(755,root,root) %{_libdir}/libgnutls-openssl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnutls-openssl.so.27
%attr(755,root,root) %{_libdir}/libgnutls-xssl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnutls-xssl.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutls.so
%attr(755,root,root) %{_libdir}/libgnutls-openssl.so
%attr(755,root,root) %{_libdir}/libgnutls-xssl.so
%{_libdir}/libgnutls.la
%{_libdir}/libgnutls-openssl.la
%{_libdir}/libgnutls-xssl.la
%{_includedir}/gnutls
%{?with_dane:%exclude %{_includedir}/gnutls/dane.h}
%exclude %{_includedir}/gnutls/gnutlsxx.h
%{_pkgconfigdir}/gnutls.pc
%{_mandir}/man3/gnutls_*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnutls.a
%{_libdir}/libgnutls-openssl.a
%{_libdir}/libgnutls-xssl.a

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutlsxx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnutlsxx.so.28

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutlsxx.so
%{_libdir}/libgnutlsxx.la
%{_includedir}/gnutls/gnutlsxx.h

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libgnutlsxx.a

%if %{with dane}
%files dane
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/danetool
%attr(755,root,root) %{_libdir}/libgnutls-dane.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnutls-dane.so.0
%{_mandir}/man1/danetool.1*

%files dane-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutls-dane.so
%{_libdir}/libgnutls-dane.la
%{_includedir}/gnutls/dane.h
%{_pkgconfigdir}/gnutls-dane.pc

%files dane-static
%defattr(644,root,root,755)
%{_libdir}/libgnutls-dane.a
%endif

%files -n guile-gnutls
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/guile/2.0/guile-gnutls-v-2.so*
%{_datadir}/guile/site/gnutls.scm
%{_datadir}/guile/site/gnutls
%{_infodir}/gnutls-guile.info*
