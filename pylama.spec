#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pylama
Version  : 7.6.4
Release  : 4
URL      : https://files.pythonhosted.org/packages/7a/aa/2d16865086c15498bc70dea1dfa415032c491938414e9b7f2a140062075c/pylama-7.6.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/7a/aa/2d16865086c15498bc70dea1dfa415032c491938414e9b7f2a140062075c/pylama-7.6.4.tar.gz
Summary  : pylama -- Code audit tool for python
Group    : Development/Tools
License  : LGPL-3.0
Requires: pylama-bin
Requires: pylama-python3
Requires: pylama-license
Requires: pylama-python
Requires: mccabe
Requires: pycodestyle
Requires: pydocstyle
Requires: pyflakes
BuildRequires : buildreq-distutils3

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
%setup -q -n pylama-7.6.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539123779
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pylama
cp LICENSE %{buildroot}/usr/share/doc/pylama/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pylama

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/pylama/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
