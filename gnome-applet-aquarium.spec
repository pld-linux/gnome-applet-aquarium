Summary:	Sherman's aquarium
Summary(pl.UTF-8):	Akwarium wzorowane na komiksie Sherman's Lagoon
Name:		gnome-applet-aquarium
Version:	2.2.0
Release:	2
License:	GPL (except for images - see COPYING)
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/aquariumapplet/shermans_aquarium-%{version}.tar.gz
# Source0-md5:	d5c6220272d18799336e0437d776d083
Patch0:		shermans_aquarium-gcc33.patch
Patch1:		shermans_aquarium-opt.patch
Patch2:		%{name}-as-needed.patch
URL:		http://aquariumapplet.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf >= 2.13
BuildRequires:	gnome-panel-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Provides:	aquariumapplet = %{version}-%{release}
Obsoletes:	aquariumapplet <= 2.2.0-1
Obsoletes:	shermans_aquarium
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		specflags	-I%{_includedir}/libgnomeui-2.0

%description
An applet that shows a bunch of swimming fishes from the comic
Sherman's Lagoon, shows the CPU load, status leds and the time.
Includes also module for xscreensaver.

%description -l pl.UTF-8
Applet pokazujący stworzenia z komiksu Sherman's Lagoon, monitor
obciążenia procesora, monitor klawiatury i zegar. Zawiera również
moduł wygaszacza ekranu dla xscreensaver.

%prep
%setup -q -n shermans_aquarium-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%{__sed} -e 's@/lib/@/%{_lib}/@' -i src/Makefile.in

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/bonobo/servers,%{_datadir}/gnome-2.0/ui,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains only note about images
%doc AUTHORS BUGS COPYING FAQ NEWS README TODO XSCREENSAVER
%attr(755,root,root) %{_bindir}/*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/aquarium
%{_datadir}/gnome-2.0/ui/*.xml
%{_pixmapsdir}/*.png
