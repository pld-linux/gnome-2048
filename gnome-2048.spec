Summary:	A 2048 clone for GNOME
Summary(pl.UTF-8):	Klon gry 2048 dla GNOME
Name:		gnome-2048
Version:	3.38.2
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	https://download.gnome.org/sources/gnome-2048/3.38/%{name}-%{version}.tar.xz
# Source0-md5:	832ad54722224a1d90c6588fe77c010d
URL:		https://wiki.gnome.org/Apps/2048
BuildRequires:	appstream-glib
BuildRequires:	clutter-devel >= 1.12.0
BuildRequires:	clutter-gtk-devel >= 1.6.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.42.0
BuildRequires:	gtk+3-devel >= 3.24.0
BuildRequires:	libgnome-games-support-devel >= 1.7.1
BuildRequires:	libgee-devel >= 0.14.0
BuildRequires:	meson >= 0.37.1
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.24.0
BuildRequires:	vala-libgnome-games-support >= 1.7.1
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.42.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	clutter >= 1.12.0
Requires:	clutter-gtk >= 1.6.0
Requires:	glib2 >= 1:2.42.0
Requires:	gtk+3 >= 3.24.0
Requires:	hicolor-icon-theme
Requires:	libgnome-games-support >= 1.7.1
Requires:	libgee >= 0.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GNOME clone of the popular game 2048.

%description -l pl.UTF-8
Klon popularnej gry 2048 przeznaczony dla środowiska GNOME.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-2048
%{_datadir}/glib-2.0/schemas/org.gnome.TwentyFortyEight.gschema.xml
%{_datadir}/metainfo/org.gnome.TwentyFortyEight.appdata.xml
%{_desktopdir}/org.gnome.TwentyFortyEight.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.TwentyFortyEight.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.TwentyFortyEight-symbolic.svg
%{_mandir}/man6/gnome-2048.6*
