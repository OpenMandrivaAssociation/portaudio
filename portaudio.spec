%define	major 2
%define libname	%mklibname portaudio %{major}
%define develname %mklibname portaudio -d
%define snapshot 20110326

Summary:	Cross platform audio I/O library
Name:		portaudio
Version:	19
Release:	23
Group:		System/Libraries
License:	BSD
URL:		http://www.portaudio.com/
Source0:	http://www.portaudio.com/archives/pa_stable_v%{version}_%{snapshot}.tgz
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(celt)

%description
PortAudio is a free, cross platform, open-source, audio I/O 
library. It lets you write simple audio programs in 'C' that will
compile and run on many platforms including Windows, Macintosh 
(8,9,X), Unix (OSS), SGI, and BeOS. PortAudio is intended to
promote the exchange of audio synthesis software between
developers on different platforms, and was recently selected as
the audio component of a larger PortMusic project that includes
MIDI and sound file support. 

PortAudio provides a very simple API for recording and/or playing
sound using a simple callback function. Example programs are 
included that synthesize sine waves and pink noise, perform fuzz
distortion on a guitar, list available audio devices, etc. 

%package -n	%{libname}
Summary:	Cross platform audio I/O library
Group:		System/Libraries
Provides:	libportaudio2

%description -n	%{libname}
PortAudio is a free, cross platform, open-source, audio I/O 
library. It lets you write simple audio programs in 'C' that will
compile and run on many platforms including Windows, Macintosh 
(8,9,X), Unix (OSS), SGI, and BeOS. PortAudio is intended to
promote the exchange of audio synthesis software between
developers on different platforms, and was recently selected as
the audio component of a larger PortMusic project that includes
MIDI and sound file support. 

PortAudio provides a very simple API for recording and/or playing
sound using a simple callback function. Example programs are 
included that synthesize sine waves and pink noise, perform fuzz
distortion on a guitar, list available audio devices, etc. 

%package -n	%{develname}
Summary:	Static library and header files for the PortAudio library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname -d portaudio 2} < 19-21
Obsoletes:	%{mklibname -d portaudio 1} < 19-21
Conflicts:	%{mklibname -d portaudio 0} < 19-21
# (Anssi 03/2008) Do not obsolete portaudio0, we still have it.

%description -n	%{develname}
PortAudio is a free, cross platform, open-source, audio I/O 
library. It lets you write simple audio programs in 'C' that will
compile and run on many platforms including Windows, Macintosh 
(8,9,X), Unix (OSS), SGI, and BeOS. PortAudio is intended to
promote the exchange of audio synthesis software between
developers on different platforms, and was recently selected as
the audio component of a larger PortMusic project that includes
MIDI and sound file support. 

PortAudio provides a very simple API for recording and/or playing
sound using a simple callback function. Example programs are 
included that synthesize sine waves and pink noise, perform fuzz
distortion on a guitar, list available audio devices, etc. 

This package contains the static PortAudio library and its header
files.

%prep
%setup -q -n %{name}

# fix dir perms
find . -type d | xargs chmod 755

# fix file perms
find . -type f | xargs chmod 644
chmod 755 configure

# strip away annoying ^M
find . -type f | xargs perl -p -i -e 's/\r//'

%build
%configure2_5x \
    --with-alsa \
    --with-jack

%make

#CC="gcc" \
#    CFLAGS="%{optflags} -fPIC -DPIC -D_REENTRANT -D_GNU_SOURCE -Ipa_common -Ipablio"

%install
%makeinstall_std

%files -n %{libname}
%doc LICENSE.txt README.txt
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/portaudio-*.pc

%changelog
* Thu May 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 19-21
+ Revision: 797858
- rel up
- provides: libportaudio2

* Wed Jan 11 2012 Götz Waschk <waschk@mandriva.org> 19-20
+ Revision: 759771
- rebuild
- update build deps
- remove libtool archive

* Tue Nov 08 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 19-18
+ Revision: 728931
- clean out old rpm junk
- drop static library
- update to latest release: v19 20110326

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 19-17
+ Revision: 667805
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 19-16mdv2011.0
+ Revision: 607191
- rebuild

* Sat Feb 27 2010 Götz Waschk <waschk@mandriva.org> 19-15mdv2010.1
+ Revision: 512441
- rebuild for new libjack

* Wed Jan 27 2010 Götz Waschk <waschk@mandriva.org> 19-14mdv2010.1
+ Revision: 497063
- rebuild for new celt

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 19-13mdv2010.0
+ Revision: 426738
- rebuild
- Don't uselessly call autoreconf

* Sat Dec 13 2008 Adam Williamson <awilliamson@mandriva.org> 19-12mdv2009.1
+ Revision: 314007
- celt-devel not libcelt-devel
- buildrequires libcelt-devel too
- buildrequires libsamplerate-devel, apparently?
- add alsa_pulse.patch (from Fedora #445644 / Kevin Kofler): fix support
  for non-mmap ALSA devices (importantly, Pulse)

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 19-11mdv2009.0
+ Revision: 225023
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Mar 07 2008 Funda Wang <fwang@mandriva.org> 19-10mdv2008.1
+ Revision: 181137
- conflicts with portaudio0-devel

* Thu Mar 06 2008 Anssi Hannula <anssi@mandriva.org> 19-9mdv2008.1
+ Revision: 180947
- do not obsolete portaudio0, we still have it

* Tue Mar 04 2008 Funda Wang <fwang@mandriva.org> 19-8mdv2008.1
+ Revision: 178485
- obsoletes more old devel package

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 19-7mdv2008.1
+ Revision: 171049
- rebuild
- summary is not licence tag
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Fri Feb 15 2008 Frederic Crozat <fcrozat@mandriva.com> 19-6mdv2008.1
+ Revision: 169000
- Update to stable v19 20071207 snapshot (fixes espeak when using pulseaudio alsa plugin)

* Fri Jan 25 2008 Funda Wang <fwang@mandriva.org> 19-5mdv2008.1
+ Revision: 157826
- new devel package policy

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 19 2007 Oden Eriksson <oeriksson@mandriva.com> 19-4mdv2008.0
+ Revision: 67030
- use a new snapshot due to api changes in latest jackit
- the patch (P4) does not apply (no more pablio/ringbuffer.h)

