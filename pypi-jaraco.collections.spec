#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jaraco.collections
Version  : 3.5.1
Release  : 24
URL      : https://files.pythonhosted.org/packages/f6/4b/b9b09f98a1626599598addc333d6c5066f97b55b0a065eeb711bd1c21f71/jaraco.collections-3.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/f6/4b/b9b09f98a1626599598addc333d6c5066f97b55b0a065eeb711bd1c21f71/jaraco.collections-3.5.1.tar.gz
Summary  : Collection objects similar to those in stdlib by jaraco
Group    : Development/Tools
License  : MIT
Requires: pypi-jaraco.collections-license = %{version}-%{release}
Requires: pypi-jaraco.collections-python = %{version}-%{release}
Requires: pypi-jaraco.collections-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jaraco.classes)
BuildRequires : pypi(jaraco.text)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
.. image:: https://img.shields.io/pypi/v/jaraco.collections.svg
:target: `PyPI link`_

%package license
Summary: license components for the pypi-jaraco.collections package.
Group: Default

%description license
license components for the pypi-jaraco.collections package.


%package python
Summary: python components for the pypi-jaraco.collections package.
Group: Default
Requires: pypi-jaraco.collections-python3 = %{version}-%{release}

%description python
python components for the pypi-jaraco.collections package.


%package python3
Summary: python3 components for the pypi-jaraco.collections package.
Group: Default
Requires: python3-core
Provides: pypi(jaraco.collections)
Requires: pypi(jaraco.classes)
Requires: pypi(jaraco.text)

%description python3
python3 components for the pypi-jaraco.collections package.


%prep
%setup -q -n jaraco.collections-3.5.1
cd %{_builddir}/jaraco.collections-3.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649767532
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jaraco.collections
cp %{_builddir}/jaraco.collections-3.5.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jaraco.collections/8e6689d37f82d5617b7f7f7232c94024d41066d1
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/jaraco/__init__.py
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/jaraco/__pycache__/__init__.*

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jaraco.collections/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
