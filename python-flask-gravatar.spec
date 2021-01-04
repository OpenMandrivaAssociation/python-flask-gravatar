# Created by pyp2rpm-3.3.5
%global pypi_name Flask-Gravatar

Name:           python-%{pypi_name}
Version:        0.5.0
Release:        1
Summary:        Small extension for Flask to make usage of Gravatar service easy
Group:          Development/Python
License:        BSD
URL:            https://github.com/zzzsochi/Flask-Gravatar/
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python-check-manifest >= 0.25
BuildRequires:  python-coverage >= 4
BuildRequires:  python-flask >= 0.10
BuildRequires:  python-isort >= 4.2.2
BuildRequires:  python-pydocstyle >= 1
BuildRequires:  python-pytest >= 2.8
BuildRequires:  python-pytest-cache >= 1
BuildRequires:  python-pytest-cov >= 1.8
BuildRequires:  python-pytest-pep8 >= 1.0.6
BuildRequires:  python-pytest-runner >= 2.6.2
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx >= 1.4.2

%description
 Flask Gravatar .. image::
%package -n python-%{pypi_name}-doc
Summary:        Flask-Gravatar documentation
%description -n python-%{pypi_name}-doc
Documentation for Flask-Gravatar

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

#%%check
#%{__python3} setup.py test

%files -n python-%{pypi_name}
%license docs/_themes/LICENSE LICENSE
%doc README.rst
%{python3_sitelib}/flask_gravatar
%{python3_sitelib}/Flask_Gravatar-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license docs/_themes/LICENSE LICENSE
