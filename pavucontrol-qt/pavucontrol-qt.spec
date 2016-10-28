# With the GitHub master.zip source, use the following command:
# rpmbuild -ba -D "scmrev 1" file.spec
# if scmrev is defined, 0%{?scmrev:1} = 01 else if not, 0%{?scmrev:1} = 0

%if 0%{?scmrev:1}
%define date 20161108
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
%define ver 0.1.0

Name: pavucontrol-qt
Version: %{vrs}
Release: %{rls}
Summary: pavucontrol-qt is the Qt port of volume control pavucontrol
URL: http://lxqt.org
License: GPL-2.0
Group: Sound/Utilities

%if 0%{?scmrev:1}
Source0: https://github.com/lxde/%{name}/archive/master.zip#/%{name}-master.zip
%else
Source0: https://downloads.lxqt.org/%{name}/%{ver}/%{name}-%{ver}.tar.xz
%endif
Source1: pavucontrol-qt_fr.desktop

BuildRequires: cmake
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(Qt5Xdg) >= 2.0.0
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: config(xdg-user-dirs)
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: libapr
BuildRequires: libapr-util
BuildRequires: git

%description
pavucontrol-qt is the Qt port of volume control [pavucontrol](https://freedesktop.org/software/pulseaudio/pavucontrol/)
of sound server [PulseAudio](https://www.freedesktop.org/wiki/Software/PulseAudio/).
As such it can be used to adjust all controls provided by PulseAudio as well as some additional settings.
The software belongs to the LXQt project but its usage isn't limited to this desktop environment.

%prep
%setup -q -n %{subdir}
%cmake_qt5

%build
%make_build -C build

%install
%make_install -C build

# Add french desktop Entry
%if 0%{!?scmrev:1}
cat %{SOURCE1} >> %{buildroot}/%{_datadir}/applications/%{name}.desktop
%endif

%files
%{_bindir}/*
%{_datadir}/%{name}/translations/*
%{_datadir}/applications/*

%changelog
* Tue Nov 8 2016 Paiiou <paiiou@free.fr> 0.7.0-11.paii6
- New package and specfile (Paiiou)
