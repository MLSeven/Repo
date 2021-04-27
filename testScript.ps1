# Test Powershell after branch rename
$ScriptFile = Get-Item $myinvocation.Mycommand.Path
$ScriptRoot = Split-Path -Path $myinvocation.Mycommand.Path -Parent
$ScriptName = $ScriptFile.BaseName
$subScript = join-path -path $ScriptRoot -ChildPath "Scripts" 


$data = [PSCustomObject]@{Fullname=$ScriptFile.fullname; Root=$ScriptRoot; Name=$ScriptName; subScripts = $subScript; subfile=""}

$psFile1 = join-path -path $subScript -ChildPath "SubFile2.ps1"

if (test-path -path $psFile1) {
    $exit = invoke-expression $psFile1
}
write-host $exit
$data.subfile=$psFile1
$data | convertto-json
