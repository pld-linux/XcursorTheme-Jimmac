%define		_name Jimmac
Summary:	A cursor theme by Jimmac (GNOME's main artist).
Summary(pl):	Motyw kursor�w autorstwa Jimmaca (g��wny grafik GNOME).
Name:		XcursorTheme-%{_name}
Version:	1.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/6550-%{_name}.tar.gz
# Source0-md5:	46fb39d5e176dfc3bfa2c65743301f03
URL:		http://www.kde-look.org/content/show.php?content=6550
BuildRequires:	XFree86 >= 4.3
Buildarch:	noarch
Requires:	XFree86 >= 4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A professional, white cursor theme with thin black outlines.

%description -l pl
Profesjonalny, bia�y motyw kursor�w z cienkimi, czarnymi brzegami.

%prep
%setup -q -n %{_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/cursors
cp -df jimmac/cursors/*  $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/cursors
echo "[Icon Theme]" > $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/index.theme
echo "Name = Jimmac" >> $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/index.theme
echo "Comment = A cursor theme by Jimmac (GNOME's main artist)" >> $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/index.theme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/%{_name}