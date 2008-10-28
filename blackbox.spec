#
# TODO: review/update patches
#
# Conditional build:
%bcond_with	epistrophy	# enables using epistorophy key grabber
#
Summary:	Very small and fast window manger for the X Window
Summary(pl.UTF-8):	Mały i szybki zarządca okien dla X Window
Summary(de.UTF-8):	Blackbox ist ein Windowmanager
Name:		blackbox
Version:	0.70.1
Release:	3.1
License:	BSD-like
Group:		X11/Window Managers
Source0:	http://dl.sourceforge.net/blackboxwm/%{name}-%{version}.tar.gz
# Source0-md5:	2d173b95ca5e64ef478c6a5d2deee9df
Source1:	%{name}.desktop
Source3:	%{name}.1
Source4:	bsetroot.1
Source5:	%{name}-README.PLD
Source6:	%{name}-xsession.desktop
Patch0:		%{name}-am_fixes.patch
Patch1:		%{name}-pipe.patch
Patch3:		%{name}-epistrophy.patch
Patch4:		%{name}-etc_dir.patch
Patch5:		%{name}-nls-codesets.patch
Patch6:		%{name}-assert.patch
Patch7:		%{name}-lib64.patch
URL:		http://blackboxwm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_epistrophy:Requires:	epistrophy}
BuildRequires:	rpm >= 4.0.2-48
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXft-devel
Obsoletes:	fluxbox
Conflicts:	filesystem < 3.0-20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/%{name}
%define		_wmpropsdir	/usr/share/gnome/wm-properties

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

%description -l pl.UTF-8
Blackbox jest zarządcą okien dla X Window spełniającym prawie
wszystkie zalecenia ICCM. Jego zaletą jest estetyczny i szybki
interfejs z wieloma pulpitami i prostym menu. Wbudowano weń także
algorytm rysowania dekoracji okien, które mogą być jednokolorowe,
gradientowe lub trójwymiarowe. Blackbox oszczędza pamięć i czas CPU.

%description -l de.UTF-8
Blackbox ist ein Windowmanager für offene Betriebssystem wie z.B.
Linux oder freie BSD-Varianten. Er erfreut sich einer großen
Fangemeinde, da er sehr ressourcenschonend und voll konfigurierbar
ist.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1
%{?with_epistrophy:%patch3 -p1}
#%patch4 -p1
#%patch5 -p1
#%patch6 -p1
%if "%{_lib}" == "lib64"
%patch7 -p0
%endif

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_wmpropsdir},%{_mandir}/pl/man1,%{_sysconfdir}} \
	$RPM_BUILD_ROOT%{_datadir}/xsessions

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/pl/man1
install %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/pl/man1
cp %{SOURCE5} README.PLD
install %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README* ChangeLog LICENSE TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}
%dir %{_datadir}/blackbox
%{_datadir}/blackbox/styles
%{_datadir}/xsessions/%{name}.desktop
%{_wmpropsdir}/blackbox.desktop
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_datadir}/blackbox/menu
