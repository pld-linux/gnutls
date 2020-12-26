#
# Conditional build:
%bcond_without	dane		# libdane (DANE with DNSSEC certificate verification)
%bcond_without	openssl		# libgnutls-openssl compatibility library
%bcond_without	tpm		# TPM support in gnutls
%bcond_without	static_libs	# static libraries
%bcond_without	doc		# do not generate documentation
%bcond_without	guile		# Guile binding
#
Summary:	The GNU Transport Layer Security Library
Summary(pl.UTF-8):	Biblioteka GNU TLS (Transport Layer Security)
Name:		gnutls
Version:	3.7.0
Release:	1
License:	LGPL v2.1+ (libgnutls), LGPL v3+ (libdane), GPL v3+ (openssl library and tools)
Group:		Libraries
Source0:	ftp://ftp.gnutls.org/gcrypt/gnutls/v3.7/%{name}-%{version}.tar.xz
# Source0-md5:	1123a7bcc2fafd703e5a811bc1beb179
Patch0:		%{name}-info.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-pl.po-update.patch
URL:		https://www.gnutls.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	autogen >= 5.16
BuildRequires:	autogen-devel >= 5.16
BuildRequires:	automake >= 1:1.12.2
BuildRequires:	gcc >= 5:3.2
BuildRequires:	gettext-tools >= 0.19
BuildRequires:	gmp-devel
%{?with_doc:BuildRequires:	gtk-doc >= 1.14}
%{?with_guile:BuildRequires:	guile-devel >= 5:2.2.0}
BuildRequires:	libidn2-devel >= 2.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtasn1-devel >= 4.11
BuildRequires:	libunistring-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	nettle-devel >= 3.6
# miniopencdk is included in sources and currently maintained
# as part of gnutls, not external package
#BuildRequires:	opencdk-devel >= 0.6.6
BuildRequires:	p11-kit-devel >= 0.23.1
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.383
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
%{?with_doc:BuildRequires:	texinfo >= 4.8}
%{?with_tpm:BuildRequires:	trousers-devel >= 0.3.11}
%{?with_dane:BuildRequires:	unbound-devel}
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
%{?with_dane:Requires:	%{name}-dane = %{version}-%{release}}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautostrip	.*\.go

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
Requires:	libidn2 >= 2.0.0
Requires:	libtasn1 >= 4.11
Requires:	nettle >= 3.6
#Requires:	opencdk >= 0.6.6
Requires:	p11-kit >= 0.23.1
%{?with_tpm:Requires:	trousers-libs >= 0.3.11}
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
Requires:	libidn2-devel
Requires:	libtasn1-devel >= 4.11
Requires:	libunistring-devel
Requires:	nettle-devel >= 3.6
#Requires:	opencdk-devel >= 0.6.6
Requires:	p11-kit-devel >= 0.23.1
%{?with_tpm:Requires:	trousers-devel >= 0.3.11}
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

%package openssl
Summary:	OpenSSL compatibility library for GnuTLS
Summary(pl.UTF-8):	Biblioteka zgodności z OpenSSL dla GnuTLS
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description openssl
OpenSSL compatibility library for GnuTLS.

%description openssl -l pl.UTF-8
Biblioteka zgodności z OpenSSL dla GnuTLS.

%package openssl-devel
Summary:	Header file for gnutls-openssl library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki gnutls-openssl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-openssl = %{version}-%{release}

%description openssl-devel
Header file for gnutls-openssl library.

%description openssl-devel -l pl.UTF-8
Plik nagłówkowy biblioteki gnutls-openssl.

%package openssl-static
Summary:	Static gnutls-openssl library
Summary(pl.UTF-8):	Statyczna biblioteka gnutls-openssl
Group:		Development/Libraries
Requires:	%{name}-openssl-devel = %{version}-%{release}

%description openssl-static
Static gnutls-openssl library.

%description openssl-static -l pl.UTF-8
Statyczna biblioteka gnutls-openssl.

%package -n guile-gnutls
Summary:	Guile bindings for GnuTLS
Summary(pl.UTF-8):	Wiązania Guile do GnuTLS
License:	LGPL v2.1+
Group:		Development/Languages
Requires:	%{name}-libs = %{version}-%{release}
Requires:	guile >= 5:2.2.0

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

