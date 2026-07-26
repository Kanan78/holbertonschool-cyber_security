$action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-ExecutionPolicy Bypass -WindowStyle Hidden -File C:\Users\Public\monitor.ps1"
$trigger = New-ScheduledTaskTrigger -AtLogOn
Register-ScheduledTask -TaskName "SystemBITSMonitor" -Action $action -Trigger $trigger -User "SYSTEM"
