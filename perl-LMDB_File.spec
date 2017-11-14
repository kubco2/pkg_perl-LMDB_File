Name:           perl-LMDB_File
Version:        0.12
Release:        1%{?dist}
Summary:        Perl5 wrapper around the OpenLDAP's LMDB
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/~sortiz/LMDB_File/
Source0:        http://search.cpan.org/CPAN/authors/id/S/SO/SORTIZ/LMDB_File-0.12.tar.gz

# Right now LMDB needs a 64bits platform and tests fail on ppc64[le].
ExcludeArch:    armv7hl i686 ppc64 ppc64le s390x

BuildRequires:  libdb-devel
BuildRequires:  lmdb-devel >= 0.9.17
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Makefile:
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
# Tests:
BuildRequires:  perl(B)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(utf8)

Requires:       libc.so.6
Requires:       liblmdb.so.0.0.0
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(AutoLoader)
Requires:       perl(Carp)
Requires:       perl(Exporter)
Requires:       perl(Fcntl)
Requires:       perl(Scalar::Util)
Requires:       perl(XSLoader)
Requires:       perl(strict)
Requires:       perl(warnings)
Requires:       rtld(GNU_HASH)
  
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
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
make %{?_smp_mflags}


%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%doc Changes README
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/LMDB_File*
%{_mandir}/man3/*


%changelog
* Tue Oct 24 2017 Jakub Janco <jjanco@redhat.com> 0.12-1
- initial package release
