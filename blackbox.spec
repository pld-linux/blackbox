# _with_gcc3:	budowanie z gcc3 

Summary:	Very small and fast window manger for the X Window
Summary(pl):	Ma³y i szybki menad¿er okien dla X Window
Name:		blackbox
Version:	0.62.1
Release:	3
License:	GPL
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
Vendor:		Brad Hughes <blackbox@alug.org>
Source0:	http://prdownloads.sourceforge.net/blackboxwm/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-am_fixes.patch
URL:		http://blackboxwm.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/%{name}

%{?_with_gcc3:%define		__cxx		"%{__cc} -lstdc++"}
%{!?_with_gcc3:%define		__cxx		"%{__cc}"}

%description
Blackbox is a window manager for the X Window environment, which is
almost completely compliant with ICCCM specified operation policies.
It features nice and fast interface with multiple workspaces and
simple menus. Fast built-in graphics code that can render solids,
gradients and bevels is used to draw window decorations. Remaining
small in size, blackbox preserves memory and CPU.

%description -l pl
Blackbox jest mened¿erem okien dla X Window spe³niaj±cym prawie
wszystkie zalecenia ICCM. Jego zalet± jest estetyczny i szybki
interfejs z wieloma pulpitami i prostym menu. Wbudowano weñ tak¿e
algorytm rysowania dekoracji okien, które mog± byæ jednokolorowe,
gradientowe lub trójwymiarowe. Blackbox oszczêdza pamiêæ i czas CPU.

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/wm-properties

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/wm-properties/

gzip -9nf README* ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}
%dir %{_datadir}/blackbox
%{_datadir}/blackbox/styles/*
%{_datadir}/blackbox/nls/*
%{_datadir}/wm-properties/blackbox.desktop
%{_mandir}/man1/*
%{_sysconfdir}/menu
