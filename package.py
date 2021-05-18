name = "oiio"

version = "1.8.9"

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
    "gcc-6.3.0",
    "libtiff-4.0.7",
    "libpng-1.6.37",
    "libjpeg-9.2",
    "openexr-2.2.0",
    "ocio-1.0.9",
    "ptex-2.1.28",
]

private_build_requires = [
    "cmake",
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-2.7", "boost-1.70.0"]
]

build_system = "cmake"

uuid = "repository.oiio"

def commands():
    env.OIIO_LOCATION = "{root}"
    env.OIIO_ROOT = "{root}"
    env.OIIO_INCLUDE_DIR = "{root}/include"
    env.OIIO_LIBRARY_DIR = "{root}/lib64"
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
    env.PATH.append("{root}/bin")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/rez_cmake")
