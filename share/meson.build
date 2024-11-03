deps += custom_target(
    'download winget',
    command: [
        py3,
        download_script,
        'https://github.com/microsoft/winget-cli/releases/download/v1.8.1911/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle',
        '@OUTPUT@',
    ],
    output: 'Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle',
)

deps += custom_target(
    'download VCLibs',
    command: [
        py3,
        download_script,
        'https://aka.ms/Microsoft.VCLibs.x64.14.00.Desktop.appx',
        '@OUTPUT@',
    ],
    output: 'Microsoft.VCLibs.x64.14.00.Desktop.appx',
)

microsoft_ui_xaml_zip = custom_target(
    'download microsoft.ui.xaml',
    command: [
        py3,
        download_script,
        'https://www.nuget.org/api/v2/package/Microsoft.UI.Xaml/2.8.6',
        '@OUTPUT@',
    ],
    output: 'microsoft.ui.xaml.2.8.6.zip',
)

deps += custom_target(
    'unzip microsoft.ui.xaml',
    command: [
        py3,
        extract_script,
        '@INPUT@',
        '@OUTDIR@',
        'tools/AppX/x64/Release/Microsoft.UI.Xaml.2.8.appx',
    ],
    input: microsoft_ui_xaml_zip,
    output: 'Microsoft.UI.Xaml.2.8.appx',
)

depend_files += configure_file(
    input: 'install.ps1',
    output: 'install.ps1',
    copy: true,
)
