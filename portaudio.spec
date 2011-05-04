%define	major 2
%define libname	%mklibname portaudio %{major}
%define develname %mklibname portaudio -d
%define snapshot 20071207

Summary:	Cross platform audio I/O library
Name:		portaudio
Version:	19
Release:	%mkrel 17
Group:		System/Libraries
License:	BSD
URL:		http://www.portaudio.com/
Source0:	http://www.portaudio.com/archives/pa_stable_v%{version}_%{snapshot}.tar.gz
# From Fedora #445644 (Kevin Kofler): fix it to work with non-mmap ALSA
# devices - importantly, PulseAudio's ALSA emulation - AdamW 2008/12
Patch0:		portaudio-19-alsa_pulse.patch
BuildRequires:	pkgconfig
BuildRequires:	libalsa-devel
BuildRequires:	libjack-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	celt-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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
Group:          System/Libraries

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
Obsoletes:	%mklibname -d portaudio 2
Obsoletes:	%mklibname -d portaudio 1
Conflicts:	%mklibname -d portaudio 0
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
%patch0 -p1 -b .pulse

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc LICENSE.txt README.txt
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/portaudio-*.pc
