Summary:     Very small and fast window manger for the X-Windows.
Summary(pl): Ma³y i szybki menad¿er okien dla X-Windows.
Name:        blackbox
Version:     0.40.13
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
CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure --prefix=/usr/X11R6
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults
make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README ChangeLog
%attr(755, root, root) /usr/X11R6/bin/blackbox
%dir /usr/X11R6/share/Blackbox
%config(noreplace) %verify(not size md5 mtime) /usr/X11R6/share/Blackbox/*

%changelog
* Thu Nov  5 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.40.12-1]
- changelog Changed to ChangeLog in %doc,
- files in /usr/X11R6/share/Blackbox/ makked as %config with
  %verify(not size md5 mtime),
- removed /usr/X11R6/lib/X11/app-defaults/* from %files.

* Mon Nov  2 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.40.11-1]
- updated for using new autoconf scheme (instead old Imake).

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
