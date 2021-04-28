# Standard PS header
$ScriptEnv = [PSCustomObject]@{
    Name = $MyInvocation.MyCommand.Name;
    Root = $PSScriptRoot;
    Path = $PSCommandPath;
    isWindows = $IsWindows;
    isLinux = $IsLinux;
    isMacOS = $IsMacOS;
    isCoreCLR = $ISCoreCLR;
    commandType = $MyInvocation.MyCommand.CommandType.ToString();
    my=$MyInvocation.MyCommand;
}

$ScriptEnv | convertto-json -depth 5
