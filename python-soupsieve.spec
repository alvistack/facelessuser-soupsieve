%global debug_package %{nil}

Name: python-soupsieve
Epoch: 100
Version: 2.3.2.post1
Release: 1%{?dist}
BuildArch: noarch
Summary: Modern CSS selector implementation for BeautifulSoup
License: MIT
URL: https://github.com/pallets/soupsieve/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Soup Sieve is a CSS selector library designed to be used with Beautiful
Soup 4. It aims to provide selecting, matching, and filtering using
modern CSS selectors. Soup Sieve currently provides selectors from the
CSS level 1 specifications up through the latest CSS level 4 drafts and
beyond (though some are not yet implemented).

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-soupsieve
Summary: Modern CSS selector implementation for BeautifulSoup
Requires: python3
Provides: python3-soupsieve = %{epoch}:%{version}-%{release}
Provides: python3dist(soupsieve) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-soupsieve = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(soupsieve) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-soupsieve = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(soupsieve) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-soupsieve
Soup Sieve is a CSS selector library designed to be used with Beautiful
Soup 4. It aims to provide selecting, matching, and filtering using
modern CSS selectors. Soup Sieve currently provides selectors from the
CSS level 1 specifications up through the latest CSS level 4 drafts and
beyond (though some are not yet implemented).

%files -n python%{python3_version_nodots}-soupsieve
%license LICENSE.md
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-soupsieve
Summary: Modern CSS selector implementation for BeautifulSoup
Requires: python3
Provides: python3-soupsieve = %{epoch}:%{version}-%{release}
Provides: python3dist(soupsieve) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-soupsieve = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(soupsieve) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-soupsieve = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(soupsieve) = %{epoch}:%{version}-%{release}

%description -n python3-soupsieve
Soup Sieve is a CSS selector library designed to be used with Beautiful
Soup 4. It aims to provide selecting, matching, and filtering using
modern CSS selectors. Soup Sieve currently provides selectors from the
CSS level 1 specifications up through the latest CSS level 4 drafts and
beyond (though some are not yet implemented).

%files -n python3-soupsieve
%license LICENSE.md
%{python3_sitelib}/*
%endif

%changelog
