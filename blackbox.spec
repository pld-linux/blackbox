Summary:	Very small and fast window manger for the X Window
Summary(pl):	Ma³y i szybki menad¿er okien dla X Window
Name:		blackbox
Version:	0.61.1
Release:	6
License:	GPL
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(pl):	X11/Zarz±dcy Okien
Vendor:		Brad Hughes <blackbox@alug.org>
Source0:	ftp://portal.alug.org/pub/blackbox/0.6x.x/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-lowcase_name.patch
Patch1:		%{name}-am_fixes.patch
URL:		http://blackbox.alug.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/%{name}

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
%patch1 -p1

%build
aclocal
autoconf
automake -a -c
%configure
%{__make} CXX="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/wm-properties

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/wm-properties/

gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_datadir}/wm-properties/blackbox.desktop
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%dir %{_sysconfdir}
%{_sysconfdir}/menu
%dir %{_datadir}/blackbox
%{_datadir}/blackbox/styles
