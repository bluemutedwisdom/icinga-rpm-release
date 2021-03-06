Name:		icinga-rpm-release
Version:	7
Release:	2%{?dist}
Summary:	Icinga Package Repository

Group:		System Environment/Base
License:	GPLv2
URL:		http://packages.icinga.com/epel/
Source0:	%{name}-%{version}.tar.gz
Source1:	icinga.key
Source2:	ICINGA-release.repo
Source3:	ICINGA-snapshot.repo

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

Requires:	redhat-release >=  %{version}

%description
This package contains the Icinga package repository GPG key
as well as configuration for yum.

%prep
%setup -q -c -T
install -pm 644 %{SOURCE0} .

%build

%install
rm -rf $RPM_BUILD_ROOT

#GPG key
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ICINGA

#yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*


%changelog

