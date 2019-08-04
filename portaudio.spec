%define	major 2
%define libname	%mklibname portaudio %{major}
%define devname %mklibname portaudio -d
%define snapshot 20161030
%define maj_ver 19

Summary:	Cross platform audio I/O library
Name:		portaudio
Version:	190600_20161030
Release:	1
Group:		System/Libraries
License:	BSD
Url:		http://www.portaudio.com/
Source0:	http://www.portaudio.com/archives/pa_stable_v%{maj_ver}0600_%{snapshot}.tgz
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(celt)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(samplerate)

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

%package -n	%{devname}
Summary:	Development library and header files for the PortAudio library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
This package contains the development PortAudio library and its header
files.

%prep
%setup -qn %{name}

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

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libportaudio.so.%{major}*

%files -n %{devname}
%doc LICENSE.txt README.txt
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/portaudio-*.pc

