Summary:     Very small and fast window manger for the X-Windows.
Summary(pl): Ma³y i szybki menad¿er okien dla X-Windows.
Name:        blackbox
Version:     0.40.9
Release:     1
URL:         http://linux.wiw.org/blackbox/
Copyright:   GPL-2.0
Group:       X11/Window Managers
Vendor:      Brad Hughes <bhughes@arn.net>
Source:      http://linux.wiw.org/blackbox/sources/%{name}-%{version}.tar.bz2
Buildroot:   /tmp/%{name}-%{version}-root

%description
Blackbox is a window manager for the X Window environment, which is almost
completely compliant with ICCCM specified operation policies. It features
nice and fast interface with multiple workspaces and simple menus. Fast
built-in graphics code that can render solids, gradients and bevels is used
to draw window decorations. Remaining small in size, blackbox preserves
memory and CPU.                                                       

%description -l pl
Blackbox jest mened¿erem okien dla X Window spe³niaj±cym prawie wszystkie
zalecenia ICCM. Jego zalet± jest estetyczny i szybki interfejs z wieloma
pulpitami i prostym menu. Wbudowano weñ tak¿e algorytm rysowania dekoracji
okien, które mog± byæ jednokolorowe, gradientowe lub trójwymiarowe.
Blackbox oszczêdza pamiêæ i czas CPU.                           

%prep
%setup -q

%build
xmkmf -a
make CXXDEBUGFLAGS="$RPM_OPT_FLAGS" CDEBUGFLAGS="$RPM_OPT_FLAGS"

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(644, root, root, 755)
%doc README Changelog
%attr(755, root, root) /usr/X11R6/bin/blackbox
/usr/X11R6/lib/X11/app-defaults/*

%changelog
* Sun Sep 27 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
  [0.40.7-2]
- rewritten %descriptions,
- removed INSTALL-file from %doc.

* Fri Sep 25 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
  [0.40.7-1]
- added -q in %setup,
- added pl translation.

* Sun Aug 23 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
  [0.40.4-1]
- removed old log enteries.

* Thu Aug 13 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
  [0.40.3-1]
- aew version
