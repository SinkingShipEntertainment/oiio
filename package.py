name = "oiio"

version = "2.5.9.0.sse.1.0.0"

description = \
    """
    OpenImageIO is a library for reading and writing images, and a bunch of related
    classes, utilities, and applications.
    """

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
    "libtiff",
    "libjpeg",
    "libpng",
    "pybind11",
    "tbb",
    "numpy",
    "ffmpeg",
    "boost-1.76",
    "openexr-3.1.12",
    "openvdb-9.1.0",
    "ocio-2.1.3",  # build of OCIO without CLI tools (without OIIO as dependency)
]

private_build_requires = [
]

variants = [
    ["python-3.7"],
    ["python-3.9"],
]

build_system = "cmake"
uuid = "repository.oiio"

# Pass cmake arguments to the REZ build system:
# rez-build -i -- -DSTOP_ON_WARNING=OFF -DBoost_NO_BOOST_CMAKE=On -DBoost_NO_SYSTEM_PATHS=True
# rez-release -- -DSTOP_ON_WARNING=OFF -DBoost_NO_BOOST_CMAKE=On -DBoost_NO_SYSTEM_PATHS=True

def pre_build_commands():

    info = {}
    with open("/etc/os-release", 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line_info = line.replace('\n', '').split('=')
            if len(line_info) != 2:
                continue
            info[line_info[0]] = line_info[1].replace('"', '')
    linux_distro = info.get("NAME", "centos")
    print("Using Linux distro: " + linux_distro)

    if linux_distro.lower().startswith("centos"):
        command("source /opt/rh/devtoolset-6/enable")
    elif linux_distro.lower().startswith("rocky"):
        pass

def commands():
    env.OIIO_LOCATION = "{root}"
    env.OIIO_ROOT = "{root}"
    env.OIIO_INCLUDE_DIR = "{root}/include"
    env.OIIO_LIBRARY_DIR = "{root}/lib64"

    env.PATH.append("{root}/bin")

    env.OPENIMAGEIOHOME = "{root}"  # For OpenShadingLanguage to find it
    env.OPENIMAGEIO_ROOT_DIR = "{root}"  # For OpenColorIO to find it

    env.LD_LIBRARY_PATH.prepend("{root}/lib64")

    python_ver = resolve["python"].version
    if python_ver.major == 3:
        if python_ver.minor == 7:
            env.PYTHONPATH.append("{root}/lib64/python3.7/site-packages")
        elif python_ver.minor == 9:
            env.PYTHONPATH.append("{root}/lib64/python3.9/site-packages")
