%include	/usr/lib/rpm/macros.perl
%define	pdir	Pod
%define	pnam	POM
Summary:	Pod::POM perl module
Summary(pl):	Modu� perla Pod::POM
Name:		perl-Pod-POM
Version:	0.15
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	baa50e390cb1ae8b465c2eac05288f37
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
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
Ten modu� jest implementacj� parsera konwertuj�cego dokumenty Pod na
prost� posta� modelu obiektowego, znan� jako Pod Object Model. Model
obiektowy jest generowany jako hierarchiczne drzewo w�z��w, z kt�rych
ka�dy reprezentuje inny element oryginalnego dokumentu. Po drzewie
mo�na si� przemieszcza� r�cznie, sprawdzaj�c, wypisuj�c lub w inny
spos�b obrabiaj�c w�z�y. Opr�cz tego, Pod::POM obs�uguje obiekty
widoku, kt�re mog� automatycznie przemieszcza� si� po drzewie lub jego
cz�ci i generowa� na wyj�ciu reprezentacj� w jakiej� formie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Pod/POM.pm
%{perl_vendorlib}/Pod/POM
%{_mandir}/man[13]/*