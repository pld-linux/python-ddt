#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Data-Driven Tests - library to multiply test cases
Summary(pl.UTF-8):	Data-Driven Tests - biblioteka do zwielokrotniania przypadków testowych
Name:		python-ddt
Version:	1.2.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ddt/
Source0:	https://files.pythonhosted.org/packages/source/d/ddt/ddt-%{version}.tar.gz
# Source0-md5:	1270d706454088ea108f23fbaa800e56
Patch0:		%{name}-mock.patch
URL:		https://github.com/txels/ddt
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-mock
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DDT (Data-Driven Tests) allows you to multiply one test case by
running it with different test data, and make it appear as multiple
test cases.

%description -l pl.UTF-8
Biblioteka DDT (Data-Driven Tests - testy sterowane danymi) pozwala na
zwielotnianie pojedynczego przypadku testowego poprzez uruchamianie go
z różnymi danymi testowymi i traktowanie go jako wielu przypadków
testowych.

%package -n python3-ddt
Summary:	Data-Driven Tests - library to multiply test cases
Summary(pl.UTF-8):	Data-Driven Tests - biblioteka do zwielokrotniania przypadków testowych
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-ddt
DDT (Data-Driven Tests) allows you to multiply one test case by
running it with different test data, and make it appear as multiple
test cases.

%description -n python3-ddt -l pl.UTF-8
Biblioteka DDT (Data-Driven Tests - testy sterowane danymi) pozwala na
zwielotnianie pojedynczego przypadku testowego poprzez uruchamianie go
z różnymi danymi testowymi i traktowanie go jako wielu przypadków
testowych.

%prep
%setup -q -n ddt-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%{py_sitescriptdir}/ddt.py[co]
%{py_sitescriptdir}/ddt-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-ddt
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%{py3_sitescriptdir}/ddt.py
%{py3_sitescriptdir}/__pycache__/ddt.cpython-*.py[co]
%{py3_sitescriptdir}/ddt-%{version}-py*.egg-info
%endif
