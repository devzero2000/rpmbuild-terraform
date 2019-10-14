# Don't try fancy stuff like debuginfo, which is useless on binary-only
# packages. Don't strip binary too
# Be sure buildpolicy set to do nothing
%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

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
%autosetup -c 

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
