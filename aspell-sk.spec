Summary:	Slovak dictionary for aspell
Summary(pl):	S這wnik s這wacki dla aspella
Name:		aspell-sk
Version:	0.52
%define	subv	0
Release:	2
Epoch:		1
License:	GPL v2
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/sk/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	ce90b109f7c602bde949880920bbbbfd
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.50.0
Requires:	aspell >= 3:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Slovak dictionary (i.e. word list) for aspell.

%description -l pl
S這wnik s這wacki (lista s堯w) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -v doc/README.sk README.sk

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%lang(sk) %doc README.sk
%{_libdir}/aspell/*
%{_datadir}/aspell/*
