@echo off

REM Get the IP address of the wireless network interface
for /f "tokens=" %%i in ('powershell -Command "Get-NetIPAddress -InterfaceAlias 'Wi-Fi' | Where-Object IPAddress -like '...*' | Select-Object -ExpandProperty IPAddress"') do set "ip_address=%%i"

REM Update the .env file with the IP address
powershell -Command "(Get-Content .env) -replace 'EXPO_PUBLIC_BASE_URL=.*', 'EXPO_PUBLIC_BASE_URL=http://%ip_address%:8000' | Set-Content .env"