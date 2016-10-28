# With the GitHub master.zip source, use the following command:
# rpmbuild -ba -D "scmrev 1" file.spec
# if scmrev is defined, 0%{?scmrev:1} = 01 else if not, 0%{?scmrev:1} = 0

%if 0%{?scmrev:1}
%define date 20161026
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

Name: lxqt-config
Version: %{vrs}
Release: %{rls}
Summary: Config panel for the LXQt desktop
URL: http://lxqt.org
License: LGPLv2+
Group: Graphical desktop/KDE

%if 0%{?scmrev:1}
Source0: https://github.com/lxde/%{name}/archive/master.zip#/%{name}-master.zip
%else
Source0: https://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
Source1: %{name}-appearance_fr.desktop
Source2: %{name}-brightness_fr.desktop
Source3: %{name}-file-associations_fr.desktop
Source4: %{name}-input_fr.desktop
Source5: %{name}-locale_fr.desktop
Source6: %{name}-monitor_fr.desktop
Source7: %{name}_fr.desktop

BuildRequires: cmake
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(kscreen2)
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(Qt5Xdg) >= 2.0.0
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Help)
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

# Add french desktop Entry
%if 0%{!?scmrev:1}
cat %{SOURCE1} >> %{buildroot}/%{_datadir}/applications/%{name}-appearance.desktop
cat %{SOURCE2} >> %{buildroot}/%{_datadir}/applications/%{name}-brightness.desktop
cat %{SOURCE3} >> %{buildroot}/%{_datadir}/applications/%{name}-file-associations.desktop
cat %{SOURCE4} >> %{buildroot}/%{_datadir}/applications/%{name}-input.desktop
cat %{SOURCE5} >> %{buildroot}/%{_datadir}/applications/%{name}-locale.desktop
cat %{SOURCE6} >> %{buildroot}/%{_datadir}/applications/%{name}-monitor.desktop
cat %{SOURCE7} >> %{buildroot}/%{_datadir}/applications/%{name}.desktop
%endif
# Délete fr_FR lines
sed -i "/_FR/d" %{buildroot}/%{_datadir}/applications/%{name}-appearance.desktop
sed -i "/_FR/d" %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%{_sysconfdir}/xdg/menus/lxqt-config.menu
%{_bindir}
%{_libdir}/lxqt-config/lib*.so
%{_datadir}/applications/lxqt-config*.desktop
%{_datadir}/icons
%{_datadir}/lxqt


%changelog
* Wed Oct 26 2016 Paiiou <paiiou@free.fr> 0.11.0-11.paii6
- New package 0.11.0 Whith french translations of Oct 18 2016
- New specfile (Paiiou)

* Mon Mar 07 2016 daviddavid <daviddavid> 0.10.0-6.mga6
+ Revision: 986933
- rebuild for new libkscreen
- run cmake_qt5 into build section

  + umeabot <umeabot>
    - Mageia 6 Mass Rebuild

* Tue Dec 08 2015 doktor5000 <doktor5000> 0.10.0-5.mga6
+ Revision: 908884
- add comment on why rpath is used for the private library
- added upstream patch for library folder paths - fixes (mga#17203)

* Fri Nov 27 2015 neoclust <neoclust> 0.10.0-4.mga6
+ Revision: 906374
- Try to disable RPATH

* Thu Nov 26 2015 neoclust <neoclust> 0.10.0-3.mga6
+ Revision: 906335
- Fix start of lxqt-config-appearance MGA#17203

* Tue Nov 10 2015 neoclust <neoclust> 0.10.0-2.mga6
+ Revision: 900883
- Rebuild against fixed qtbase5

* Mon Nov 09 2015 neoclust <neoclust> 0.10.0-1.mga6
+ Revision: 900244
- New version 0.10.0
