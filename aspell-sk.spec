Summary:	Slovak dictionary for aspell
Summary(pl.UTF-8):	Słownik słowacki dla aspella
Summary(sk.UTF-8):	Slovenské slovníky pre program ASpell
Name:		aspell-sk
Version:	2.01
%define	subv	2
Release:	1
Epoch:		1
License:	GPL v2 or LGPL v2.1 or MPL 1.1
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/sk/aspell6-sk-%{version}-%{subv}.tar.bz2
# Source0-md5:	b31bdc33a681902e5bc493a0692022a9
URL:		http://www.sk-spell.sk.cx/aspell-sk
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Slovak dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik słowacki (lista słów) dla aspella.

%description -l sk.UTF-8
Slovenské slovníky pre program ASpell.

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
%{_libdir}/aspell/sk.*
%{_libdir}/aspell/sk_SK.alias
%{_libdir}/aspell/slovak.alias
%{_libdir}/aspell/slovensky.alias
%{_datadir}/aspell/sk.dat
%{_datadir}/aspell/sk_affix.dat
