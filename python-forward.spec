%global modname forward
%global commit 94a6c2af58be59be9d779f4cc85af02532887f84
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{modname}
Version:        0.1
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Accurate electromagnetic head models and EEG lead field matrices from T1 / DTI
License:        GPLv2+
URL:            http://cyclotronresearchcentre.github.io/forward/
Source0:        https://github.com/CyclotronResearchCentre/forward/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
This project aims to simplify the preparation of accurate electromagnetic head
models for EEG forward modeling.

It builds off of the seminal SimNIBS tool for electromagnetic field modelling
of transcranial magnetic stimulation (TMS) and transcranial direct current
stimulation. Human skin, skull, cerebrospinal fluid, and brain meshing pipelines
have been rewritten with Nipype to ease access parallel processing and to allow
users to start/stop the workflows. Conductivity tensor mapping from
diffusion-weighted imaging is also included.

%package -n python2-%{modname}
Summary:        %{summary}
BuildRequires:  python2-devel
Requires:       numpy scipy
Requires:       h5py
Requires:       python2-nibabel
Requires:       python-matplotlib
Requires:       python2-nipype

%description -n python2-%{modname}
This project aims to simplify the preparation of accurate electromagnetic head
models for EEG forward modeling.

It builds off of the seminal SimNIBS tool for electromagnetic field modelling
of transcranial magnetic stimulation (TMS) and transcranial direct current
stimulation. Human skin, skull, cerebrospinal fluid, and brain meshing pipelines
have been rewritten with Nipype to ease access parallel processing and to allow
users to start/stop the workflows. Conductivity tensor mapping from
diffusion-weighted imaging is also included.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel
Requires:       python3-numpy python3-scipy
Requires:       python3-h5py
Requires:       python3-nibabel
Requires:       python3-matplotlib
Requires:       python3-nipype

%description -n python3-%{modname}
This project aims to simplify the preparation of accurate electromagnetic head
models for EEG forward modeling.

It builds off of the seminal SimNIBS tool for electromagnetic field modelling
of transcranial magnetic stimulation (TMS) and transcranial direct current
stimulation. Human skin, skull, cerebrospinal fluid, and brain meshing pipelines
have been rewritten with Nipype to ease access parallel processing and to allow
users to start/stop the workflows. Conductivity tensor mapping from
diffusion-weighted imaging is also included.

Python 3 version.

%prep
%autosetup -c
mv %{modname}-%{commit} python2
pushd python2
  sed -i -e '/import setuptools/d' setup.py
popd
cp -a python2 python3
2to3 --write --nobackup python3

%build
export LC_ALL="en_US.utf8"
pushd python2
  %py2_build
popd
pushd python3
  %py3_build
popd

%install
export LC_ALL="en_US.utf8"
pushd python2
  %py2_install
popd
pushd python3
  %py3_install
popd

%files -n python2-%{modname}
%license python2/LICENSE
%{python2_sitelib}/Forward*.egg-info
%{python2_sitelib}/%{modname}/

%files -n python3-%{modname}
%license python3/LICENSE
%{python3_sitelib}/Forward*.egg-info
%{python3_sitelib}/%{modname}/

%changelog
* Tue Nov 17 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1-0.1.git94a6c2a
- Initial package
