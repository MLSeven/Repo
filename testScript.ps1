write-host "This is testCsript.ps1 from my Test Integration Repo"
$h = Get-Host | convertto-json -depth 5

$h
