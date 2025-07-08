$default = "Y"
Write-Host "IF YOU DOESNT RUNNED PWSH WITH ADMIN IT WILL NOT WORK!"
$response = Read-Host "Do you want to continue? [Y/N] (default: $default)"
if ([string]::IsNullOrWhiteSpace($response)) { $response = $default }

if ($response.ToUpper() -eq "Y") {
    Write-Host "Proceeding..."
    pip install pyinstaller
    pyinstaller --onefile easyhost.py 
    Copy-Item -Path "dist/easyhost.exe" -Destination "C:\Windows\System32\"
    Write-Host "Just type 'easyhost'"
} else {
    Write-Host "Operation cancelled"
}