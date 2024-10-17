#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/PROTO/emote emote; \
#cd emote; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#VERSION=$(cat configure.ac | grep "emote" | grep INIT | sed 's@\[@@g' | sed 's@\]@@g' | sed 's@)@@g' | cut -d, -f 2 | sed "s@ @@"); \
#PKG_VERSION=$VERSION.$SVNREV; \
#cd ..; \
#tar -Jcf emote-$PKG_VERSION.tar.xz emote/ --exclude .svn --exclude .*ignore

%define svnrev	76838

%define major   0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Emotion icons
Name:		emote
Version:	0.0.1
Release:	0.%{svnrev}.1
License:	GPLv3
Group:		Graphical desktop/Enlightenment
URL:		https://enlightenment.org/
Source0: 	%{name}-%{version}.%{svnrev}.tar.xz

BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(elementary)

%description
Emote emotion icons for applications.

%package -n %{libname}
Summary:    Emote library
Group:      System/Libraries

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{develname}
Summary:    Emote headers, libraries, documentation and test programs
Group:      Development/C
Requires:   %{libname} = %{version}
Provides:   %{name}-devel = %{version}-%{release}

%description -n %{develname}
Headers and libraries from %{name}

%prep
%setup -qn %{name}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
rm -fr %{buildroot}/%{_datadir}/%{name}/{COPYING,AUTHORS}

%find_lang %{name}

%files  -f %{name}.lang
%doc COPYING AUTHORS
%{_bindir}/emote
%{_datadir}/icons/*.png
%{_datadir}/applications/*.desktop
%{_libdir}/%{name}/protocols/*.so

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}/*.h
