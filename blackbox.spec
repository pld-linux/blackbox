Summary:     Very small and fast window manger for the X-Windows.
Summary(pl): Bardzo ma³y i szybki menad¿er okien dla X-Windows.
Name:        blackbox
Version:     0.40.7
Release:     1
URL:         http://linux.wiw.org/blackbox/
Copyright:   GPL-2.0
Group:       X11/Window Managers
Vendor:      Brad Hughes <bhughes@arn.net>
Source:      http://linux.wiw.org/blackbox/sources/%{name}-%{version}.tar.bz2
Buildroot:   /tmp/%{name}-%{version}-root

%description
Blackbox is a window manager for the X/Windows environment.
It suports many "nice" features:
- Small code size (10352 lines in the 0.40.7).
- Minimal resource usage. Memory, CPU horse power and the load on
  the X server's resources are minimal.
- Fast interface with simple menus, multiple workspaces, and decorated windows
- Built-in graphics code to render solids, gradients and bevels on the fly
  when needed.
- Image dithering is possible for displays running at depths of 8,
  15 and 16 bits per pixel.
- Ability to run on displays with 8, 15, 16, 24 and 32 bits per pixel
- Near complete support for all ICCCM specified operation policies.

%description -l pl
Blackbox to menad¿er okien dla ¶rodowiska X-Windows.
Ma wiele ciekawych w³a¶ciwo¶ci:
- Bardzo ma³y kod ¼ród³owy (10352 linii w wersji 0.40.7)
- Minimalne zu¿ycie zasobów. Zajêto¶æ pamiêci, obci±¿enie procesora oraz
  zasobów X Serwera jest minimalne.
- Szybki interfejs z prostym systemem menu, wieloma pulpitami i dekoracyjnymi
  oknami.
- Wbudowany kod graficzny generuj±ce pe³nokolorowe, gradientowe i wyt³aczane
  elementy w czasie rzeczywistym.
- Przeliczanie palety kolorów (image dithering) pomiêdzy 8, 15 i 16-bitowym
  kolorem.
- Zdolno¶æ pracy z 8, 15, 16, 24 i 32-bitowym kolorem.
- Bliska kompletnej zgodno¶æ z za³o¿eniami ICCCM.

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
%defattr(644,root,root,755)
%doc README INSTALL Changelog
%attr(755,root,root) /usr/X11R6/bin/blackbox
/usr/X11R6/lib/X11/app-defaults/*

%changelog
* Fri Sep 25 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
  [0.40.7-1]
- Added -q in %setup,
- added pl translation.

* Sun Aug 23 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
  [0.40.4-1]
- Removed old log enteries.

* Thu Aug 13 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
  [0.40.3-1]
- New version
