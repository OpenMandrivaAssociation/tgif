%define name 	tgif
%define version 4.2.5
%define release 1
%define license QPL
%define prefix  /usr/X11R6

Summary: 	Xlib-based 2-D drawing tool
Name: 		%{name}
Version: 	%{version}
Release: 	%mkrel %{release}
Source0: 	%{name}-%{license}-%{version}.tar.gz
Source2:	tgif.png
Source3:	tgif-large.png
Source4:	tgif-mini.png
License: 	QPL
Group: 		Graphics
Url: 		http://bourbon.usc.edu/tgif/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	X11-devel
BuildRequires:	libxt-devel

%description
Tgif (pronounced t-g-i-f) is an Xlib-based interactive 2-D drawing tool 
for Linux and most UNIX platforms.

%prep
%setup -q -n %{name}-%{license}-%{version}

%build
%configure2_5x
%make

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
Exec=%{prefix}/bin/%{name} %f
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Graphics;VectorGraphics;
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

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



%changelog
* Thu Jun 30 2011 Lev Givon <lev@mandriva.org> 4.2.5-1mdv2011.0
+ Revision: 688386
- Update to 4.2.5.

* Tue May 24 2011 Lev Givon <lev@mandriva.org> 4.2.3-2
+ Revision: 678203
- Force rebuild.
- Update to 4.2.3.

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 4.2.2-2mdv2011.0
+ Revision: 615173
- the mass rebuild of 2010.1 packages

* Thu Dec 10 2009 Lev Givon <lev@mandriva.org> 4.2.2-1mdv2010.1
+ Revision: 476024
- Update to 4.2.2.

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 4.1.45-12mdv2010.0
+ Revision: 434351
- rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 4.1.45-11mdv2009.0
+ Revision: 218426
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Feb 01 2008 Funda Wang <fwang@mandriva.org> 4.1.45-11mdv2008.1
+ Revision: 161045
- fix menu entry description

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 4.1.45-10mdv2008.1
+ Revision: 136546
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Oct 26 2006 Lev Givon <lev@mandriva.org> 4.1.45-10mdv2007.0
+ Revision: 72547
- Fix x86_64 deps.
- Try again..
- Fix deps yet again.
- Fix deps again.
- Fix build deps.
- Fix menu title.
- import tgif 4.1.45-4mdv2007.0

