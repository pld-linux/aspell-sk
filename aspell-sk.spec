Summary:	Slovak dictionary for aspell
Summary(pl.UTF-8):	Słownik słowacki dla aspella
Name:		aspell-sk
Version:	2.00
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2 or LGPL v2.1 or MPL 1.1
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/sk/aspell6-sk-%{version}-%{subv}.tar.bz2
# Source0-md5:	b7ac2b1cb31bad0cd676c1027fa46dc4
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Slovak dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik słowacki (lista słów) dla aspella.

%prep
%setup -q -n aspell6-sk-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README doc/{AUTHORS,CHANGELOG}
%{_libdir}/aspell/*
%{_datadir}/aspell/*
