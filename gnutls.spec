Summary:	The GNU Transport Layer Security Library
Summary(pl):	Biblioteka GNU TLS (Transport Layer Security)
Name:		gnutls
Version:	0.2.9
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/libgcrypt/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/gnutls/
BuildRequires:	libgcrypt-devel >= 1.1.4
BuildRequires:	libmcrypt-devel
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
Requires:	%{name} = %{version}

%description devel
Header files etc to develop gnutls applications.

%description devel -l pl
Pliki nag³ówkowe i inne do gnutls.

%package static
Summary:	Static gnutls library
Summary(pl):	Biblioteka statyczna gnutls
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static gnutls library.

%description static -l pl
Biblioteka statyczna gnutls.

%prep
%setup -q

%build
%configure \
	--with-mcrypt \
	--with-mhash
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf AUTHORS NEWS README THANKS

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*.h
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
