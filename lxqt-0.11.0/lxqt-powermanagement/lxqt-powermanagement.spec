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

Name: lxqt-powermanagement
Version: %{vrs}
Release: %{rls}
Summary: Power management module for LXQt
URL: http://lxqt.org
License: LGPLv2+
Group: Graphical desktop/KDE

%if 0%{?scmrev:1}
Source0: https://github.com/lxde/%{name}/archive/master.zip#/%{name}-master.zip
%else
Source0: https://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
Source1: lxqt-config-powermanagement_fr.desktop

BuildRequires: cmake
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(Qt5Xdg) >= 2.0.0
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: solid-devel
BuildRequires: cmake(KF5IdleTime)
BuildRequires: libapr
BuildRequires: libapr-util
BuildRequires: git
#upower binary is required to prevent "power management disabled" popup on login
Requires: upower

%description
%{summary}.

%prep
%setup -q -n %{subdir}
%cmake_qt5

%build
%make_build -C build

%install
%make_install -C build

# Add french desktop Entry
%if 0%{!?scmrev:1}
cat %{SOURCE1} >> %{buildroot}/%{_datadir}/applications/lxqt-config-powermanagement.desktop
%endif

%files
%{_bindir}/lxqt-config-powermanagement
%{_bindir}/%{name}
%{_datadir}/applications/lxqt-config-powermanagement.desktop
%{_datadir}/icons/*/*/*/laptop-lid.svg
%{_datadir}/lxqt/translations/%{name}
%{_datadir}/lxqt/translations/lxqt-config-powermanagement



%changelog
* Thu Oct 27 2016 Paiiou <paiiou@free.fr> 0.11.0-11.paii6
- New package 0.11.0
- New specfile (Paiiou)

* Mon Mar 28 2016 doktor5000 <doktor5000> 0.10.0-5.mga6
+ Revision: 995930
+ rebuild (emptylog)

* Mon Feb 15 2016 umeabot <umeabot> 0.10.0-4.mga6
+ Revision: 961320
- Mageia 6 Mass Rebuild

* Tue Nov 10 2015 neoclust <neoclust> 0.10.0-3.mga6
+ Revision: 900888
- Rebuild against fixed qtbase5
- Use qt5 cmake macro

* Mon Nov 09 2015 neoclust <neoclust> 0.10.0-1.mga6
+ Revision: 900212
- New version 0.10.0
