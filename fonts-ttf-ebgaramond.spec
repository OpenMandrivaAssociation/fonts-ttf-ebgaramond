%define pkgname	EBGaramond

Name:		fonts-ttf-ebgaramond
Summary:	A revival of Claude Garamont’s famous humanist typeface
Version:	0.016
Release:	1
License:	OFL
Group:		System/Fonts/True type
URL:		http://www.georgduffner.at/ebgaramond/index.html
Source0:	https://bitbucket.org/georgd/eb-garamond/downloads/EBGaramond-%{version}.zip
BuildArch:	noarch
BuildRequires:	freetype-tools
BuildRequires:	dos2unix

%description
Garamont’s fonts represent a milestone in the history of type design,
a touchstone to which font designers have been returning ever since.
EB Garamond is an open source project to create a revival of Claude
Garamont’s famous humanist typeface from the mid-16th century. Its design
reproduces the original by Claude Garamont: The source for the letterforms
is a scan of a specimen known as the “Berner specimen”, which, composed
in 1592 by Conrad Berner, son-in-law of Christian Egenolff and his successor
at the Egenolff print office, shows Garamont’s roman and Granjon’s italic
fonts at different sizes. Hence the name of this project: Egenolff-Berner
Garamond.

%prep
%setup -qn %{pkgname}-%{version}
dos2unix COPYING

%build

%install
%__mkdir_p %{buildroot}%{_xfontdir}/TTF/ebgaramond

%__install -m 644 ttf/*.ttf %{buildroot}%{_xfontdir}/TTF/ebgaramond
ttmkfdir %{buildroot}%{_xfontdir}/TTF/ebgaramond -o %{buildroot}%{_xfontdir}/TTF/ebgaramond/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/ebgaramond/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/ebgaramond \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-ebgaramond:pri=50

%files
%defattr(0644,root,root,0755)
%doc COPYING
%dir %{_xfontdir}/TTF/ebgaramond
%{_xfontdir}/TTF/ebgaramond/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/ebgaramond/fonts.dir
%{_xfontdir}/TTF/ebgaramond/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-ebgaramond:pri=50


%changelog
* Mon Aug 13 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.014e-1
+ Revision: 814504
- imported package fonts-ttf-ebgaramond

