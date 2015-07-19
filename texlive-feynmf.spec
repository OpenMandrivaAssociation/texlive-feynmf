# revision 17259
# category Package
# catalog-ctan /macros/latex/contrib/feynmf
# catalog-date 2010-03-01 15:04:13 +0100
# catalog-license gpl
# catalog-version 1.08
Name:		texlive-feynmf
Version:	1.08
Release:	10
Summary:	Macros and fonts for creating Feynman (and other) diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/feynmf
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/feynmf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/feynmf.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/feynmf.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The feynmf package provides an interface to MetaFont (inspired
by the facilities of mfpic) to use simple structure
specifications to produce relatively complex diagrams. (The
feynmp package, also part of this bundle, uses MetaPost in the
same way.) While the package was designed for Feynman diagrams,
it could in principle be used for diagrams in graph and similar
theories, where the structure is semi-algorithmically
determined.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metafont/feynmf/feynmf.mf
%{_texmfdistdir}/metapost/feynmf/feynmp.mp
%{_texmfdistdir}/metapost/feynmf/manpics.mp
%{_texmfdistdir}/tex/latex/feynmf/feynmf.sty
%{_texmfdistdir}/tex/latex/feynmf/feynmp.sty
%doc %{_texmfdistdir}/doc/latex/feynmf/Announce
%doc %{_texmfdistdir}/doc/latex/feynmf/COPYING
%doc %{_texmfdistdir}/doc/latex/feynmf/Feynman.Diagrams
%doc %{_texmfdistdir}/doc/latex/feynmf/README
%doc %{_texmfdistdir}/doc/latex/feynmf/Tutorial
%doc %{_texmfdistdir}/doc/latex/feynmf/fmfman.pdf
%doc %{_texmfdistdir}/doc/latex/feynmf/manpics.1
%doc %{_texmfdistdir}/doc/latex/feynmf/manpics.2
%doc %{_texmfdistdir}/doc/latex/feynmf/manpics.3
%doc %{_texmfdistdir}/doc/latex/feynmf/template.tex
#- source
%doc %{_texmfdistdir}/source/latex/feynmf/Makefile
%doc %{_texmfdistdir}/source/latex/feynmf/feynmf.drv
%doc %{_texmfdistdir}/source/latex/feynmf/feynmf.dtx
%doc %{_texmfdistdir}/source/latex/feynmf/feynmf.ins
%doc %{_texmfdistdir}/source/latex/feynmf/feynmf.pl
%doc %{_texmfdistdir}/source/latex/feynmf/feynmf209.ins
%doc %{_texmfdistdir}/source/latex/feynmf/feynmp.drv
%doc %{_texmfdistdir}/source/latex/feynmf/fmfman.drv
%doc %{_texmfdistdir}/source/latex/feynmf/fmfmanps.drv

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metafont metapost tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.08-2
+ Revision: 751832
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.08-1
+ Revision: 718428
- texlive-feynmf
- texlive-feynmf
- texlive-feynmf
- texlive-feynmf

