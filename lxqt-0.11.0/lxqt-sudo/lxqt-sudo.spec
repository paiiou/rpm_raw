# With the GitHub master.zip source, use the following command:
# rpmbuild -ba -D "scmrev 1" file.spec
# if scmrev is defined, 0%{?scmrev:1} = 01 else if not, 0%{?scmrev:1} = 0

%if 0%{?scmrev:1}
%define date 20161028
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

Name: lxqt-sudo
Version: %{vrs}
Release: %{rls}
Summary: LXQt sudo wrapper
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
%{_bindir}/*
%{_datadir}/lxqt/translations/*
%{_mandir}/man1/*

%changelog
* Fri Oct 28 2016 Paiiou <paiiou@free.fr> 0.11.0-11.paii6
- New package 0.11.0
- New specfile (Paiiou)

* Wed Apr 6 2016 Païou <paiiou> 0.10.0-11.paii6
- rebuild to fix .desktop files after liblxqt and libfm are fixed
- Update french translation

* Mon Nov 30 2015 Paiiou <paiiou> 0.10.0-10.paii6
- New package
