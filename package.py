name = "oiio"

version = "2.3.8.0"

description = \
    """
    OpenImageIO is a library for reading and writing images, and a bunch of related
    classes, utilities, and applications.
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
    "tbb-2017.6",
    "openexr-2.4.0",
    "libtiff-4.0.7",
    "libjpeg-9.2",
    "libpng-1.6.29",
    "qtbase-5.15.2",
]

private_build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7", "boost-1.70.0"],
]

build_system = "cmake"

uuid = "repository.oiio"

# Pass cmake arguments to the REZ build system:
# rez-build -i -- -DUSE_PYTHON=OFF -DSTOP_ON_WARNING=OFF -DBoost_NO_BOOST_CMAKE=On -DBoost_NO_SYSTEM_PATHS=True
# rez-release -- -DUSE_PYTHON=OFF -DSTOP_ON_WARNING=OFF -DBoost_NO_BOOST_CMAKE=On -DBoost_NO_SYSTEM_PATHS=True

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
