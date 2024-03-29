import sys

from . import (
    bdist_dumb as bdist_dumb,
    bdist_rpm as bdist_rpm,
    build as build,
    build_clib as build_clib,
    build_ext as build_ext,
    build_py as build_py,
    build_scripts as build_scripts,
    check as check,
    clean as clean,
    install as install,
    install_data as install_data,
    install_headers as install_headers,
    install_lib as install_lib,
    register as register,
    sdist as sdist,
    upload as upload,
)

if sys.version_info < (3, 10):
    from . import bdist_wininst as bdist_wininst

__all__ = [
    "build",
    "build_py",
    "build_ext",
    "build_clib",
    "build_scripts",
    "clean",
    "install",
    "install_lib",
    "install_headers",
    "install_scripts",
    "install_data",
    "sdist",
    "register",
    "bdist",
    "bdist_dumb",
    "bdist_rpm",
    "bdist_wininst",
    "check",
    "upload",
]
