#
# Please submit bugfixes or comments via http://bugs.tizen.org/
#

Name:           inputproto
Version:        2.2
Release:        1
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          Development/System
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros)

%description
Description: %{summary}

%prep
%setup -q

%build

./autogen.sh
%reconfigure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

make %{?_smp_mflags}

%install
%make_install

%remove_docs


%files
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/*.h
%{_datadir}/pkgconfig/*.pc
