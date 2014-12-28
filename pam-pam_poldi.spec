Summary:	PAM module implementing authentication via OpenPGP smartcards
Summary(pl.UTF-8):	Moduł PAM implementujący uwierzytelnianie za pomocą kart procesorowych OpenPGP
Name:		pam-pam_poldi
Version:	0.4.1
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/poldi/poldi-%{version}.tar.bz2
# Source0-md5:	197986f9ba6aec9a91ee4610f4c6be8b
Patch0:		poldi-info.patch
Patch1:		poldi-system-libassuan.patch
URL:		http://www.gnupg.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.7.9
BuildRequires:	gettext-tools
BuildRequires:	libassuan-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libgpg-error-devel >= 0.7
BuildRequires:	libksba-devel >= 1.0.2
BuildRequires:	pam-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Poldi is a PAM module implementing authentication via OpenPGP
smartcards.

%description -l pl.UTF-8
Poldi to moduł PAM implementujący uwierzytelnianie kartami
procesorowymi OpenPGP.

%prep
%setup -q -n poldi-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-pam-module-directory=/%{_lib}/security
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# missing in make install
install -D src/pam/pam_poldi.so $RPM_BUILD_ROOT/%{_lib}/security/pam_poldi.so

#find_lang poldi

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
# -f poldi.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog EXPERIMENTAL MIGRATION NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/poldi-ctrl
%attr(755,root,root) /%{_lib}/security/pam_poldi.so
%{_infodir}/poldi.info*
