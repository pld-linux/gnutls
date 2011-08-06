#
# Conditional build:
%bcond_with	gcrypt	# use gcrypt crypto backend instead of nettle (broken or withdrawn?)
#
Summary:	The GNU Transport Layer Security Library
Summary(pl.UTF-8):	Biblioteka GNU TLS (Transport Layer Security)
Name:		gnutls
Version:	3.0.0
Release:	1
License:	LGPL v3+ (libgnutls), GPL v3+ (extra libs and tools)
Group:		Libraries
Source0:	ftp://ftp.gnutls.org/pub/gnutls/%{name}-%{version}.tar.xz
# Source0-md5:	0677a66667f48810ff8df8335a9a9f9b
Patch0:		%{name}-info.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-pl.po-update.patch
URL:		http://www.gnu.org/software/gnutls/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	gtk-doc >= 1.1
BuildRequires:	guile-devel >= 5:1.8
BuildRequires:	libcfg+-devel
%{?with_gcrypt:BuildRequires:	libgcrypt-devel >= 1.4.0}
BuildRequires:	libstdc++-devel
BuildRequires:	libtasn1-devel >= 2.9
BuildRequires:	libtool >= 2:1.5
%{!?with_gcrypt:BuildRequires:	nettle-devel >= 2.2}
# miniopencdk is included in sources and currently maintained
# as part of gnutls, not external package
#BuildRequires:	opencdk-devel >= 0.6.6
BuildRequires:	p11-kit-devel >= 0.2
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.383
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo >= 4.8
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires(post,postun):	/sbin/ldconfig
%{?with_gcrypt:Requires:	libgcrypt >= 1.4.0}
Requires:	libtasn1 >= 2.9
%{!?with_gcrypt:Requires:	nettle >= 2.2}
#Requires:	opencdk >= 0.6.6
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
License:	LGPL v2.1+ (libgnutls), GPL v3+ (extra libs)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_gcrypt:Requires:	libgcrypt-devel >= 1.4.0}
Requires:	libtasn1-devel >= 2.9
%{!?with_gcrypt:Requires:	nettle-devel >= 2.2}
#Requires:	opencdk-devel >= 0.6.6
Requires:	p11-kit-devel >= 0.2
Requires:	zlib-devel

%description devel
Header files etc to develop gnutls applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe i inne do gnutls.

%package static
Summary:	Static gnutls library
Summary(pl.UTF-8):	Biblioteka statyczna gnutls
License:	LGPL v2.1+ (libgnutls), GPL v3+ (extra libs)
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

%package -n guile-gnutls
Summary:	Guile bindings for GnuTLS
Summary(pl.UTF-8):	Wiązania Guile do GnuTLS
License:	LGPL v2.1+ (gnutls binding), GPL v3+ (gnutls-extra binding)
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	guile >= 5:1.8

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
%{__aclocal} -I m4 -I gl/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_gcrypt:--with-libgcrypt}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# although libgnutls{,-extra}.la are obsoleted by pkg-config, there are
# .pc files missing for libgnutls{-openssl,xx}, and they need libgnutls.la

# guile module - dynamic only
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libguile-gnutls-*.{la,a}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

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

%post	-n guile-gnutls -p /sbin/ldconfig
%postun	-n guile-gnutls -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/certtool
%attr(755,root,root) %{_bindir}/gnutls-*
%attr(755,root,root) %{_bindir}/p11tool
%attr(755,root,root) %{_bindir}/psktool
%attr(755,root,root) %{_bindir}/srptool
%attr(755,root,root) %{_libdir}/libgnutls.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnutls.so.28
%attr(755,root,root) %{_libdir}/libgnutls-extra.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnutls-extra.so.28
%attr(755,root,root) %{_libdir}/libgnutls-openssl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnutls-openssl.so.27
%{_mandir}/man1/certtool.1*
%{_mandir}/man1/gnutls-*.1*
%{_mandir}/man1/p11tool.1*
%{_mandir}/man1/psktool.1*
%{_mandir}/man1/srptool.1*
%{_infodir}/gnutls.info*
%{_infodir}/gnutls-*.png
%{_infodir}/pkcs11-vision.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutls.so
%attr(755,root,root) %{_libdir}/libgnutls-extra.so
%attr(755,root,root) %{_libdir}/libgnutls-openssl.so
%{_libdir}/libgnutls.la
%{_libdir}/libgnutls-extra.la
%{_libdir}/libgnutls-openssl.la
%{_includedir}/gnutls
%exclude %{_includedir}/gnutls/gnutlsxx.h
%{_pkgconfigdir}/gnutls.pc
%{_pkgconfigdir}/gnutls-extra.pc
%{_mandir}/man3/gnutls*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnutls.a
%{_libdir}/libgnutls-extra.a
%{_libdir}/libgnutls-openssl.a

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

%files -n guile-gnutls
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguile-gnutls-v-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguile-gnutls-v-1.so.0
%attr(755,root,root) %{_libdir}/libguile-gnutls-v-1.so
%attr(755,root,root) %{_libdir}/libguile-gnutls-extra-v-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguile-gnutls-extra-v-1.so.0
%attr(755,root,root) %{_libdir}/libguile-gnutls-extra-v-1.so
%{_datadir}/guile/site/gnutls.scm
%dir %{_datadir}/guile/site/gnutls
%{_datadir}/guile/site/gnutls/extra.scm
%{_infodir}/gnutls-guile.info*
