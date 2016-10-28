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
%define ver 0.11.0
%define major 0
%define libname %mklibname lxqt %{major}
%define devname %mklibname lxqt -d

Name: liblxqt
Version: %{vrs}
Release: %{rls}
Summary: Libraries for the LXQt desktop
URL: http://lxqt.org
License: LGPLv2+
Group: System/Libraries

%if 0%{?scmrev:1}
Source0: https://github.com/lxde/%{name}/archive/master.zip#/%{name}-master.zip
%else
Source0: https://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif

BuildRequires: cmake
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: kwindowsystem-devel
BuildRequires: pkgconfig(Qt5Xdg) >= 2.0.0
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: libxscrnsaver-devel
BuildRequires: libapr
BuildRequires: libapr-util
BuildRequires: git

%description
Libraries for the LXQt desktop

%package -n %{libname}
Summary: Libraries for the LXQt desktop
Group: System/Libraries

%description -n %{libname}
Libraries for the LXQt desktop

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %libname = %version
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release
Obsoletes: %{_lib}razorqt-devel < 0.5.3-1

%description -n %{devname}
Development files (Headers etc.) for %{name}.


%prep
%setup -q -n %{subdir}

%cmake_qt5


%build
%make_build -C build

%install
%make_install -C build


%files
%{_datadir}/lxqt

%files -n %{libname}
%{_libdir}/*.so.%{major}{,.*}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/lxqt


%changelog
* Sun Oct 23 2016 Paiiou <paiiou@free.fr> 0.11.0-11.paii6
- New version 0.11.0 Whith french translations of Oct 21 2016
- New specfile (Paiiou)

* Mon Mar 21 2016 doktor5000 <doktor5000> 0.10.0-5.mga6
+ Revision: 993516
- fix breakage when handling .desktop files with grep > 2.23 (mga#17981)
- update translations during build if necessary

* Mon Feb 15 2016 umeabot <umeabot> 0.10.0-4.mga6
+ Revision: 961075
- Mageia 6 Mass Rebuild

* Tue Nov 10 2015 neoclust <neoclust> 0.10.0-3.mga6
+ Revision: 900903
- Rebuild against fixed qtbase5

* Mon Nov 09 2015 neoclust <neoclust> 0.10.0-2.mga6
+ Revision: 900064
- Fix LXQT_ETC_XDG_DIR

* Mon Nov 09 2015 neoclust <neoclust> 0.10.0-1.mga6
+ Revision: 900010
- New version 0.10.0
