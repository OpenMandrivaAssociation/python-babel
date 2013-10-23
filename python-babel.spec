%define tarname	Babel

Summary:	Internationalization utilities for Python
Name:		python-babel
Version:	0.9.6
Release:	3
Source0:	http://ftp.edgewall.com/pub/babel/%{tarname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://babel.edgewall.org/
BuildArch:	noarch
BuildRequires:	python3-distribute
BuildRequires:	python-distribute
BuildRequires:	python3-devel

%description
Babel is a Python library that provides an integrated collection of
utilities that assist with internationalizing and localizing Python
applications (in particular web-based applications.)

%package -n python3-babel
Summary:        Python package implementing YAML parser and emitter
Group:          Development/Python
BuildRequires:  python-setuptools
Requires:       python3
 
%description -n python3-babel
Babel is a Python library that provides an integrated collection of
utilities that assist with internationalizing and localizing Python
applications (in particular web-based applications.)

%prep
%setup -q -c

mv %{tarname}-%{version} python2
cp -r python2 python3

%install
pushd python2
mv doc html
%{__python} setup.py install --root=%{buildroot}
popd

pushd python3
mv doc html
%{__python3} setup.py install --root=%{buildroot}
popd

%files -n python-babel 
%{_bindir}/pybabel
%doc python2/ChangeLog python2/COPYING python2/README.txt python2/html/
%{python_sitelib}/babel
%{python_sitelib}/*.egg-info

%files -n python3-babel
%doc python3/ChangeLog python3/COPYING python3/README.txt python3/html/
%{python3_sitelib}/babel
%{python3_sitelib}/*.egg-info
