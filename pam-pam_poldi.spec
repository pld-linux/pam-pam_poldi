Summary:	PAM module implementing authentication via OpenPGP smartcards
Summary(pl.UTF-8):   Moduł PAM implementujący uwierzytelnianie za pomocą kart procesorowych OpenPGP
Name:		pam-pam_poldi
Version:	0.3
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/poldi/poldi-%{version}.tar.bz2
# Source0-md5:	83fc751869cafa2393228e586e752c71
Patch0:		poldi-info.patch
URL:		http://www.gnupg.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.7.9
BuildRequires:	libgcrypt-devel
BuildRequires:	libgpg-error-devel >= 0.7
BuildRequires:	libusb-devel
BuildRequires:	pam-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PAM module implementing authentication via OpenPGP smartcards.

%description -l pl.UTF-8
Moduł PAM implementujący uwierzytelnianie za pomocą kart procesorowych
OpenPGP.

%prep
%setup -q -n poldi-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-pam-module-directory=/lib/security
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
%attr(755,root,root) %{_bindir}/poldi-ctrl
%attr(755,root,root) /%{_lib}/security/pam_poldi.so
%{_infodir}/poldi.info*
