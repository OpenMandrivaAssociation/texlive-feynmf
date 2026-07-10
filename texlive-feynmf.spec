%global tl_name feynmf
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.08
Release:	%{tl_revision}.1
Summary:	Macros and fonts for creating Feynman (and other) diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/feynmf
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/feynmf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/feynmf.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/feynmf.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The feynmf package provides an interface to Metafont (inspired by the
facilities of mfpic) to use simple structure specifications to produce
relatively complex diagrams. (The feynmp package, also part of this
bundle, uses MetaPost in the same way.) While the package was designed
for Feynman diagrams, it could in principle be used for diagrams in
graph and similar theories, where the structure is semi-algorithmically
determined.

