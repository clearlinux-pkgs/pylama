#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pylama
Version  : 7.7.1
Release  : 17
URL      : https://files.pythonhosted.org/packages/8a/89/082aa9378e382bd8132c3a8a3ef09af71e1c8f5c00cef211583e476ba4df/pylama-7.7.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/8a/89/082aa9378e382bd8132c3a8a3ef09af71e1c8f5c00cef211583e476ba4df/pylama-7.7.1.tar.gz
Summary  : pylama -- Code audit tool for python
Group    : Development/Tools
License  : LGPL-3.0
Requires: pylama-bin = %{version}-%{release}
Requires: pylama-license = %{version}-%{release}
Requires: pylama-python = %{version}-%{release}
Requires: pylama-python3 = %{version}-%{release}
Requires: mccabe
Requires: pycodestyle
Requires: pydocstyle
Requires: pyflakes
BuildRequires : buildreq-distutils3
BuildRequires : mccabe
BuildRequires : pycodestyle
BuildRequires : pydocstyle
BuildRequires : pyflakes

%description
#############

%package bin
Summary: bin components for the pylama package.
Group: Binaries
Requires: pylama-license = %{version}-%{release}

%description bin
bin components for the pylama package.


%package license
Summary: license components for the pylama package.
Group: Default

%description license
license components for the pylama package.


%package python
Summary: python components for the pylama package.
Group: Default
Requires: pylama-python3 = %{version}-%{release}

%description python
python components for the pylama package.


%package python3
Summary: python3 components for the pylama package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pylama package.


%prep
%setup -q -n pylama-7.7.1
cd %{_builddir}/pylama-7.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574715625
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pylama
cp %{_builddir}/pylama-7.7.1/LICENSE %{buildroot}/usr/share/package-licenses/pylama/f45ee1c765646813b442ca58de72e20a64a7ddba
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3*/site-packages/tests/__pycache__/__init__.cpython-3*.pyc
rm -f %{buildroot}/usr/lib/python3*/site-packages/tests/__init__.py

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pylama

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pylama/f45ee1c765646813b442ca58de72e20a64a7ddba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
