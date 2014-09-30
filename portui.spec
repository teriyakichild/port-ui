%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define module_name portui

Name:           %{module_name}
Version:        0.1.0
Release:        1
Summary:        PortUI - UI for PORT.

License:        ASLv2
URL:            https://github.com/teriyakichild/portui
Source0:        %{module_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-setuptools

Requires: python-tornado

%description

%prep
%setup -q -n %{module_name}-%{version}


%build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT

%files
%doc README.md
%{python_sitelib}/*
%attr(0755,-,-) %{_bindir}/portui

%changelog
* Wed Sep 24 2014 Tony Rogers <tony.rogers@rackspace.com> - 0.1.1-1
- Updating name.
* Wed Sep 24 2014 Tony Rogers <tony.rogers@rackspace.com> - 0.1.0-1
- Initial spec
