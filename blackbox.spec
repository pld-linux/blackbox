Summary:	Very small and fast window manger for the X Window.
Summary(pl):	Ma�y i szybki menad�er okien dla X Window.
Name:		blackbox
Version:	0.61.1
Release:	1
License:	GPL
Group:		X11/Window Managers
Group(pl):	X11/Zarz�dcy Okien
Vendor:		Brad Hughes <blackbox@alug.org>
Source0:	ftp://portal.alug.org/pub/blackbox/0.6x.x/%{name}-%{version}.tar.bz2
#Patch0:		blackbox-no-brueghel.patch
URL:		http://blackbox.alug.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man
%define		_datadir	/etc/X11

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
%setup -q
#%patch -p1

%build
LDFLAGS="-s"; export LDFLAGS 
%configure \
	--enable-kde
%{__make} CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz ChangeLog.gz
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/Blackbox/menu
%dir %{_datadir}/Blackbox

%attr(755,root,root) %{_bindir}/*
%{_datadir}/Blackbox/styles