%build
%{__libtoolize}
%{__aclocal} -I m4 -I src/libopts/m4 -I src/gl/m4 -I lib/unistring/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_doc:--disable-doc} \
	%{!?with_guile:--disable-guile} \
	%{?with_openssl:--enable-openssl-compatibility} \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-default-trust-store-file=/etc/certs/ca-certificates.crt \
	%{!?with_tpm:--without-tpm} \
	--with-trousers-lib=%{_libdir}/libtspi.so.1

# docs build is broken with -jN
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# although libgnutls.la is obsoleted by pkg-config, there is
# .pc file missing for libgnutls-openssl, and it needs libgnutls.la

%if %{with guile}
# guile module - dynamic only
%{__rm} $RPM_BUILD_ROOT%{_libdir}/guile/2.*/extensions/guile-gnutls-*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/guile/2.*/extensions/guile-gnutls-*.a
%endif
%endif

# images for (not installed) htmlized infos - already packaged with infos
%if %{with doc}
%{__rm} $RPM_BUILD_ROOT%{_docdir}/gnutls/*.png
%endif

%{__rm} -f $RPM_BUILD_ROOT%{_infodir}/dir

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

%post	dane -p /sbin/ldconfig
%postun	dane -p /sbin/ldconfig

%post	openssl -p /sbin/ldconfig
%postun	openssl -p /sbin/ldconfig

%post	-n guile-gnutls -p /sbin/ldconfig
%postun	-n guile-gnutls -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md THANKS
%attr(755,root,root) %{_bindir}/certtool
%attr(755,root,root) %{_bindir}/gnutls-*
%attr(755,root,root) %{_bindir}/ocsptool
%attr(755,root,root) %{_bindir}/p11tool
%attr(755,root,root) %{_bindir}/psktool
%attr(755,root,root) %{_bindir}/srptool
%{?with_tpm:%attr(755,root,root) %{_bindir}/tpmtool}
%if %{with doc}
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
%endif

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutls.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnutls.so.30

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutls.so
%{_libdir}/libgnutls.la
%{_includedir}/gnutls
%{?with_dane:%exclude %{_includedir}/gnutls/dane.h}
%exclude %{_includedir}/gnutls/gnutlsxx.h
%{?with_openssl:%exclude %{_includedir}/gnutls/openssl.h}
%{_pkgconfigdir}/gnutls.pc
%{?with_doc:%{_mandir}/man3/gnutls_*.3*}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgnutls.a
%endif

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutlsxx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnutlsxx.so.28

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutlsxx.so
%{_libdir}/libgnutlsxx.la
%{_includedir}/gnutls/gnutlsxx.h

%if %{with static_libs}
%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libgnutlsxx.a
%endif

%if %{with dane}
%files dane
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/danetool
%attr(755,root,root) %{_libdir}/libgnutls-dane.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnutls-dane.so.0
%{?with_doc:%{_mandir}/man1/danetool.1*}

%files dane-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutls-dane.so
%{_libdir}/libgnutls-dane.la
%{_includedir}/gnutls/dane.h
%{_pkgconfigdir}/gnutls-dane.pc
%if %{with doc}
%{_mandir}/man3/dane_*.3*
%endif

%if %{with static_libs}
%files dane-static
%defattr(644,root,root,755)
%{_libdir}/libgnutls-dane.a
%endif
%endif

%if %{with openssl}
%files openssl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutls-openssl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnutls-openssl.so.27

%files openssl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutls-openssl.so
%{_libdir}/libgnutls-openssl.la
%{_includedir}/gnutls/openssl.h

%if %{with static_libs}
%files openssl-static
%defattr(644,root,root,755)
%{_libdir}/libgnutls-openssl.a
%endif
%endif

%if %{with guile}
%files -n guile-gnutls
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/guile/2.*/extensions/guile-gnutls-v-2.so*
%{_libdir}/guile/2.*/site-ccache/gnutls.go
%{_libdir}/guile/2.*/site-ccache/gnutls
%{_datadir}/guile/site/2.*/gnutls.scm
%{_datadir}/guile/site/2.*/gnutls
%if %{with doc}
%{_infodir}/gnutls-guile.info*
%endif
%endif
