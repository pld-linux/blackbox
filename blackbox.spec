Summary:	Very small and fast window manger for the X Window
Summary(pl):	Ma³y i szybki menad¿er okien dla X Window
Name:		blackbox
Version:	0.62.1
Release:	4.7
License:	GPL
Group:		X11/Window Managers
Vendor:		Brad Hughes <blackbox@alug.org>
Source0:	http://prdownloads.sourceforge.net/blackboxwm/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}-nls-pl.tar.bz2
Source3:	%{name}.1
Source4:	bsetroot.1
Patch0:		%{name}-am_fixes.patch
Patch1:		%{name}-pipe.patch
Patch2:		%{name}-nls-pl.patch
URL:		http://blackboxwm.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	rpm >= 4.0.2-48
Obsoletes:	fluxbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/%{name}

%define		_gcc_ver	%(%{__cc} --version | cut -b 1)
%if %{_gcc_ver} == 2
%define		__cxx		"%{__cc}"
%endif

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
%setup -q -a2
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
aclocal
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/wm-properties,%{_mandir}/pl/man1}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/wm-properties/
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/pl/man1
install %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/pl/man1
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
%{_mandir}/pl/man1/*
%{_sysconfdir}/menu
