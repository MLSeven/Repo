import sys
import argparse
import winrm
from getpass import getpass


def run_winrm(endpoint,user,password,task):

    remotehost = f"http://{endpoint}:5985/wsman"

    print(f"Remote host {remotehost}")
    print(f"Connecting as User {user}")

    pwsh = """ 
        $PSSenderInfo | convertto-json
        $git=Invoke-Webrequest -Uri "https://raw.githubusercontent.com/MLSeven/Gitstuff/main/PShell/tasktools.ps1" -UseBasicParsing
        invoke-expression $git.content
        Get-TaskInfo -AsJson
    """

    powershell_session = winrm.Session(remotehost,auth=(user,password), transport='ntlm')

    # force protocol to accept unsigned certs

    p = winrm.Protocol(
        endpoint=remotehost,
        transport='ntlm',           
        username=user,
        password=password,
        server_cert_validation='ignore')

    powershell_session.protocol = p

    try:
        run_ps = powershell_session.run_ps(pwsh)
    except Exception as err:
        print(f"winRm Exception {err}")
        sys.exit(1)

    exit_code = run_ps.status_code
    print(f"Powershell exit code {exit_code}")
    error_value = run_ps.std_err
    output = run_ps.std_out
    error_value = error_value.decode('utf-8')
    output = output.decode('utf-8')

    if exit_code != 0:
        raise Exception('An error occurred in the PowerShell script, see logging for more info')
    print(len(output))
    return output


# when run from Command like get the args
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run a Powershell command or scriptblock on a remote server')
    parser.add_argument('--endpoint', help='the remote server') 
    parser.add_argument('--user', '-u', help='the Remote username')
    parser.add_argument('--password', '-p',required=False, help='The password - will prompt if ommitted')

    parser.add_argument('--version', '-v', action='version', version='%(prog)s verison 1.0')
    args = parser.parse_args()
    if not args.password:
        args.password=getpass()
    
    output = run_winrm(args.endpoint,args.user,args.password,"")
    print(output)