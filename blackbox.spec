Summary:     Very small and fast window manger for the X-Windows.
Summary(pl): Ma�y i szybki menad�er okien dla X-Windows.
Name:        blackbox
Version:     0.50.0
Release:     2
Copyright:   GPL-2.0
Group:       X11/Window Managers
Vendor:      Brad Hughes <bhughes@arn.net>
Source:      http://linux.wiw.org/blackbox/sources/%{name}-%{version}.tar.bz2
URL:         http://linux.wiw.org/blackbox/
Buildroot:   /tmp/%{name}-%{version}-root

%description
Blackbox is a window manager for the X Window environment, which is almost
completely compliant with ICCCM specified operation policies. It features
nice and fast interface with multiple workspaces and simple menus. Fast
built-in graphics code that can render solids, gradients and bevels is used
to draw window decorations. Remaining small in size, blackbox preserves
memory and CPU.                                                       

%description -l pl
Blackbox jest mened�erem okien dla X Window spe�niaj�cym prawie wszystkie
zalecenia ICCM. Jego zalet� jest estetyczny i szybki interfejs z wieloma
pulpitami i prostym menu. Wbudowano we� tak�e algorytm rysowania dekoracji
okien, kt�re mog� by� jednokolorowe, gradientowe lub tr�jwymiarowe.
Blackbox oszcz�dza pami�� i czas CPU.                           

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6 \
	--datadir=/etc/X11
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README ChangeLog
/etc/X11/Blackbox/styles/*
%config(noreplace) %verify(not size md5 mtime) /etc/X11/Blackbox/menu
%config(noreplace) %verify(not size md5 mtime) /etc/X11/Blackbox/rc
%attr(755, root, root) /usr/X11R6/bin/*
%dir /etc/X11/Blackbox
%dir /etc/X11/Blackbox/styles

%changelog
* Tue Nov 24 1998 Maciej Le�niewski <nimir@kis.p.lodz.pl>
  [0.50.0-2]
- %config files moved to /etc/X11,
- Few fixes of %files macro.

* Tue Nov 24 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.50.0-1]
- simplification: added using $DESTDIR on "make install",
- added CFLAGS="$RPM_OPT_FLAGS" to configure enviroment.

* Thu Nov  5 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.40.12-1]
- changelog changed to ChangeLog in %doc,
- files in /usr/X11R6/share/Blackbox/{menu,rc,styles/*} marked as %config
  with %verify rules,
- removed /usr/X11R6/lib/X11/app-defaults/* from %files.

* Mon Nov  2 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.40.11-1]
- updated for using new autoconf scheme (instead old Imake).

* Sun Sep 27 1998 Maciej Le�niewski <nimir@kis.p.lodz.pl>
  [0.40.7-2]
- rewritten %descriptions,
- removed INSTALL-file from %doc.

* Fri Sep 25 1998 Maciej Le�niewski <nimir@kis.p.lodz.pl>
  [0.40.7-1]
- added -q in %setup,
- added pl translation.

* Sun Aug 23 1998 Maciej Le�niewski <nimir@kis.p.lodz.pl>
  [0.40.4-1]
- removed old log enteries.

* Thu Aug 13 1998 Maciej Le�niewski <nimir@kis.p.lodz.pl>
  [0.40.3-1]
- aew version
