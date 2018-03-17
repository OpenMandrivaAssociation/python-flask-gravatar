# Created by pyp2rpm-2.0.0
%global pypi_name Flask-Gravatar
%global with_python2 1
%define version 0.5.0

Name:           python3-flask-gravatar
Version:        %{version}
Release:        1
Group:          Development/Python
Summary:        Small extension for Flask to make usage of Gravatar service easy.

License:        BSD
URL:            https://github.com/zzzsochi/Flask-Gravatar
Source0:        https://pypi.python.org/packages/cd/9a/d7b1d570f98725d340034ea7df62ef20a48d9f5322b89f3accae88d58466/Flask-Gravatar-0.5.0.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest-runner >= 2.6.2
BuildRequires:  python3-check-manifest >= 0.25
BuildRequires:  python3-coverage >= 4.0
BuildRequires:  python3-isort >= 4.2.2
BuildRequires:  python3-pydocstyle >= 1.0.0
BuildRequires:  python3-pytest-cache >= 1.0
BuildRequires:  python3-pytest-cov >= 1.8.0
BuildRequires:  python3-pytest-pep8 >= 1.0.6
BuildRequires:  python3-pytest >= 2.8.0
BuildRequires:  python3-sphinx
 
%if %{?with_python2}
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pytest-runner >= 2.6.2
BuildRequires:  python-check-manifest >= 0.25
BuildRequires:  python-coverage >= 4.0
BuildRequires:  python-isort >= 4.2.2
BuildRequires:  python-pydocstyle >= 1.0.0
BuildRequires:  python-pytest-cache >= 1.0
BuildRequires:  python-pytest-cov >= 1.8.0
BuildRequires:  python-pytest-pep8 >= 1.0.6
BuildRequires:  python-pytest >= 2.8.0
BuildRequires:  python-sphinx
%endif # if with_python2
 
Requires:       python3-flask >= 0.10

%description
TODO:

%if 0%{?with_python2}
%package -n     python-%{pypi_name}
Summary:        Small extension for Flask to make usage of Gravatar service easy.
 
Requires:       python-flask >= 0.10

%description -n python-%{pypi_name}
This is small and simple integration gravatar into flask.
%endif # with_python2


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# generate html docs 
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%if 0%{?with_python2}
rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'
# generate html docs 
python2-sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%endif # with_python2


%build
%{__python3} setup.py build

%if 0%{?with_python2}
pushd %{py2dir}
%{__python} setup.py build
popd
%endif # with_python2


%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if 0%{?with_python2}
pushd %{py2dir}
%{__python} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python2

%{__python3} setup.py install --skip-build --root %{buildroot}


%files
%doc html README.rst docs/_themes/LICENSE LICENSE
%{python3_sitelib}/Flask_Gravatar
%{python3_sitelib}/Flask_Gravatar-%{version}-py?.?.egg-info
%if 0%{?with_python2}
%files -n python-%{pypi_name}
%doc html README.rst docs/_themes/LICENSE LICENSE
%{python_sitelib}/Flask_Gravatar
%{python_sitelib}/Flask_Gravatar-%{version}-py?.?.egg-info
%endif # with_python2

