%define	major 2
%define libname	%mklibname portaudio %{major}
%define devname %mklibname portaudio -d
%define cppmajor 0
%define libcpp %mklibname %{name}cpp %{cppmajor}
%define snapshot 20161030
%define maj_ver 19

Summary:	Cross platform audio I/O library
Name:		portaudio
Version:	190600_20161030
Release:	2
Group:		System/Libraries
License:	BSD
Url:		http://www.portaudio.com/
Source0:	http://www.portaudio.com/archives/pa_stable_v%{maj_ver}0600_%{snapshot}.tgz

Patch0:		portaudio-pkgconfig-alsa.patch
# Add some extra API needed by audacity
Patch1:		debian-20161225-audacity-portmixer.patch

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(celt)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	autoconf 
BuildRequires:	automake 
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:  gettext
BuildRequires:  glib-gettextize


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

%package -n	%{libcpp}
Summary:	Cross platform audio I/O library
Group:		System/Libraries

%description -n	%{libcpp}
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
distortion on a guitar, list available audio devices, etc

%package -n	%{devname}
Summary:	Development library and header files for the PortAudio library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	lib%{name}cpp-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libcpp} = %{version}-%{release}

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

autoreconf -i -f

%build
%configure \
	--with-alsa \
	--with-jack \
	--disable-static \
	--enable-cxx
	
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' bindings/cpp/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' bindings/cpp/libtool

# do not use make_build or build faied
make

%install
%make_install

%files -n %{libname}
%{_libdir}/libportaudio.so.%{major}*

%files -n %{libcpp}
%{_libdir}/lib%{name}cpp.so.%{cppmajor}
%{_libdir}/lib%{name}cpp.so.%{cppmajor}.*

%files -n %{devname}
%doc LICENSE.txt README.txt
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/portaudio-*.pc
%{_libdir}/pkgconfig/portaudiocpp.pc
