%global upname forward
%{!?__python2: %global __python2 %__python}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:           python-forward
Version:        0.1
Release:        1%{?dist}
Summary:        Accurate electromagnetic head models and EEG lead field matrices from T1 / DTI
License:        GPLv2
URL:             
Source0:        %{upname}.tar.gz
#BuildArch:      
BuildRequires:  python2-devel
%if %{with python3}
BuildRequires:  python3-devel
%endif # with python3

%description
This project aims to simplify the preparation of accurate
electromagnetic head models for EEG forward modeling.
It builds off of the seminal SimNIBS tool the field
modelling of transcranial magnetic stimulation (TMS) and
transcranial direct current stimulation. Human skin, skull,
cerebrospinal fluid, and brain meshing pipelines have been
rewritten with Nipype to ease access parallel processing
and to allow users to start/stop the workflows. 
Conductivity tensor mapping from diffusion-weighted 
imaging is also included.

%if %{with python3}
%package     -n 
Summary:        

%description -n 

%endif # with python3


%prep
%setup -qc
mv %{name}-%{version} python2

%if %{with python3}
cp -a python2 python3
%endif # with python3


%build
pushd python2
# Remove CFLAGS=... for noarch packages (unneeded)
#CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build
%py2_build
popd

%if %{with python3}
pushd python3
# Remove CFLAGS=... for noarch packages (unneeded)
#CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
%py3_build
popd
%endif # with python3


%install
rm -rf $RPM_BUILD_ROOT
# Must do the python3 install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if %{with python3}
pushd python3
#%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%py3_install
popd
%endif # with python3

pushd python2
#%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
py2_install
popd


%check
pushd python2
%{__python2} setup.py test
popd

%if %{with python3}
pushd python3
%{__python2} setup.py test
popd
%endif


%files
%doc
# For noarch packages: sitelib
%{python2_sitelib}/*
# For arch-specific packages: sitearch
%{python2_sitearch}/*

%if %{with python3}
%files -n 
%doc
# For noarch packages: sitelib
%{python3_sitelib}/*
# For arch-specific packages: sitearch
%{python3_sitearch}/*
%endif # with python3


%changelog
* Wed Nov  4 2015 Adrian Alves <alvesadrian@fedoraproject.org> 0.1-1
- Initial Build
