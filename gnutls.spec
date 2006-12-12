Summary:	The GNU Transport Layer Security Library
Summary(pl):	Biblioteka GNU TLS (Transport Layer Security)
Name:		gnutls
Version:	1.2.10
Release:	2
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnutls.org/pub/gnutls/%{name}-%{version}.tar.bz2
# Source0-md5:	523273961e3cca45c92e50b2676b3c83
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/gnutls/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	libcfg+-devel
BuildRequires:	libgcrypt-devel >= 1.2.2
BuildRequires:	libtasn1-devel >= 0.2.18
BuildRequires:	libtool >= 2:1.5
BuildRequires:	lzo-devel
BuildRequires:	opencdk-devel >= 0.5.5
BuildRequires:	readline-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires(post,postun):	/sbin/ldconfig
Requires:	libgcrypt >= 1.2.2
Requires:	libtasn1 >= 0.2.18
Requires:	opencdk >= 0.5.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuTLS is a project that aims to develop a library which provides a
secure layer, over a reliable transport layer (ie. TCP/IP). Currently
the gnuTLS library implements the proposed standards by the IETF's TLS
working group.

%description -l pl
GnuTLS to projekt maj±cy na celu stworzenie biblioteki udostêpniaj±cej
pow³okê bezpieczeñstwa ponad pow³ok± transportow± (np. TCP/IP).
Aktualnie biblioteka gnuTLS implementuje standardy proponowane przez
grupê robocz± IETF TLS.

%package devel
Summary:	Header files etc to develop gnutls applications
Summary(pl):	Pliki nag³ówkowe i inne do gnutls
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgcrypt-devel >= 1.2.2
Requires:	libtasn1-devel >= 0.2.18
Requires:	opencdk-devel
Requires:	zlib-devel

%description devel
Header files etc to develop gnutls applications.

%description devel -l pl
Pliki nag³ówkowe i inne do gnutls.

%package static
Summary:	Static gnutls library
Summary(pl):	Biblioteka statyczna gnutls
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gnutls library.

%description static -l pl
Biblioteka statyczna gnutls.

%prep
%setup -q
%patch0 -p1

%build
# supplied libtool is broken (relink)
%{__libtoolize}
%{__aclocal} -I m4 -I gl/m4
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

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/certtool
%attr(755,root,root) %{_bindir}/gnutls*
%attr(755,root,root) %{_bindir}/srptool
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/certtool.1*
%{_mandir}/man1/gnutls-*
%{_mandir}/man1/srptool.1*
%{_infodir}/*.info*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libgnutls*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gnutls
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/*gnutls*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
