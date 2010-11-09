%define tarname	Babel
%define name	python-babel
%define version 0.9.5
%define release %mkrel 1

Summary:	Internationalization utilities for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://ftp.edgewall.com/pub/babel/%{tarname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://babel.edgewall.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-setuptools

%description
Babel is a Python library that provides an integrated collection of
utilities that assist with internationalizing and localizing Python
applications (in particular web-based applications.)

%prep
%setup -q -n %{tarname}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
mv doc html

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc ChangeLog COPYING README.txt html/
