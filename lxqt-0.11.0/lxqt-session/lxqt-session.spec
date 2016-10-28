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

Name: lxqt-session
Version: %{vrs}
Release: %{rls}
Summary: Session manager for the LXQt desktop
URL: http://lxqt.org
License: LGPLv2+
Group: Graphical desktop/KDE

%if 0%{?scmrev:1}
Source0: https://github.com/lxde/%{name}/archive/master.zip#/%{name}-master.zip
%else
Source0: https://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
Source1: lxqt-config-session_fr.desktop
Source2: lxqt-hibernate_fr.desktop
Source3: lxqt-leave_fr.desktop
Source4: lxqt-logout_fr.desktop
Source5: lxqt-reboot_fr.desktop
Source6: lxqt-shutdown_fr.desktop
Source7: lxqt-suspend_fr.desktop

BuildRequires: cmake
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(Qt5Xdg) >= 2.0.0
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: xdg-user-dirs
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
cat %{SOURCE1} >> %{buildroot}/%{_datadir}/applications/lxqt-config-session.desktop
cat %{SOURCE2} >> %{buildroot}/%{_datadir}/applications/lxqt-hibernate.desktop
cat %{SOURCE3} >> %{buildroot}/%{_datadir}/applications/lxqt-leave.desktop
cat %{SOURCE4} >> %{buildroot}/%{_datadir}/applications/lxqt-logout.desktop
cat %{SOURCE5} >> %{buildroot}/%{_datadir}/applications/lxqt-reboot.desktop
cat %{SOURCE6} >> %{buildroot}/%{_datadir}/applications/lxqt-shutdown.desktop
cat %{SOURCE7} >> %{buildroot}/%{_datadir}/applications/lxqt-suspend.desktop
sed -i "/_FR/d" %{buildroot}/%{_datadir}/applications/lxqt-config-session.desktop
%endif

%files
%{_bindir}/lxqt-leave
%{_bindir}/lxqt-session
%{_bindir}/lxqt-config-session
%{_datadir}/applications/lxqt-leave.desktop
%{_datadir}/applications/lxqt-config-session.desktop
%{_datadir}/applications/lxqt-hibernate.desktop
%{_datadir}/applications/lxqt-lockscreen.desktop
%{_datadir}/applications/lxqt-logout.desktop
%{_datadir}/applications/lxqt-reboot.desktop
%{_datadir}/applications/lxqt-shutdown.desktop
%{_datadir}/applications/lxqt-suspend.desktop
%{_datadir}/lxqt/translations/lxqt-config-session
%{_datadir}/lxqt/translations/lxqt-leave
%{_datadir}/lxqt/translations/lxqt-session
%{_mandir}/man1/*


%changelog
* Thu Oct 27 2016 Paiiou <paiiou@free.fr> 0.11.0-11.paii6
- New package 0.11.0 Whith french translations of Oct 21 2016
- New specfile (Paiiou)

* Mon Mar 28 2016 doktor5000 <doktor5000> 0.10.0-5.mga6
+ Revision: 995919
+ rebuild (emptylog)

* Mon Feb 15 2016 umeabot <umeabot> 0.10.0-4.mga6
+ Revision: 961350
- Mageia 6 Mass Rebuild

* Tue Nov 10 2015 neoclust <neoclust> 0.10.0-3.mga6
+ Revision: 900955
- Rebuild against fixed qtbase5
- Use qt5 cmake macro
- New version 0.10.0
