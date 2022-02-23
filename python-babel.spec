%define tarname	babel

Summary:	Internationalization utilities for Python
Name:		python-babel
Version:	2.9.1
Release:	2
Source0:	https://github.com/python-babel/babel/archive/%{tarname}-%{version}.tar.gz
%define cldrversion 37
Source1:	http://unicode.org/Public/cldr/%{cldrversion}/core.zip
License:	BSD
Group:		Development/Python
Url:		http://babel.edgewall.org/
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
ln -s %{SOURCE1} cldr/cldr-core-%{cldrversion}.zip

%install
sed -i -e 's,getiterator,iter,g;s,\.getchildren(),,g' scripts/import_cldr.py
%{__python} setup.py import_cldr
%{__python} setup.py install --root=%{buildroot}

%files -n python-babel
%doc docs/
%{_bindir}/pybabel
%{python_sitelib}/babel/*
%{python_sitelib}/*.egg-info
