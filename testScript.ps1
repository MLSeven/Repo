# Test Poerrshell

$proc =  get-process -Id $pid

$json = $proc | convertto-json -depth 5
$json