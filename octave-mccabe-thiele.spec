%global octpkg mccabe-thiele

Summary:	A toolbox for the McCabe-Thiele method for GNU Octave. asd asdf safasdfsad fasdf sadfm ksajflksadjfklsajfdlk
Name:		octave-mccabe-thiele
Version:	0.1.5
Release:	1
License:	GPLv3+
Group:		Development/Python
#Url:		https://packages.octave.org/mccabe-thiele/
Url:		https://github.com/aumpierre-unb/McCabe-Thiele-for-GNU-Octave/
Source0:	https://github.com/aumpierre-unb/McCabe-Thiele-for-GNU-Octave/archive/v%{version}/mccabe-thiele-%{version}.tar.gz

#BuildRequires:	octave-devel >= 3.8.0
Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
A toolbox for the McCabe-Thiele method for GNU Octave.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n McCabe-Thiele-for-GNU-Octave-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

