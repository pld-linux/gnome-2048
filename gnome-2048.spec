Summary:	A 2048 clone for GNOME
Name:		gnome-2048
Version:	3.18.1
Release:	1
License:	GPL v3
Group:		Applications
Source0:	http://download.gnome.org/sources/gnome-2048/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	363876f05d76cae37dbc213659e74cf1
URL:		https://wiki.gnome.org/Apps/2048
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	clutter-devel >= 1.12.0
BuildRequires:	clutter-gtk-devel >= 1.6.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.12.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	libgames-support-devel >= 0.1
BuildRequires:	libgee-devel >= 0.14.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.24.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	clutter >= 1.12.0
Requires:	clutter-gtk >= 1.6.0
Requires:	gtk+3 >= 3.12.0
Requires:	libgee >= 0.14.0
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GNOME clone of the popular game 2048.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%doc NEWS README
%attr(755,root,root) %{_bindir}/gnome-2048
%{_desktopdir}/org.gnome.gnome-2048.desktop
%{_datadir}/appdata/org.gnome.gnome-2048.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.2048.gschema.xml
%{_iconsdir}/hicolor/*/*/gnome-2048.png
%{_iconsdir}/hicolor/scalable/*/gnome-2048*.svg
