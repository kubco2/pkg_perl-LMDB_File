Name:           perl-LMDB_File
Version:        0.12
Release:        1%{?dist}
Summary:        Perl5 wrapper around the OpenLDAP's LMDB
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/~sortiz/LMDB_File-0.12/
Source0:        http://search.cpan.org/CPAN/authors/id/S/SO/SORTIZ/LMDB_File-0.12.tar.gz

# Right now LMDB needs a 64bits platform.
ExclusiveArch:  x86_64 ppc64le aarch64 ppc64

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  libdb-devel
BuildRequires:  lmdb-devel >= 0.9.17
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 5.16
# Tests:
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Devel::Peek)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Fcntl)
Requires:       perl(XSLoader)

%{?perl_default_filter}

%description
LMDB_File is a Perl wrapper around the OpenLDAP's LMDB (Lightning
Memory-Mapped Database) C library.
LMDB is an ultra-fast, ultra-compact key-value data store developed
by Symas for the OpenLDAP Project. See http://symas.com/mdb/ for details.
LMDB_File provides full access to the complete C API, a thin Perl wrapper
with an Object-Oriented interface and a simple Perl's tie interface
compatible with others DBMs.


%prep
%setup -q -n LMDB_File-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%doc Changes README
%license LICENSE
%exclude %{perl_archlib}/perllocal.pod
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/LMDB_File*
%{_mandir}/man3/*


%changelog
* Tue Oct 24 2017 Jakub Janco <jjanco@redhat.com> 0.12-1
- initial package release
