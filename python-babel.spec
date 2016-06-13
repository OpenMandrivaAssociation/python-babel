%define tarname	babel

Summary:	Internationalization utilities for Python
Name:		python-babel
Version:	2.3.4
Release:	2
Source0:	https://github.com/python-babel/babel/archive/%{version}.tar.gz
Source1:	http://unicode.org/Public/cldr/28/core.zip
License:	BSD
Group:		Development/Python
Url:		http://babel.edgewall.org/
BuildArch:	noarch
BuildRequires:	python-distribute
BuildRequires:	python2-distribute
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools
BuildRequires:	python2-devel
BuildRequires:	python-pytz
BuildRequires:	python2-pytz

%description
Babel is a Python library that provides an integrated collection of
utilities that assist with internationalizing and localizing Python
applications (in particular web-based applications.)

%package -n python2-babel
Summary:        Python package implementing YAML parser and emitter
Group:          Development/Python
Requires:       python3
 
%description -n python2-babel
Babel is a Python library that provides an integrated collection of
utilities that assist with internationalizing and localizing Python
applications (in particular web-based applications.)

%prep
%setup -q -c

mv %{tarname}-%{version} python2
ln -s %{SOURCE1} python2/cldr/core-28.zip
cp -r python2 python3

%install
pushd python2
%{__python2} setup.py import_cldr
%{__python2} setup.py install --root=%{buildroot}
popd

pushd python3
%{__python} setup.py import_cldr
%{__python} setup.py install --root=%{buildroot}
popd

%files -n python2-babel
%{_bindir}/pybabel
%doc python2/docs/
%{python2_sitelib}/babel/*
%{python2_sitelib}/*.egg-info

%files -n python-babel
%doc python3/docs/
%{python_sitelib}/babel/*
%{python_sitelib}/*.egg-info
