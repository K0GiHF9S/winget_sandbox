project(
    'sandbox',
    meson_version: '>=1.4.0',
)

py3 = import('python').find_installation(pure: false)

configure = configure_file(
    input: 'sandbox.wsb.in',
    output: 'sandbox.wsb',
    configuration: {'current_path': meson.project_build_root()},
)

download_script = configure_file(
    input: 'download.py',
    output: 'download.py',
    copy: true,
)

extract_script = configure_file(
    input: 'extract.py',
    output: 'extract.py',
    copy: true,
)

deps = []
depend_files = [configure]
subdir('share')

custom_target(
    'run wsb',
    command: ['powershell', '-NoProfile', configure.full_path()],
    output: 'dummy',
    depend_files: depend_files,
    depends: deps,
    build_by_default: true,
)
