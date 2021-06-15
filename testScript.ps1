# Standard PS header (Updated)
$ScriptEnv = [PSCustomObject]@{
    Name = $MyInvocation.MyCommand.Name;
    Instance = "<%=instance.name%>"; 
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
