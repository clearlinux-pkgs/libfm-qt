#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x42C9C8D3AF5EA5E3 (agaida@siduction.org)
#
Name     : libfm-qt
Version  : 0.14.1
Release  : 4
URL      : https://downloads.lxqt.org/downloads/libfm-qt/0.14.1/libfm-qt-0.14.1.tar.xz
Source0  : https://downloads.lxqt.org/downloads/libfm-qt/0.14.1/libfm-qt-0.14.1.tar.xz
Source99 : https://downloads.lxqt.org/downloads/libfm-qt/0.14.1/libfm-qt-0.14.1.tar.xz.asc
Summary  : A Qt/glib/gio-based lib used to develop file managers providing some file management utilities.
Group    : Development/Tools
License  : LGPL-2.1
Requires: libfm-qt-data = %{version}-%{release}
Requires: libfm-qt-lib = %{version}-%{release}
Requires: libfm-qt-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : doxygen
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : lxqt-build-tools
BuildRequires : pkgconfig(libexif)
BuildRequires : pkgconfig(libmenu-cache)
BuildRequires : qttools-dev

%description
# libfm-qt
## Overview
libfm-qt is the Qt port of libfm, a library providing components to build
desktop file managers which belongs to [LXDE](https://lxde.org).

%package data
Summary: data components for the libfm-qt package.
Group: Data

%description data
data components for the libfm-qt package.


%package dev
Summary: dev components for the libfm-qt package.
Group: Development
Requires: libfm-qt-lib = %{version}-%{release}
Requires: libfm-qt-data = %{version}-%{release}
Provides: libfm-qt-devel = %{version}-%{release}
Requires: libfm-qt = %{version}-%{release}

%description dev
dev components for the libfm-qt package.


%package lib
Summary: lib components for the libfm-qt package.
Group: Libraries
Requires: libfm-qt-data = %{version}-%{release}
Requires: libfm-qt-license = %{version}-%{release}

%description lib
lib components for the libfm-qt package.


%package license
Summary: license components for the libfm-qt package.
Group: Default

%description license
license components for the libfm-qt package.


%prep
%setup -q -n libfm-qt-0.14.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556946015
mkdir -p clr-build
pushd clr-build
export LDFLAGS="${LDFLAGS} -fno-lto"
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1556946015
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libfm-qt
cp LICENSE %{buildroot}/usr/share/package-licenses/libfm-qt/LICENSE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/cmake/*
/usr/share/libfm-qt/archivers.list
/usr/share/libfm-qt/terminals.list
/usr/share/libfm-qt/translations/libfm-qt_ar.qm
/usr/share/libfm-qt/translations/libfm-qt_ca.qm
/usr/share/libfm-qt/translations/libfm-qt_cs.qm
/usr/share/libfm-qt/translations/libfm-qt_cy.qm
/usr/share/libfm-qt/translations/libfm-qt_da.qm
/usr/share/libfm-qt/translations/libfm-qt_de.qm
/usr/share/libfm-qt/translations/libfm-qt_el.qm
/usr/share/libfm-qt/translations/libfm-qt_en_GB.qm
/usr/share/libfm-qt/translations/libfm-qt_es.qm
/usr/share/libfm-qt/translations/libfm-qt_fr.qm
/usr/share/libfm-qt/translations/libfm-qt_gl.qm
/usr/share/libfm-qt/translations/libfm-qt_he.qm
/usr/share/libfm-qt/translations/libfm-qt_hu.qm
/usr/share/libfm-qt/translations/libfm-qt_id.qm
/usr/share/libfm-qt/translations/libfm-qt_it.qm
/usr/share/libfm-qt/translations/libfm-qt_ja.qm
/usr/share/libfm-qt/translations/libfm-qt_lt.qm
/usr/share/libfm-qt/translations/libfm-qt_nb_NO.qm
/usr/share/libfm-qt/translations/libfm-qt_nl.qm
/usr/share/libfm-qt/translations/libfm-qt_pl.qm
/usr/share/libfm-qt/translations/libfm-qt_pt.qm
/usr/share/libfm-qt/translations/libfm-qt_pt_BR.qm
/usr/share/libfm-qt/translations/libfm-qt_ru.qm
/usr/share/libfm-qt/translations/libfm-qt_tr.qm
/usr/share/libfm-qt/translations/libfm-qt_uk.qm
/usr/share/libfm-qt/translations/libfm-qt_zh_CN.qm
/usr/share/libfm-qt/translations/libfm-qt_zh_TW.qm
/usr/share/mime-packages/libfm-qt-mimetypes.xml

%files dev
%defattr(-,root,root,-)
/usr/include/libfm-qt/appchoosercombobox.h
/usr/include/libfm-qt/appchooserdialog.h
/usr/include/libfm-qt/applaunchcontext.h
/usr/include/libfm-qt/appmenuview.h
/usr/include/libfm-qt/appmenuview_p.h
/usr/include/libfm-qt/bookmarkaction.h
/usr/include/libfm-qt/browsehistory.h
/usr/include/libfm-qt/cachedfoldermodel.h
/usr/include/libfm-qt/colorbutton.h
/usr/include/libfm-qt/core/archiver.h
/usr/include/libfm-qt/core/basicfilelauncher.h
/usr/include/libfm-qt/core/bookmarks.h
/usr/include/libfm-qt/core/cstrptr.h
/usr/include/libfm-qt/core/deletejob.h
/usr/include/libfm-qt/core/dirlistjob.h
/usr/include/libfm-qt/core/filechangeattrjob.h
/usr/include/libfm-qt/core/fileinfo.h
/usr/include/libfm-qt/core/fileinfo_p.h
/usr/include/libfm-qt/core/fileinfojob.h
/usr/include/libfm-qt/core/filelinkjob.h
/usr/include/libfm-qt/core/filemonitor.h
/usr/include/libfm-qt/core/fileoperationjob.h
/usr/include/libfm-qt/core/filepath.h
/usr/include/libfm-qt/core/filesysteminfojob.h
/usr/include/libfm-qt/core/filetransferjob.h
/usr/include/libfm-qt/core/folder.h
/usr/include/libfm-qt/core/folderconfig.h
/usr/include/libfm-qt/core/gioptrs.h
/usr/include/libfm-qt/core/gobjectptr.h
/usr/include/libfm-qt/core/iconinfo.h
/usr/include/libfm-qt/core/iconinfo_p.h
/usr/include/libfm-qt/core/job.h
/usr/include/libfm-qt/core/job_p.h
/usr/include/libfm-qt/core/legacy/fm-app-info.h
/usr/include/libfm-qt/core/legacy/fm-config.h
/usr/include/libfm-qt/core/legacy/glib-compat.h
/usr/include/libfm-qt/core/mimetype.h
/usr/include/libfm-qt/core/templates.h
/usr/include/libfm-qt/core/terminal.h
/usr/include/libfm-qt/core/thumbnailer.h
/usr/include/libfm-qt/core/thumbnailjob.h
/usr/include/libfm-qt/core/totalsizejob.h
/usr/include/libfm-qt/core/trashjob.h
/usr/include/libfm-qt/core/untrashjob.h
/usr/include/libfm-qt/core/userinfocache.h
/usr/include/libfm-qt/core/vfs/fm-file.h
/usr/include/libfm-qt/core/vfs/fm-xml-file.h
/usr/include/libfm-qt/core/volumemanager.h
/usr/include/libfm-qt/createnewmenu.h
/usr/include/libfm-qt/customaction_p.h
/usr/include/libfm-qt/customactions/fileaction.h
/usr/include/libfm-qt/customactions/fileactioncondition.h
/usr/include/libfm-qt/customactions/fileactionprofile.h
/usr/include/libfm-qt/dirtreemodel.h
/usr/include/libfm-qt/dirtreemodelitem.h
/usr/include/libfm-qt/dirtreeview.h
/usr/include/libfm-qt/dndactionmenu.h
/usr/include/libfm-qt/dnddest.h
/usr/include/libfm-qt/editbookmarksdialog.h
/usr/include/libfm-qt/execfiledialog_p.h
/usr/include/libfm-qt/filedialog.h
/usr/include/libfm-qt/filedialoghelper.h
/usr/include/libfm-qt/filelauncher.h
/usr/include/libfm-qt/filemenu.h
/usr/include/libfm-qt/filemenu_p.h
/usr/include/libfm-qt/fileoperation.h
/usr/include/libfm-qt/fileoperationdialog.h
/usr/include/libfm-qt/fileoperationdialog_p.h
/usr/include/libfm-qt/filepropsdialog.h
/usr/include/libfm-qt/filesearchdialog.h
/usr/include/libfm-qt/fm-qt_export.h
/usr/include/libfm-qt/fm-search.h
/usr/include/libfm-qt/folderitemdelegate.h
/usr/include/libfm-qt/foldermenu.h
/usr/include/libfm-qt/foldermodel.h
/usr/include/libfm-qt/foldermodelitem.h
/usr/include/libfm-qt/folderview.h
/usr/include/libfm-qt/folderview_p.h
/usr/include/libfm-qt/fontbutton.h
/usr/include/libfm-qt/libfmqt.h
/usr/include/libfm-qt/libfmqtglobals.h
/usr/include/libfm-qt/mountoperation.h
/usr/include/libfm-qt/mountoperationpassworddialog_p.h
/usr/include/libfm-qt/mountoperationquestiondialog_p.h
/usr/include/libfm-qt/pathbar.h
/usr/include/libfm-qt/pathbar_p.h
/usr/include/libfm-qt/pathedit.h
/usr/include/libfm-qt/pathedit_p.h
/usr/include/libfm-qt/placesmodel.h
/usr/include/libfm-qt/placesmodelitem.h
/usr/include/libfm-qt/placesview.h
/usr/include/libfm-qt/proxyfoldermodel.h
/usr/include/libfm-qt/renamedialog.h
/usr/include/libfm-qt/sidepane.h
/usr/include/libfm-qt/utilities.h
/usr/include/libfm-qt/utilities_p.h
/usr/include/libfm-qt/utils.h
/usr/include/libfm-qt/xdndworkaround.h
/usr/lib64/libfm-qt.so
/usr/lib64/pkgconfig/libfm-qt.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfm-qt.so.6
/usr/lib64/libfm-qt.so.6.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libfm-qt/LICENSE
