Name:		texlive-afparticle
Version:	35900
Release:	2
Summary:	Typesetting articles for Archives of Forensic Psychology
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/afparticle
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/afparticle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/afparticle.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/afparticle.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a class for typesetting articles for the
open access journal Archives of Forensic Psychology.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/afparticle
%{_texmfdistdir}/tex/latex/afparticle
%doc %{_texmfdistdir}/doc/latex/afparticle

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
