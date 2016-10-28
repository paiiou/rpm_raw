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
%define ver 2.0.0
%define major 2
%define libname %mklibname qtxdg %{major}
%define devname %mklibname qtxdg -d

Name: libqtxdg
Version: %{vrs}
Release: %{rls}
Summary: Library providing freedesktop.org specs implementations for Qt
URL: https://github.com/lxde/libqtxdg
License: LGPLv2+
Group: System/Libraries

%if 0%{?scmrev:1}
Source0: https://github.com/lxde/%{name}/archive/master.zip#/%{name}-master.zip
%else
Source0: https://downloads.lxqt.org/%{name}/%{version}/%{name}-%{version}.tar.xz
%endif

BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5DBus)

%description
%{summary}.


%package -n %{libname}
Summary: Library providing freedesktop.org specs implementations for Qt
Group: System/Libraries
#-data subpackage does not exist anymore, contained only translations (dropped upstream)
Obsoletes: %{_lib}qtxdg-data < 1.0.0-7

%description -n %{libname}
Library providing freedesktop.org specs implementations for Qt

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %libname = %version
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release

%description -n %{devname}
Development files (Headers etc.) for %{name}, a library providing
freedesktop.org specs implementations for Qt.

%prep
%setup -q -n %{subdir}

%cmake_qt5


%build
%make_build -C build

%install
%make_install -C build


%files -n %{libname}
%{_libdir}/*.so.%{major}{,.*}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/qt5xdg
%{_datadir}/cmake/qt5xdgiconloader



%changelog
* Wed Oct 12 2016 Paiiou <paiiou@free.fr> 2.0.0-11.paii6
- New version 2.0.0

* Thu Apr 28 2016 Paiiou <paiiou@free.fr> 1.3.0-12.paii6
- Rebuild with git %{date}

* Mon Feb 15 2016 umeabot <umeabot> 1.3.0-2.mga6
+ Revision: 961179
- Mageia 6 Mass Rebuild

* Mon Nov 09 2015 neoclust <neoclust> 1.3.0-1.mga6
+ Revision: 900011
- New version 1.3.0
