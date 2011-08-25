Name: librdmacm
Version: 1.0.10
Release: 2%{?dist}
Summary: Userspace RDMA Connection Manager
Group: System Environment/Libraries
License: GPLv2 or BSD
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/rdmacm/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch: s390 s390x
BuildRequires: libibverbs-devel >= 1.1

%description
librdmacm provides a userspace RDMA Communication Managment API.

%package devel
Summary: Development files for the librdmacm library
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release} libibverbs-devel%{?_isa}

%description devel
Development files for the librdmacm library.

%package static
Summary: Static development files for the librdmacm library
Group: System Environment/Libraries

%description static
Static libraries for the librdmacm library.

%package utils
Summary: Examples for the librdmacm library
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description utils
Example test programs for the librdmacm library.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/librdmacm*.so.*
%doc AUTHORS COPYING README

%files devel
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_includedir}/*
%{_mandir}/man3/*
%{_mandir}/man7/*

%files static
%defattr(-,root,root,-)
%{_libdir}/*.a

%files utils
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Jan 11 2010 Doug Ledford <dledford@redhat.com> - 1.0.10-2
- ExcludeArch s390(x) as the hardware doesn't exist there

* Thu Dec 03 2009 Doug Ledford <dledford@redhat.com> - 1.0.10-1
- Update to latest upstream release
- Change Requires on -devel package (bz533937)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Mar 29 2008 Roland Dreier <rolandd@cisco.com> - 1.0.7-1
- New upstream release

* Fri Feb 22 2008 Roland Dreier <rdreier@cisco.com> - 1.0.6-2
- Spec file cleanups from Fedora review: add BuildRequires for
  libibverbs, and move the static library to -static.

* Fri Feb 15 2008 Roland Dreier <rdreier@cisco.com> - 1.0.6-1
- Initial Fedora spec file
