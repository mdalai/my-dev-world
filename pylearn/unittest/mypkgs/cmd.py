import subprocess
import sys

def run_cmd_return_output(cmd, args):
    #command = f"{cmd} {' '.join(str(arg) if ' ' not in arg else arg.replace(' ','\ ') for arg in args)}"
    command = "{} {}".format(cmd, " ".join(str(arg) if ' ' not in arg else arg.replace(' ','\ ') for arg in args))
    print(command)
    proc = subprocess.Popen(command, shell=True, 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.STDOUT, universal_newlines=True)

    # while True:
    #     #nextline = proc.stdout.readline().decode('UTF-8')
    #     nextline = proc.stdout.readline()
    #     if nextline == '' and proc.poll() is not None:
    #         break
    #     sys.stdout.write(nextline)
    #     sys.stdout.flush()

    output = proc.communicate()[0]
    exit_code = proc.returncode

    if (exit_code == 0):
        return output.rstrip()
    else:
        raise Exception(cmd, exit_code, output)
        #raise ValueError("ERROR")


def main():
    #out = run_cmd_return_output('uname', args=['-srm'])
    out = run_cmd_return_output('hostnamectl', args=[])
    print('-'*50)
    print(out)
    print('-'*50)


if __name__ == "__main__":
    main()
