Summary:	Chemtool - program for 2D drawing organic molecules
Summary(pl):	Chemtool - program do rysowania 2-wymiarowych cz�steczek organicznych
Name:		chemtool
Version:	1.6
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://ruby.chemie.uni-freiburg.de/~martin/chemtool/%{name}-%{version}.tar.gz
# Source0-md5:	1b7a1bde89517ef8a1b4a566bfbd9b3f
Source1:	%{name}.desktop
URL:		http://ruby.chemie.uni-freiburg.de/~martin/chemtool/
BuildRequires:	autoconf
BuildRequires:	gtk+-devel >= 1.2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chemtool is a program for drawing organic molecules easily and store
them as a X bitmap, Xfig or EPS file. It runs under the X Window
System using the GTK widget set.

%description -l pl
Chemtool jest programem do rysowania cz�steczek organicznych i zapisu
ich jako pliki X-bitmap, Xfig lub EPS. Pracuje pod X Window u�ywaj�c
bibliotek GTK.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/{mimelnk/application,mime-info,mime-types} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Scientific/Chemistry,%{_pixmapsdir}/hicolor/32x32/mimetypes}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install kde/mimelnk/application/x-chemtool.desktop	$RPM_BUILD_ROOT%{_datadir}/mimelnk/application
install kde/icons/hicolor/32x32/mimetypes/chemtool.png	$RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/32x32/mimetypes
install gnome/mime-types/* 			$RPM_BUILD_ROOT%{_datadir}/mime-info
install %{SOURCE1}				$RPM_BUILD_ROOT%{_applnkdir}/Scientific/Chemistry
install gnome/gnome-application-chemtool.png %{name}.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO examples/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mimelnk/application/*
%{_pixmapsdir}/hicolor/32x32/mimetypes/*.png
%{_datadir}/mime-info/*
%{_pixmapsdir}/*.png
%{_pixmapsdir}/*.xpm
%{_applnkdir}/Scientific/Chemistry/*.desktop
%{_mandir}/man1/*
