Summary:	Chemtool - program for 2D drawing organic molecules.
Summary(pl):	Chemtool - program do rysowania 2-wymiarowych cz±steczek organicznych.
Name:		chemtool
Version:	1.5
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://www.uni-ulm.de/~s_tvolk/chemtool/src/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.uni-ulm.de/~s_tvolk/chemtool.html
BuildRequires:	autoconf
BuildRequires:	gtk+-devel >= 1.2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Chemtool is a program for drawing organic molecules easily and store
them as a X bitmap, Xfig or EPS file. It runs under the X Window
System using the GTK widget set.

%description -l pl
Chemtool jest programem do rysowania cz±steczek organicznych i zapisu
ich jako pliki X-bitmap, Xfig lub EPS. Pracuje pod X Window u¿ywaj±c
bibliotek GTK.

%prep
%setup -q
%patch -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/{pixmaps/hicolor/32x32/mimetypes,mimelnk/application,mime-info} \
	$RPM_BUILD_ROOT%{_applnkdir}/Scientific

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install kde/mimelnk/application/x-chemtool.desktop	$RPM_BUILD_ROOT%{_datadir}/mimelnk/application
install kde/icons/hicolor/32x32/mimetypes/chemtool.png	$RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/32x32/mimetypes
install gnome/mime-types/* 			$RPM_BUILD_ROOT%{_datadir}/mime-info
install %{SOURCE1}				$RPM_BUILD_ROOT%{_applnkdir}/Scientific
install gnome/gnome-application-chemtool.png %{name}.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO examples/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mimelnk/application/*
%{_pixmapsdir}/hicolor/32x32/mimetypes/*.png
%{_datadir}/mime-info/*
%{_pixmapsdir}/*.png
%{_pixmapsdir}/*.xpm
%{_applnkdir}/Scientific/*.desktop
