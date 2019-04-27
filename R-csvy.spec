#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-csvy
Version  : 0.3.0
Release  : 7
URL      : https://cran.r-project.org/src/contrib/csvy_0.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/csvy_0.3.0.tar.gz
Summary  : Import and Export CSV Data with a YAML Metadata Header
Group    : Development/Tools
License  : GPL-2.0
Requires: R-yaml
BuildRequires : R-data.table
BuildRequires : R-jsonlite
BuildRequires : R-rlang
BuildRequires : R-yaml
BuildRequires : buildreq-R

%description
# Import and Export CSV Data With a YAML Metadata Header
CSVY is a file format that combines the simplicity of CSV (comma-separated values) with the metadata of other plain text and binary formats (JSON, XML, Stata, etc.). The [CSVY file specification](http://csvy.org/) is simple: place a YAML header on top of a regular CSV. The yaml header is formatted according to the [Table Schema](https://frictionlessdata.io/specs/table-schema/) of a [Tabular Data Package](https://frictionlessdata.io/specs/tabular-data-package/).

%prep
%setup -q -c -n csvy

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552731645

%install
export SOURCE_DATE_EPOCH=1552731645
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library csvy
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library csvy
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library csvy
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  csvy || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/csvy/CITATION
/usr/lib64/R/library/csvy/DESCRIPTION
/usr/lib64/R/library/csvy/INDEX
/usr/lib64/R/library/csvy/Meta/Rd.rds
/usr/lib64/R/library/csvy/Meta/features.rds
/usr/lib64/R/library/csvy/Meta/hsearch.rds
/usr/lib64/R/library/csvy/Meta/links.rds
/usr/lib64/R/library/csvy/Meta/nsInfo.rds
/usr/lib64/R/library/csvy/Meta/package.rds
/usr/lib64/R/library/csvy/NAMESPACE
/usr/lib64/R/library/csvy/NEWS.md
/usr/lib64/R/library/csvy/R/csvy
/usr/lib64/R/library/csvy/R/csvy.rdb
/usr/lib64/R/library/csvy/R/csvy.rdx
/usr/lib64/R/library/csvy/examples/example1.csvy
/usr/lib64/R/library/csvy/examples/example2.csvy
/usr/lib64/R/library/csvy/help/AnIndex
/usr/lib64/R/library/csvy/help/aliases.rds
/usr/lib64/R/library/csvy/help/csvy.rdb
/usr/lib64/R/library/csvy/help/csvy.rdx
/usr/lib64/R/library/csvy/help/paths.rds
/usr/lib64/R/library/csvy/html/00Index.html
/usr/lib64/R/library/csvy/html/R.css
/usr/lib64/R/library/csvy/tests/test-all.R
/usr/lib64/R/library/csvy/tests/testthat/test-metadata.R
/usr/lib64/R/library/csvy/tests/testthat/test-read_csvy.R
/usr/lib64/R/library/csvy/tests/testthat/test-write_csvy.R
/usr/lib64/R/library/csvy/tests/testthat/test-write_metadata.R
