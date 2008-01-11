%define name 	tgif
%define version 4.1.45 
%define release 10
%define license QPL
%define prefix  /usr/X11R6

Summary: 	Xlib-based 2-D drawing tool
Name: 		%{name}
Version: 	%{version}
Release: 	%mkrel %{release}
Source0: 	%{name}-%{license}-%{version}.tar.bz2
Source2:	tgif.png
Source3:	tgif-large.png
Source4:	tgif-mini.png
License: 	QPL
Group: 		Graphics
Url: 		http://bourbon.usc.edu/tgif/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	imake
BuildRequires:	X11-devel
BuildRequires:	libxt-devel

%description
Tgif (pronounced t-g-i-f) is an Xlib-based interactive 2-D drawing tool 
for Linux and most UNIX platforms.

%prep
%setup -q -n %{name}-%{license}-%{version}

%build
xmkmf
%__make -j 3

%install
%__rm -rf %{buildroot}
%__install -d -m 755 %{buildroot}%{prefix}/bin
%__install -d -m 755 %{buildroot}%{prefix}/lib/X11/tgif
%__install -d -m 755 %{buildroot}%{prefix}/man/man1

# Don't use make install because the paths are not correct:
%__install -s tgif %{buildroot}%{prefix}/bin/tgif
%__install -m 0444 tgif.Xdefaults %{buildroot}%{prefix}/lib/X11/tgif
%__install -m 0444 *.sym %{buildroot}%{prefix}/lib/X11/tgif
%__install -m 0444 keys.obj %{buildroot}%{prefix}/lib/X11/tgif

# Compress man page before installing:
%__cp tgif.man tgif.1
%__bzip2 tgif.1
%__install -m 644 tgif.1.bz2 %{buildroot}%{prefix}/man/man1/

# prtgif is deprecated:
%__rm -f %{buildroot}%{prefix}/bin/prtgif

# Icons:
%__install -D -m 644 %{SOURCE2} %{buildroot}%{_iconsdir}/tgif.png
%__install -D -m 644 %{SOURCE3} %{buildroot}%{_liconsdir}/tgif.png
%__install -D -m 644 %{SOURCE4} %{buildroot}%{_miconsdir}/tgif.png

# XDG menu:
%__install -d -m 755 %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Tgif
Comment=%{longtitle}
Exec=%{prefix}/bin/%{name} %f
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Graphics;VectorGraphics;X-MandrivaLinux-Office-Drawing;
EOF


%post
%{update_menus}

%postun
%{clean_menus}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc HISTORY README LICENSE.QPL Copyright
%{prefix}/bin/tgif
%dir %{prefix}/lib/X11/tgif
%{prefix}/lib/X11/tgif/*
%{prefix}/man/man1/*
%{_iconsdir}/tgif.png
%{_miconsdir}/tgif.png
%{_liconsdir}/tgif.png
%{_datadir}/applications/mandriva-%{name}.desktop

