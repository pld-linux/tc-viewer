Summary:	Provides the ability to watch current transfers that take place in HTB and HFSC
Summary(pl.UTF-8):	Pozwala śledzić bieżący ruch w klasach HTB, HFSC.
Name:		tc-viewer
Version:	1.5
Release:	0.1
License:	GPL
Group:		Networking
Source0:	http://snaj.ath.cx/%{name}/tc-viewer
# Source0-md5:	e56f6a686e110aba273a94b62dd6f36d
Source1:	http://snaj.ath.cx/tc-viewer/%{name}.conf
# Source1-md5:	8c57ec7df34b953ade2202b0a092496e
Source2:	http://snaj.ath.cx/tc-viewer/Changelog
# Source2-md5:	89813ba4e157c2ab287ebafdd7ab74b4
URL:		http://snaj.ath.cx/tc-viewer/tc-viewer.html
Requires:	perl-base
BuildArch:      noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tc-viewer provides the ability to watch current transfers that take
place in HTB and HFSC traffic shaping classes on specified interface.

%description -l pl.UTF-8
tc-viewer pozwala śledzić bieżący transfer w HTB i HFSC dla każdej z
klas na określonym inferfejsie.

%prep
%setup -qcT
cp %{SOURCE1} tc-viewer.conf.example
cp %{SOURCE2} Changelog

%build
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog tc-viewer.conf.example
%attr(755,root,root) %{_bindir}/tc-viewer
