# Standard PS header
$ScriptEnv = [PSCustomObject]@{
    Name = $MyInvocation.Command.Name;
    Root = $PSScriptRoot;
    Path = $PSCommandPath;
    isWindows = $IsWindows;
    isLinux = $IsLinux;
    isMacOS = $IsMacOS;
    isCoreCLR = $ISCoreCLR;
    isScriptBlock = ($MyInvocation.ScriptBlock -ne $null)
}

$ScriptEnv | convertto-json
