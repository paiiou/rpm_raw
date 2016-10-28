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

Name: lxqt-admin
Version: %{vrs}
Release: %{rls}
Summary: Administration application for the LXQt desktop
URL: http://lxqt.org
License: LGPLv2+
Group: Graphical desktop/KDE

%if 0%{?scmrev:1}
Source0: https://github.com/lxde/%{name}/archive/master.zip#/%{name}-master.zip
%else
Source0: https://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
Source1: %{name}-time_fr.desktop
Source2: %{name}-user_fr.desktop

BuildRequires: cmake
BuildRequires: kwindowsystem-devel
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(Qt5Xdg) >= 2.0.0
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: libapr
BuildRequires: libapr-util
BuildRequires: git

%description
This repository is providing two GUI tools to adjust settings 
of the operating system LXQt is running on.

%prep
%setup -q -n %{subdir}
%cmake_qt5

%build
%make_build -C build

%install
%make_install -C build

# Add french desktop Entry
%if 0%{!?scmrev:1}
cat %{SOURCE1} >> %{buildroot}/%{_datadir}/applications/%{name}-time.desktop
cat %{SOURCE2} >> %{buildroot}/%{_datadir}/applications/%{name}-user.desktop
%endif


%files
%{_bindir}/lxqt-admin-time
%{_bindir}/lxqt-admin-user
%{_bindir}/lxqt-admin-user-helper
%{_datadir}/applications/*.desktop
%{_datadir}/polkit-1/actions/org.lxqt.lxqt-admin-user.policy
%{_datadir}/lxqt/translations/lxqt-admin-time
%{_datadir}/lxqt/translations/lxqt-admin-user


%changelog
* Wed Oct 26 2016 Paiiou <paiiou@free.fr> 0.11.0-11.paii6
- New package 0.11.0 Whith french translations of Oct 18 2016
- New specfile (Paiiou)
