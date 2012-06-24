# --with	epistrophy	(enables using epistorophy key grabber)

Summary:	Very small and fast window manger for the X Window
Summary(pl):	Ma�y i szybki menad�er okien dla X Window
Name:		blackbox
Version:	0.62.1
Release:	5
License:	GPL
Group:		X11/Window Managers
Vendor:		Brad Hughes <blackbox@alug.org>
Source0:	http://prdownloads.sourceforge.net/blackboxwm/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}-nls-pl.tar.bz2
Source3:	%{name}.1
Source4:	bsetroot.1
Source5:	%{name}-README.PLD
Patch0:		%{name}-am_fixes.patch
Patch1:		%{name}-pipe.patch
Patch2:		%{name}-nls-pl.patch
%{?_with_epistrophy:Patch3:	%{name}-epistrophy.patch}
URL:		http://blackboxwm.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	rpm >= 4.0.2-48
%{?_with_epistrophy:Requires:	epistrophy}
Obsoletes:	fluxbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/%{name}

%define		_gcc_ver	%(%{__cc} -dumpversion | cut -b 1)
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
Blackbox jest mened�erem okien dla X Window spe�niaj�cym prawie
wszystkie zalecenia ICCM. Jego zalet� jest estetyczny i szybki
interfejs z wieloma pulpitami i prostym menu. Wbudowano we� tak�e
algorytm rysowania dekoracji okien, kt�re mog� by� jednokolorowe,
gradientowe lub tr�jwymiarowe. Blackbox oszcz�dza pami�� i czas CPU.

%prep
%setup -q -a2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{?_with_epistrophy:%patch3 -p1}

%build
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/wm-properties,%{_mandir}/pl/man1}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/wm-properties/
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/pl/man1
install %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/pl/man1
cp %{SOURCE5} README.PLD

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
