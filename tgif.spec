%define license QPL
%define prefix  /usr/X11R6

%define debug_package %{nil}

Summary: 	Xlib-based 2-D drawing tool
Name: 		tgif
Version: 	4.2.5
Release: 	2
Source0: 	%{name}-%{license}-%{version}.tar.gz
Source2:	tgif.png
Source3:	tgif-large.png
Source4:	tgif-mini.png
License: 	QPL
Group: 		Graphics
Url: 		http://bourbon.usc.edu/tgif/
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xt)

%description
Tgif (pronounced t-g-i-f) is an Xlib-based interactive 2-D drawing tool 
for Linux and most UNIX platforms.

%prep
%setup -q -n %{name}-%{license}-%{version}

%build
%configure2_5x
%make

%install
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
%__lzma -z tgif.1
%__install -m 644 tgif.1.lzma %{buildroot}%{prefix}/man/man1/

# Icons:
%__install -D -m 644 %{SOURCE2} %{buildroot}%{_iconsdir}/tgif.png
%__install -D -m 644 %{SOURCE3} %{buildroot}%{_liconsdir}/tgif.png
%__install -D -m 644 %{SOURCE4} %{buildroot}%{_miconsdir}/tgif.png

# XDG menu:
%__install -d -m 755 %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Tgif
Comment=Xlib-based 2-D drawing tool
Comment[ru]=Создание 2D рисунков
Exec=%{prefix}/bin/%{name} %f
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Graphics;VectorGraphics;
EOF

%files
%doc HISTORY README LICENSE.QPL Copyright
%{prefix}/bin/tgif
%dir %{prefix}/lib/X11/tgif
%{prefix}/lib/X11/tgif/*
%{prefix}/man/man1/*
%{_iconsdir}/tgif.png
%{_miconsdir}/tgif.png
%{_liconsdir}/tgif.png
%{_datadir}/applications/mandriva-%{name}.desktop
