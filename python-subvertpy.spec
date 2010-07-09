# TODO:
# - include examples in package
#
%define		module	subvertpy
#
Summary:	A Pythonic binding for subversion
Summary(pl.UTF-8):	Pythonowe wiązanie do subversion
Name:		python-%{module}
Version:	0.7.2
Release:	4
License:	LGPLv2.1+
Group:		Libraries/Python
Source0:	http://samba.org/~jelmer/subvertpy/%{module}-%{version}.tar.gz
# Source0-md5:	01e2098db04ddddaf06a7e27c075745d
Patch0:		apu_includes.patch
URL:		http://samba.org/~jelmer/subvertpy/
BuildRequires:	apr-devel
BuildRequires:	apr-util-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	subversion-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for the Subversion version control system that are
aimed to be complete, fast and feel native to Python programmers.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_bindir}/subvertpy-fast-export
%dir %{py_sitedir}/subvertpy
%{py_sitedir}/subvertpy/*.py[co]
%attr(755,root,root) %{py_sitedir}/subvertpy/*.so
%{py_sitedir}/subvertpy-*.egg-info
