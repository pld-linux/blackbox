Summary:	Very small and fast window manger for the X Window.
Summary(pl):	Ma³y i szybki menad¿er okien dla X Window.
Name:		blackbox
Version:	0.50.5
Release:	1
Copyright:	GPL-2.0
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy Okien
Vendor:		Brad Hughes <bhughes@arn.net>
Source:		ftp://balance.wiw.org/pub/blackbox/%{name}-%{version}.tar.bz2
Patch:		blackbox-no-brueghel.patch
URL:		http://linux.wiw.org/blackbox/
Buildroot:	/tmp/%{name}-%{version}-root

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6/man

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
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--datadir=/etc/X11 \
	--enable-kde
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz ChangeLog.gz
%config(noreplace) %verify(not size md5 mtime) /etc/X11/Blackbox/menu
%dir /etc/X11/Blackbox

%attr(755,root,root) /usr/X11R6/bin/*
/etc/X11/Blackbox/styles
