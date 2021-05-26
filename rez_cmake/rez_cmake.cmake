
# FindTIFF
set(TIFF_INCLUDE_DIR $ENV{REZ_LIBTIFF_ROOT}/include)
set(TIFF_LIBRARY $ENV{REZ_LIBTIFF_ROOT}/lib/libtiff.so)

# FindPNG
set(PNG_PNG_INCLUDE_DIR $ENV{REZ_LIBPNG_ROOT}/include)
set(PNG_LIBRARY $ENV{REZ_LIBPNG_ROOT}/lib64/libpng16.so)

# FindJPEG
set(JPEG_INCLUDE_DIR $ENV{REZ_LIBJPEG_ROOT}/include)
set(JPEG_LIBRARY $ENV{REZ_LIBJPEG_ROOT}/lib/libjpeg.so)

# FindOpenEXR
set(OPENEXR_HOME $ENV{REZ_OPENEXR_ROOT})

# FindOCIO
set(OCIO_PATH $ENV{REZ_OCIO_ROOT})
set(OpenColorIO_ROOT $ENV{REZ_OCIO_ROOT})

# FindOpenVDB
set(OpenVDB_ROOT $ENV{REZ_OPENVDB_ROOT})

# Set which python version to look for
set(REZ_BUILD_WITH_PYTHON_VERSION "2.7")
if($ENV{REZ_PYTHON_VERSION} EQUAL "3.7.7")
    set(REZ_BUILD_WITH_PYTHON_VERSION "3.7")
endif()

# FindBoost and FindPython
set(BOOST_CUSTOM 1)
set(Boost_VERSION 1.70)
set(BOOST_ROOT $ENV{REZ_BOOST_ROOT})
set(Boost_INCLUDE_DIRS $ENV{BOOST_INCLUDEDIR})
set(Boost_LIBRARY_DIRS $ENV{BOOST_LIBRARYDIR})
set(Boost_PYTHON_LIBRARIES $ENV{REZ_BOOST_ROOT}/lib)
set(Boost_LIBRARIES
    $ENV{REZ_BOOST_ROOT}/lib/libboost_filesystem.so
    $ENV{REZ_BOOST_ROOT}/lib/libboost_system.so
    $ENV{REZ_BOOST_ROOT}/lib/libboost_thread.so)
set(Boost_PYTHON27_LIBRARIES
    $ENV{REZ_BOOST_ROOT}/lib/libboost_python27.so)
set(Boost_PYTHON37_LIBRARIES
    $ENV{REZ_BOOST_ROOT}/lib/libboost_python37.so)
