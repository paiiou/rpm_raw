# With the GitHub master.zip source, use the following command:
# rpmbuild -ba -D "scmrev 1" file.spec
# if scmrev is defined, 0%{?scmrev:1} = 01 else if not, 0%{?scmrev:1} = 0

%if 0%{?scmrev:1}
%define date 20161027
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

Name: lxqt-qtplugin
Version: %{vrs}
Release: %{rls}
Summary: Qt plugin for the LXQt desktop
URL: http://lxqt.org
License: LGPLv2+
Group: Graphical desktop/KDE

%if 0%{?scmrev:1}
Source0: https://github.com/lxde/%{name}/archive/master.zip#/%{name}-master.zip
%else
Source0: https://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif

BuildRequires: cmake
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(Qt5Xdg) >= 2.0.0
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: libdbusmenu-qt5-devel
BuildRequires: libapr
BuildRequires: libapr-util
BuildRequires: git

%description
%{summary}.

%prep
%setup -q -n %{subdir}
%cmake_qt5

%build
%make_build -C build

%install
%make_install -C build


%files
%_qt5_plugindir/platformthemes/*



%changelog
* Thu Oct 27 2016 Paiiou <paiiou@free.fr> 0.11.0-11.paii6
- New package 0.11.0
- New specfile (Paiiou)

* Mon Mar 28 2016 doktor5000 <doktor5000> 0.10.0-4.mga6
+ Revision: 995921
+ rebuild (emptylog)

* Mon Feb 15 2016 umeabot <umeabot> 0.10.0-3.mga6
+ Revision: 961343
- Mageia 6 Mass Rebuild

* Tue Nov 10 2015 neoclust <neoclust> 0.10.0-2.mga6
+ Revision: 900885
- Rebuild against fixed qtbase5

* Mon Nov 09 2015 neoclust <neoclust> 0.10.0-1.mga6
+ Revision: 900213
- New version 0.10.0
