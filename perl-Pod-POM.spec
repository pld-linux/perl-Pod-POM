%include	/usr/lib/rpm/macros.perl
%define	pdir	Pod
%define	pnam	POM
Summary:	Pod-POM perl module
Summary(pl):	Modu³ perla Pod-POM
Name:		perl-Pod-POM
Version:	0.13
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a parser to convert Pod documents into a simple
object model form known hereafter as the Pod Object Model.  The object
model is generated as a hierarchical tree of nodes, each of which
represents a different element of the original document.  The tree can
be walked manually and the nodes examined, printed or otherwise
manipulated.  In addition, Pod::POM supports and provides view objects
which can automatically traverse the tree, or section thereof, and
generate an output representation in one form or another.

%description -l pl
Ten modu³ jest implementacj± parsera konwertuj±cego dokumenty Pod na
prost± postaæ modelu obiektowego, znan± jako Pod Object Model. Model
obiektowy jest generowany jako hierarchiczne drzewo wêz³ów, z których
ka¿dy reprezentuje inny element oryginalnego dokumentu. Po drzewie
mo¿na siê przemieszczaæ rêcznie, sprawdzaj±c, wypisuj±c lub w inny
sposób obrabiaj±c wêz³y. Oprócz tego, Pod::POM obs³uguje obiekty
widoku, które mog± automatycznie przemieszczaæ siê po drzewie lub jego
czê¶ci i generowaæ na wyj¶ciu reprezentacjê w jakiej¶ formie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/Pod/POM.pm
%{perl_sitelib}/Pod/POM
%{_mandir}/man[13]/*
