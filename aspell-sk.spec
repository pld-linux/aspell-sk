Summary:	Slovak dictionary for aspell
Summary(pl):	S這wacki s這wnik dla aspella
Name:		aspell-sk
Version:	0.50
%define	subv	2
Release:	2
Epoch:		1
License:	GPL v2
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/sk/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	8f4db7bf8ffe8c49cd16621620a43240
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= 0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Slovak dictionary (i.e. word list) for aspell.

%description -l pl
S這wacki s這wnik (lista s堯w) dla aspella.

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

mv -v doc/README README.sk

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%lang(sk) %doc README.sk
%{_libdir}/aspell/*
%{_datadir}/aspell/*
