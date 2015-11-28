# TODO:
# - package tests
#
%define		module	subvertpy
#
Summary:	A Pythonic binding for subversion
Summary(pl.UTF-8):	Pythonowe wiązanie do subversion
Name:		python-%{module}
Version:	0.8.10
Release:	1
License:	LGPLv2.1+
Group:		Libraries/Python
Source0:	http://samba.org/~jelmer/subvertpy/%{module}-%{version}.tar.gz
# Source0-md5:	e8a762128ff5f656fd5488e3d14a8516
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

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

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
