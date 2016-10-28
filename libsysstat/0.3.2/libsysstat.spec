# With the GitHub master.zip source, use the following command:
# rpmbuild -ba -D "scmrev 1" file.spec
# if scmrev is defined, 0%{?scmrev:1} = 01 else if not, 0%{?scmrev:1} = 0

%if 0%{?scmrev:1}
%define date 20161008
%define rls %mkrel -c git%{date} %{rel}
%define vrs %{ver}.1
%define subdir %{name}-master
%else
%define rls %mkrel 1%{rel}
%define vrs %{ver}
%define subdir %{name}-%{ver}
%endif

# No debuginfo:
%define debug_package %{nil}

%define rel 1
%define ver 0.3.2
%define major 0
%define libname %mklibname sysstat %{major}
%define devname %mklibname sysstat -d

Name: libsysstat
Version: %{vrs}
Release: %{rls}
Summary: System status library for LXQt
URL: http://lxqt.org/
License: LGPLv2+
Group: System/Libraries

%if 0%{?scmrev:1}
Source0: https://github.com/lxde/%{name}/archive/master.zip#/%{name}-master.zip
%else
Source0: https://downloads.lxqt.org/%{name}/%{version}/%{name}-%{version}.tar.xz
%endif

BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)

%description
%{summary}.


%package -n %{libname}
Summary: System status library for LXQt
Group: System/Libraries
Obsoletes: %{_lib}razorsysstat0 < 0.5.4

%description -n %{libname}
System status library for LXQt

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %libname = %version
Provides: %name-devel = %version-%release
%if %mgaversion < 5
Provides: pkgconfig(sysstat-qt5)
%endif
Obsoletes: %{_lib}razorsysstat-devel < 0.5.4

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q -n %{subdir}

%cmake_qt5


%build
%make_build -C build

%install
%make_install -C build

mkdir -p %{buildroot}%{_libdir}/cmake
mv %{buildroot}%{_datadir}/cmake/sysstat-qt5 \
	%{buildroot}%{_libdir}/cmake/sysstat-qt5


%files -n %{libname}
%{_libdir}/*.so.%{major}{,.*}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/sysstat-qt5



%changelog
* Wed Oct 12 2016 Paiiou <paiiou@free.fr> 0.3.2-11.paii6
- New version 0.3.2

* Mon Mar 28 2016 doktor5000 <doktor5000> 0.3.1-4.mga6
+ Revision: 995912
+ rebuild (emptylog)

* Sun Dec 27 2015 wally <wally> 0.3.1-3.mga6
+ Revision: 915921
- rebuild with new cmake and cmake() provides

* Sun Dec 27 2015 wally <wally> 0.3.1-2.mga6
+ Revision: 915904
- add patch to fix version in cmake version config file

* Mon Nov 09 2015 neoclust <neoclust> 0.3.1-1.mga6
+ Revision: 900148
- New version 0.3.1
