#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	GraphViz
%define	pnam	DBI
Summary:	GraphViz::DBI Perl module - graph database tables and relations
Summary(pl):	Modu³ Perla GraphViz::DBI - tworzenie graf tabel i relacji dla bazy danych
Name:		perl-GraphViz-DBI
Version:	0.02
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9921cf28e6db58c0b4b9728bdf2866d7
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-GraphViz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module constructs a graph for a database showing tables and
connecting them if they are related. While or after constructing the
object, pass an open database handle, then call `graph_tables' to
determine database metadata and construct a GraphViz graph from the
table and field information.

%description -l pl
Ten modu³ konstruuje graf dla bazy danych pokazuj±c tabele i ³±cz±c
je je¶li s± miêdzy nimi relacje. Wystarczy w czasie lub po tworzeniu
obiektu przekazaæ uchwyt otwartej bazy i wywo³aæ graph_tables, aby
okre¶liæ metadane bazy i skonstruowaæ GraphVizowy graf z informacji o
tabelach i polach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/GraphViz/DBI.pm
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
