#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Pod
%define		pnam	POM
Summary:	Pod::POM perl module
Summary(pl.UTF-8):	Moduł perla Pod::POM
Name:		perl-Pod-POM
Version:	0.25
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	02f62bc9115a4931aa316ba16d65d013
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl.UTF-8
Ten moduł jest implementacją parsera konwertującego dokumenty Pod na
prostą postać modelu obiektowego, znaną jako Pod Object Model. Model
obiektowy jest generowany jako hierarchiczne drzewo węzłów, z których
każdy reprezentuje inny element oryginalnego dokumentu. Po drzewie
można się przemieszczać ręcznie, sprawdzając, wypisując lub w inny
sposób obrabiając węzły. Oprócz tego, Pod::POM obsługuje obiekty
widoku, które mogą automatycznie przemieszczać się po drzewie lub jego
części i generować na wyjściu reprezentację w jakiejś formie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Pod/POM.pm
%{perl_vendorlib}/Pod/POM
%{_mandir}/man[13]/*
