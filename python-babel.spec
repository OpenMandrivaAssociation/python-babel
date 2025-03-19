%define tarname	babel

Summary:	Internationalization utilities for Python
Name:		python-babel
Version:	2.17.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/B/Babel/%{tarname}-%{version}.tar.gz
%define cldrversion 44.0
Source1:	http://unicode.org/Public/cldr/%(echo %{cldrversion}|cut -d. -f1)/cldr-common-%{cldrversion}.zip
License:	BSD
Group:		Development/Python
Url:		https://babel.edgewall.org/
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python-pkg-resources
BuildRequires:	python-pytz
Requires:       python-pytz

%description
Babel is a Python library that provides an integrated collection of
utilities that assist with internationalizing and localizing Python
applications (in particular web-based applications.)

%prep
%autosetup -p1 -n %{tarname}-%{version}
mkdir cldr
ln -s %{SOURCE1} cldr/cldr-common-%{cldrversion}.zip

%install
sed -i -e 's,getiterator,iter,g;s,\.getchildren(),,g' scripts/import_cldr.py
%{__python} setup.py import_cldr
%{__python} setup.py install --root=%{buildroot}

%files -n python-babel
%doc docs/
%{_bindir}/pybabel
%{python_sitelib}/babel/*
%{python_sitelib}/*.egg-info
