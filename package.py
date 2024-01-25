name = "oiio"

version = "2.3.15.0.sse.2.0.0"

description = \
    """
    OpenImageIO is a library for reading and writing images, and a bunch of related
    classes, utilities, and applications.
    """

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
    "libtiff-4.0.7",
    "libjpeg-9.2",
    "libpng-1.6.29",
    "libraw",
    "pybind11",
    "numpy",
    "openexr-3.1.5",
    "openvdb-9.1.0",
    "qtbase-5.14.1",
    "ocio-2.1.1",  # build of OCIO without OIIO
]

private_build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-3.7", "tbb-2019.6", "boost-1.76", "ptex"],
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-3.7", "tbb-2019.6", "boost-1.76", "!ptex"],
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-3.9", "tbb-2019.6", "boost-1.76", "ptex"],
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-3.9", "tbb-2019.6", "boost-1.76", "!ptex"],
]

build_system = "cmake"

uuid = "repository.oiio"

# Pass cmake arguments to the REZ build system:
# rez-build -i -- -DSTOP_ON_WARNING=OFF -DBoost_NO_BOOST_CMAKE=On -DBoost_NO_SYSTEM_PATHS=True
# rez-release -- -DSTOP_ON_WARNING=OFF -DBoost_NO_BOOST_CMAKE=On -DBoost_NO_SYSTEM_PATHS=True

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.OIIO_LOCATION = "{root}"
    env.OIIO_ROOT = "{root}"
    env.OIIO_INCLUDE_DIR = "{root}/include"
    env.OIIO_LIBRARY_DIR = "{root}/lib64"

    env.PATH.append("{root}/bin")

    env.OPENIMAGEIOHOME = "{root}"  # For OpenShadingLanguage to find it
    env.OPENIMAGEIO_ROOT_DIR = "{root}"  # For OpenColorIO to find it

    env.LD_LIBRARY_PATH.prepend("{root}/lib64")

    if "python" in resolve:
        python_ver = resolve["python"].version
        if python_ver.major == 3:
            if python_ver.minor == 7:
                env.PYTHONPATH.append("{root}/lib64/python3.7/site-packages")
            elif python_ver.minor == 9:
                env.PYTHONPATH.append("{root}/lib64/python3.9/site-packages")
