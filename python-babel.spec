%define tarname	Babel

Summary:	Internationalization utilities for Python
Name:		python-babel
Version:	0.9.6
Release:	2
Source0:	http://ftp.edgewall.com/pub/babel/%{tarname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://babel.edgewall.org/
BuildArch:	noarch
BuildRequires:	python-setuptools

%description
Babel is a Python library that provides an integrated collection of
utilities that assist with internationalizing and localizing Python
applications (in particular web-based applications.)

%prep
%setup -q -n %{tarname}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
mv doc html
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%doc ChangeLog COPYING README.txt html/


%changelog
* Thu Apr 21 2011 Lev Givon <lev@mandriva.org> 0.9.6-1mdv2011.0
+ Revision: 656497
- Update to 0.9.6.

* Tue Nov 09 2010 Lev Givon <lev@mandriva.org> 0.9.5-1mdv2011.0
+ Revision: 595336
- import python-babel


