@echo off
meson setup builddir --reconfigure
meson compile -C builddir
