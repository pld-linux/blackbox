#
# Conditional build:
# _with_epistrophy	- enables using epistorophy key grabber
#
Summary:	Very small and fast window manger for the X Window
Summary(pl):	Ma³y i szybki zarz±dca okien dla X Window
Summary(de):	Blackbox ist ein Windowmanager
Name:		blackbox
Version:	0.65.0
Release:	2
License:	BSD-like
Group:		X11/Window Managers
Vendor:		Brad Hughes <blackbox@alug.org>
Source0:	http://dl.sourceforge.net/blackboxwm/%{name}-%{version}.tar.gz
# Source0-md5:	08560fa287c68d65fbe894696d04deaf
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
URL:		http://blackboxwm.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	rpm >= 4.0.2-48
%{?_with_epistrophy:Requires:	epistrophy}
Obsoletes:	fluxbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/%{name}
%define		_wmpropsdir	/usr/share/wm-properties

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
Blackbox jest zarz±dc± okien dla X Window spe³niaj±cym prawie
wszystkie zalecenia ICCM. Jego zalet± jest estetyczny i szybki
interfejs z wieloma pulpitami i prostym menu. Wbudowano weñ tak¿e
algorytm rysowania dekoracji okien, które mog± byæ jednokolorowe,
gradientowe lub trójwymiarowe. Blackbox oszczêdza pamiêæ i czas CPU.

%description -l de
Blackbox ist ein Windowmanager für offene Betriebssystem wie z.B.
Linux oder freie BSD-Varianten. Er erfreut sich einer großen
Fangemeinde, da er sehr ressourcenschonend und voll konfigurierbar
ist.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{?_with_epistrophy:%patch3 -p1}
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
rm -f missing
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
%dir %{_datadir}/blackbox/nls
%{_datadir}/blackbox/nls/C
%{_datadir}/blackbox/nls/POSIX
%{_datadir}/blackbox/nls/US_ASCII
%{_datadir}/blackbox/nls/en*
%lang(da) %{_datadir}/blackbox/nls/da*
%lang(de) %{_datadir}/blackbox/nls/de*
%lang(es) %{_datadir}/blackbox/nls/es
%lang(es_AR) %{_datadir}/blackbox/nls/es_AR
%lang(es) %{_datadir}/blackbox/nls/es_ES
%lang(es) %{_datadir}/blackbox/nls/es_MX
%lang(fr) %{_datadir}/blackbox/nls/fr*
%lang(hu) %{_datadir}/blackbox/nls/hu*
%lang(it) %{_datadir}/blackbox/nls/it*
%lang(ja) %{_datadir}/blackbox/nls/ja*
%lang(ko) %{_datadir}/blackbox/nls/ko*
%lang(lv) %{_datadir}/blackbox/nls/lv*
%lang(nl) %{_datadir}/blackbox/nls/nl*
%lang(nb) %{_datadir}/blackbox/nls/no*
%lang(pl) %{_datadir}/blackbox/nls/pl*
%lang(pt_BR) %{_datadir}/blackbox/nls/pt_BR
%lang(ro) %{_datadir}/blackbox/nls/ro*
%lang(ru) %{_datadir}/blackbox/nls/ru*
%lang(sk) %{_datadir}/blackbox/nls/sk*
%lang(sl) %{_datadir}/blackbox/nls/sl*
%lang(sv) %{_datadir}/blackbox/nls/sv*
%lang(uk) %{_datadir}/blackbox/nls/uk*
%lang(zh_CN) %{_datadir}/blackbox/nls/zh_CN
%lang(zh_TW) %{_datadir}/blackbox/nls/zh_TW
%{_datadir}/xsessions/%{name}.desktop
%{_wmpropsdir}/blackbox.desktop
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_sysconfdir}/menu
