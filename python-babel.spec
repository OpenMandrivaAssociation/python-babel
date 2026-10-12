%define tarname	babel

Summary:	Internationalization utilities for Python
Name:		python-babel
Version:	2.18.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/B/Babel/%{tarname}-%{version}.tar.gz
License:	BSD-3-Clause
Group:		Development/Python
Url:		https://babel.pocoo.org/
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
Babel is a Python library that provides an integrated collection of
utilities that assist with internationalizing and localizing Python
applications (in particular web-based applications.)

%prep -a
# The sdist already contains the imported CLDR data.
rm -rf babel.egg-info

%files
%doc README.rst CHANGES.rst docs/
%license LICENSE
%{_bindir}/pybabel
%{python_sitelib}/babel
%{python_sitelib}/babel-%{version}.dist-info
