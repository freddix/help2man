# based on PLD Linux spec git://git.pld-linux.org/packages/help2man.git
%include	/usr/lib/rpm/macros.perl

Summary:	Conversion tool to create man files
Name:		help2man
Version:	1.46.6
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/help2man/%{name}-%{version}.tar.xz
# Source0-md5:	320ca506f21823d183d2f573a18bead0
URL:		http://www.gnu.org/software/help2man/
BuildRequires:	gettext-devel
BuildRequires:	perl-Locale-gettext
BuildRequires:	rpm-perlprov
BuildRequires:	texinfo
Requires:	perl-Locale-gettext
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
help2man is a tool for automatically generating simple manual pages
from program output. This program is intended to provide an easy way
for software authors to include a manual page in their distribution
without having to maintain that document. Given a program which
produces reasonably standard `--help' and `--version' outputs,
help2man can re-arrange that output into something which resembles
a manual page.

%prep
%setup -q

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README THANKS
%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/bindtextdomain.so

%{_infodir}/*.info*
%{_mandir}/man1/help2man.1*
%lang(de) %{_mandir}/de/man1/help2man.1*
%lang(el) %{_mandir}/el/man1/help2man.1*
%lang(eo) %{_mandir}/eo/man1/help2man.1*
%lang(fi) %{_mandir}/fi/man1/help2man.1*
%lang(fr) %{_mandir}/fr/man1/help2man.1*
%lang(it) %{_mandir}/it/man1/help2man.1*
%lang(ja) %{_mandir}/ja/man1/help2man.1*
%lang(pl) %{_mandir}/pl/man1/help2man.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/help2man.1*
%lang(ru) %{_mandir}/ru/man1/help2man.1*
%lang(sr) %{_mandir}/sr/man1/help2man.1*
%lang(sv) %{_mandir}/sv/man1/help2man.1*
%lang(uk) %{_mandir}/uk/man1/help2man.1*

