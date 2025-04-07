%define module setupmeta
%bcond_without test

Name:		python-setupmeta
Version:	3.8.0
Release:	1
Summary:	Simplify your setup.py
Group:		Development/Python
License:	MIT
URL:		https://github.com/codrsquad/setupmeta
Source0:	https://files.pythonhosted.org/packages/source/s/setupmeta/%{module}-%{version}.tar.gz

BuildSystem:	python
BuildArch:		noarch

BuildRequires:	git-core
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pdm-backend)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with test}
BuildRequires:	python%{pyver}dist(mock)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(pdm-backend)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-mock)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
%endif


%description
Writing a setup.py typically involves lots of boilerplate and copy-pasting
from project to project.

This package aims to simplify that and bring some DRY principle to python
packaging.

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %%{module}.egg-info

%build
%py_build

%install
%py3_install

%if %{with test}
%check
# required for some tests
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
# test_check_dependencies: requires a virtualenv
# test_version and test_scenario require full git project with its versioning scheme, disabled
pytest -v tests/ -k "not test_check_dependencies and not test_version and not test_scenario"
%endif

%files
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-*.dist-info
%license LICENSE
%doc README.rst
