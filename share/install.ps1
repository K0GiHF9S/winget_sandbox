Set-Location $PSScriptRoot
Add-AppxPackage -Path Microsoft.VCLibs.x64.14.00.Desktop.appx
Add-AppxPackage -Path Microsoft.UI.Xaml.2.8.appx

Add-AppxPackage -Path Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle

Out-File C:\Users\WDAGUtilityAccount\Desktop\install_completed
