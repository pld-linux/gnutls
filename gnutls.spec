Summary:	The GNU Transport Layer Security Library
Summary(pl):	Biblioteka GNU TLS (Transport Layer Security)
Name:		gnutls
Version:	0.8.10
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnutls.org/pub/gnutls/%{name}-%{version}.tar.gz
# Source0-md5:	11130b920b1395d03e559beebf6b3c2b
Patch0:		%{name}-libgcrypt.patch
Patch1:		%{name}-opencdk.patch
URL:		http://www.gnu.org/software/gnutls/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libgcrypt-devel >= 1.1.42
BuildRequires:	libtasn1-devel
BuildRequires:	lzo-devel
BuildRequires:	opencdk-devel >= 0.5.1
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuTLS is a project that aims to develop a library which provides a
secure layer, over a reliable transport layer (ie. TCP/IP). Currently
the gnuTLS library implements the proposed standards by the IETF's TLS
working group.

%description -l pl
GnuTLS to projekt maj�cy na celu stworzenie biblioteki udost�pniaj�cej
pow�ok� bezpiecze�stwa ponad pow�ok� transportow� (np. TCP/IP).
Aktualnie biblioteka gnuTLS implementuje standardy proponowane przez
grup� robocz� IETF TLS.

%package devel
Summary:	Header files etc to develop gnutls applications
Summary(pl):	Pliki nag��wkowe i inne do gnutls
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libgcrypt-devel >= 1.1.42
Requires:	libtasn1-devel
Requires:	zlib-devel

%description devel
Header files etc to develop gnutls applications.

%description devel -l pl
Pliki nag��wkowe i inne do gnutls.

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
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gnutls
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
