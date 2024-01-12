Summary:	Control your GPG keys
Name:		plasma6-kgpg
Version:	24.01.90
Release:	2
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://utils.kde.org/projects/kgpg
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kgpg-%{version}.tar.xz
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KPim6AkonadiContactCore)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(ECM)
BuildRequires:	gpgme-devel
BuildRequires:	boost-devel

%description
KGpg is a simple interface for GnuPG, a powerful encryption utility.

%files -f kgpg.lang
%{_datadir}/qlogging-categories6/kgpg.categories
%{_bindir}/*
%{_datadir}/icons/*/*/*/*.*
%{_datadir}/metainfo/*.appdata.xml
%{_sysconfdir}/xdg/autostart/org.kde.kgpg.desktop
%{_datadir}/applications/org.kde.kgpg.desktop
%{_datadir}/config.kcfg/kgpg.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.kgpg.Key.xml
%{_datadir}/kio/servicemenus/*

%prep
%autosetup -p1 -n kgpg-%{?git:master}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kgpg --with-html