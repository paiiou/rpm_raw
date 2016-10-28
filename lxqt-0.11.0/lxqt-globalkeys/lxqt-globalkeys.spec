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
%define libname %mklibname lxqt-globalkeys 0
%define uiname %mklibname lxqt-globalkeys-ui 0
%define devname %mklibname -d lxqt-globalkeys
%define uidevname %mklibname -d lxqt-globalkeys-ui

Name: lxqt-globalkeys
Version: %{vrs}
Release: %{rls}
Summary: Global keys config module for LXQt
URL: http://lxqt.org
License: LGPLv2+
Group: Graphical desktop/KDE

%if 0%{?scmrev:1}
Source0: https://github.com/lxde/%{name}/archive/master.zip#/%{name}-master.zip
%else
Source0: https://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
Source1: lxqt-config-globalkeyshortcuts_fr.desktop

BuildRequires: cmake
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(Qt5Xdg) >= 2.0.0
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: libapr
BuildRequires: libapr-util
BuildRequires: git

%description
%{summary}.

%package -n %{libname}
Summary: The LXQt globalkeys library
Group: System/Libraries

%description -n %{libname}
The LXQt globalkeys library

%package -n %{uiname}
Summary: The LXQt globalkeys UI library
Group: System/Libraries

%description -n %{uiname}
The LXQt globalkeys UI library

%package -n %{devname}
Summary: Development files for the LXQt globalkeys library
Group: Development/C
Requires: %libname = %version
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release
Obsoletes: %{_lib}razorglobalkeyshortcuts-devel < 0.5.3-1

%description -n %{devname}
Development files for the LXQt globalkeys library

%package -n %{uidevname}
Summary: Development files for the LXQt globalkeys UI library
Group: Development/C
Requires: %libname = %version
Requires: %uiname = %version
Provides: %uiname-devel = %version-%release
Provides: lib%name-devel = %version-%release

%description -n %{uidevname}
Development files for the LXQt globalkeys UI library

%prep
%setup -q -n %{subdir}
%cmake_qt5

%build
%make_build -C build

%install
%make_install -C build

# Add french desktop Entry
%if 0%{!?scmrev:1}
cat %{SOURCE1} >> %{buildroot}/%{_datadir}/applications/lxqt-config-globalkeyshortcuts.desktop
%endif

%files
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/lxqt/translations

%files -n %{libname}
%{_libdir}/liblxqt-globalkeys.so.0*

%files -n %{uiname}
%{_libdir}/liblxqt-globalkeys-ui.so.0*

%files -n %{devname}
%{_libdir}/liblxqt-globalkeys.so
%{_includedir}/lxqt-globalkeys
%{_libdir}/pkgconfig/lxqt-globalkeys.pc
%{_datadir}/cmake/lxqt-globalkeys

%files -n %{uidevname}
%{_libdir}/liblxqt-globalkeys-ui.so
%{_includedir}/lxqt-globalkeys-ui
%{_libdir}/pkgconfig/lxqt-globalkeys-ui.pc
%{_datadir}/cmake/lxqt-globalkeys-ui

%changelog
* Wed Oct 26 2016 Paiiou <paiiou@free.fr> 0.11.0-11.paii6
- New package 0.11.0
- New specfile (Paiiou)

* Mon Mar 28 2016 doktor5000 <doktor5000> 0.10.0-5.mga6
+ Revision: 995887
+ rebuild (emptylog)

* Mon Feb 15 2016 umeabot <umeabot> 0.10.0-4.mga6
+ Revision: 961310
- Mageia 6 Mass Rebuild

* Tue Nov 10 2015 neoclust <neoclust> 0.10.0-3.mga6
+ Revision: 900905
- Rebuild against fixed qtbase5
- Use qt5 cmake macro

* Mon Nov 09 2015 neoclust <neoclust> 0.10.0-1.mga6
+ Revision: 900137
- New version 0.10.0

* Sun Feb 22 2015 doktor5000 <doktor5000> 0.9.0-1.mga5
+ Revision: 816428
- new version 0.9.0
- drop lxqt-globalkeys-0.7.0-mga-desktopfile-el_GR.patch, merged upstream
- remove conditional handling for QT5 as QT4 is not supported anymore
- adjusted BuildRequires from pkgconfig(lxqt-qt5) to pkgconfig(lxqt)

* Wed Dec 17 2014 doktor5000 <doktor5000> 0.8.0-5.mga5
+ Revision: 803660
- rebuild for QT 5.4 breakage

* Sun Oct 26 2014 doktor5000 <doktor5000> 0.8.0-4.mga5
+ Revision: 793516
- do not remove LXQt Catgories from .desktop file

  + umeabot <umeabot>
    - Second Mageia 5 Mass Rebuild

* Tue Oct 14 2014 doktor5000 <doktor5000> 0.8.0-1.mga5
+ Revision: 738656
- add missing BuildRequires on pkgconfig(Qt5Widgets)
- add missing BuildRequires on pkgconfig(Qt5DBus)
- add missing BuildRequires on pkgconfig(Qt5Help)
- correct license
- new version 0.8.0
- enabled QT5 build

* Wed Sep 17 2014 wally <wally> 0.7.0-5.mga5
+ Revision: 693140
- obsolete librazorglobalkeyshortcuts-devel

  + umeabot <umeabot>
    - Mageia 5 Mass Rebuild

* Sat Sep 13 2014 wally <wally> 0.7.0-4.mga5
+ Revision: 675024
- obsolete razorqt-globalkeyshortcuts

* Fri May 23 2014 dglent <dglent> 0.7.0-3.mga5
+ Revision: 625111
- Add patch for el_GR desktop file

* Thu May 22 2014 doktor5000 <doktor5000> 0.7.0-2.mga5
+ Revision: 624962
- add Requires in lxqt-globalkeys-ui-devel on lxqt-globalkeys-ui lib

* Thu May 22 2014 doktor5000 <doktor5000> 0.7.0-1.mga5
+ Revision: 624929
- fix .desktop file
  o remove Category=LXQt for now
  o change Comment[el_GR] to not be redundant with Name[el_GR]
- remove useless Requires, use proper Requires/Provides
- use %%mkrel
- fix BuildRequires
- imported package lxqt-globalkeys

