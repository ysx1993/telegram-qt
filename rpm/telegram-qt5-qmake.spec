Name: telegram-qt
Summary: Qt library for Telegram network

%define version_major 0
%define version_minor 2
%define version_patch 0

Version: %{version_major}.%{version_minor}.%{version_patch}
Release: 1
Group: System/Libraries
License: LGPLv2.1
URL: https://github.com/Kaffeine/telegram-qt
Source0: https://github.com/Kaffeine/telegram-qt/releases/download/telegram-qt-%{version}/telegram-qt-%{version}.tar.bz2
BuildRequires: qt%{_qt5_version}-qtcore-devel >= %qt_abi_version
BuildRequires: qt%{_qt5_version}-qtgui-devel >= %qt_abi_version
BuildRequires: qt%{_qt5_version}-qtnetwork-devel >= %qt_abi_version
BuildRequires: qt%{_qt5_version}-qtdeclarative-devel >= %qt_abi_version
BuildRequires: qt%{_qt5_version}-qtdeclarative-qtquick-devel >= %qt_abi_version
BuildRequires: qt%{_qt5_version}-qmake >= %qt_abi_version
BuildRequires: pkgconfig(openssl)

%description
%{summary}.

%package qt5
Summary: TelegramQt library for Qt5
Group: Development/Libraries

%description qt5
%{summary}.

%package qt5-devel
Summary:    Development headers and pkg-config for TelegramQt library
Group:      Development/Libraries
Requires:   %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-devel
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build
%{qmake_qt5} \
  "BUILD_ONLY_LIBRARY=true" \
  "INSTALL_PREFIX=%{_qt5_prefix}" \
  "INSTALL_LIB_DIR=%{_qt5_libdir}" \
  "INSTALL_INCLUDE_DIR=%{_qt5_headerdir}"

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files qt5
%defattr(-,root,root,-)
%{_qt5_libdir}/libTelegramQt5.so
%{_qt5_libdir}/libTelegramQt5.so.%{version_major}
%{_qt5_libdir}/libTelegramQt5.so.%{version_major}.%{version_minor}
%{_qt5_libdir}/libTelegramQt5.so.%{version_major}.%{version_minor}.%{version_patch}

%files qt5-devel
%defattr(-,root,root,-)
%{_qt5_headerdir}/telegram-qt5/TelegramQt/*
%{_qt5_libdir}/pkgconfig/TelegramQt5.pc
