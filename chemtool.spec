Summary:	Chemtool - program for 2D drawing organic molecules
Summary(pl.UTF-8):	Chemtool - program do rysowania 2-wymiarowych cząsteczek organicznych
Name:		chemtool
Version:	1.6.13
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://ruby.chemie.uni-freiburg.de/~martin/chemtool/%{name}-%{version}.tar.gz
# Source0-md5:	d263b8cf097134e36c5e929e7e77d668
Source1:	%{name}.desktop
URL:		http://ruby.chemie.uni-freiburg.de/~martin/chemtool/
BuildRequires:	autoconf >= 2.50
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chemtool is a program for drawing organic molecules easily and store
them as a X bitmap, Xfig or EPS file. It runs under the X Window
System using the GTK+ widget set.

%description -l pl.UTF-8
Chemtool jest programem do rysowania cząsteczek organicznych i zapisu
ich jako pliki X-bitmap, Xfig lub EPS. Pracuje pod X Window używając
bibliotek GTK+.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/{mimelnk/application,mime-info,mime-types} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_iconsdir}/hicolor/32x32/mimetypes}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install kde/mimelnk/application/x-chemtool.desktop	$RPM_BUILD_ROOT%{_datadir}/mimelnk/application
install kde/icons/hicolor/32x32/mimetypes/chemtool.png	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/mimetypes
install %{SOURCE1}				$RPM_BUILD_ROOT%{_desktopdir}
install gnome/gnome-application-chemtool.png %{name}.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO examples/{Neu2,*.{cht,mol,pdb}}
%attr(755,root,root) %{_bindir}/chemtool
%attr(755,root,root) %{_bindir}/chemtoolbg
%attr(755,root,root) %{_bindir}/cht
%{_datadir}/mimelnk/application/x-chemtool.desktop
%{_iconsdir}/hicolor/32x32/mimetypes/chemtool.png
%{_pixmapsdir}/gnome-application-chemtool.png
%{_pixmapsdir}/chemtool.xpm
%{_desktopdir}/chemtool.desktop
%{_mandir}/man1/chemtool.1*
%{_mandir}/man1/cht.1*
