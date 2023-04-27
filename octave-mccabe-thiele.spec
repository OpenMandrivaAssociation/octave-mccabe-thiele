%global octpkg mccabe-thiele

Summary:	A toolbox for the McCabe-Thiele method for GNU Octave
Name:		octave-mccabe-thiele
Version:	0.1.5
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/mccabe-thiele/
Url:		https://github.com/aumpierre-unb/McCabe-Thiele-for-GNU-Octave/
Source0:	https://github.com/aumpierre-unb/McCabe-Thiele-for-GNU-Octave/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0

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

