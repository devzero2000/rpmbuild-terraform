%define debug_package %{nil}

Name:           terraform
Version:        0.12.10
Release:        1%{?dist}
Summary:        Terraform provides a common configuration to launch cloud-based infrastructure.
Group:          Applications/System
License:        MPLv2.0
URL:            https://terraform.io/
Source0:	https://releases.hashicorp.com/%{name}/%{version}/%{name}_%{version}_linux_amd64.zip
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


%description
Terraform is a tool for building, changing, and combining infrastructure safely 
and efficiently.

%prep
%autosetup

%install
mkdir -p %{buildroot}/%{_bindir}
cp %{name}* %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/%{name}*

%doc

%changelog
* Mon Oct 14 2019 Elia Pinto <pinto.elia@gmail.com> - 0.12.10-1
- Initial RPM release (v0.12.10)
