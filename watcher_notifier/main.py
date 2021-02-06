
import subprocess
import threading
import time
import pyinotify
import sys

def run_cmd():
    print("Run cmd")

def spawn_cmd_and_call_func_on_exit(cmd_args, func_on_exit):
    def run_in_thread(cmd_args, func_on_exit):
        proc = subprocess.Popen(cmd_args)
        proc.wait()
        func_on_exit()
        return
    thread = threading.Thread(target=run_in_thread, args=(cmd_args, func_on_exit))
    thread.start()
    # returns immediately after the thread starts
    return thread

def spawn_process(cmd_in_arr):
    subprocess.Popen(cmd_in_arr)

def run_cmd_fg(cmd_in_arr):
    proc = subprocess.Popen(cmd_in_arr, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = proc.communicate()
    if proc.returncode:
        raise str(err)
    else:
        return output.rstrip()



def runCommandHelloBlock(ev):
    '''Runs <my_cmd> by blocking other processes to start
    TODO:  not sure how to pass <my_cmd> as an arg.
    '''
    my_cmd = ['/bin/echo', 'File', ev.pathname, 'changed']
    print("Running [{}] by blocking other processes".format(my_cmd))
    subprocess.Popen(my_cmd).communicate()

    # this stops pyinotify notifier loop, but not sure if this is right way of doing it
    #sys.exit(0)


def watch_afile_trigger_afunc_nonstop(filepath_to_watch, event, func):
    """Watch a <filepath_to_watch> on <event>, trigger a <func> if event occurs
    This continues foreever until force to stop by (CTRL+C)
    """
    if event.upper() in 'DELETE':
        pyevent = pyinotify.IN_DELETE
    if event.upper() in 'MODIFY':
        pyevent = pyinotify.IN_MODIFY
    wm = pyinotify.WatchManager()
    wm.add_watch(filepath_to_watch, pyevent, proc_fun=func)
    notifier = pyinotify.Notifier(wm)
    notifier.loop()



def runCommandAndStopNotifierLoop(notifier):
    '''
    IF the event occurs, run <my_cmd> and stop the notifier loop
    '''
    my_cmd = ['/bin/echo', 'DO SOMETHING']      
    print("notifier <{}> is looping...".format(notifier))
    if notifier.check_events():
        print("The event is occurred")
        print("Running [{}] by blocking other processes".format(my_cmd))
        subprocess.Popen(my_cmd).communicate()

        # stop: is not necessary because <return True> will do that        
        #notifier.stop()

        # following return will stop the notifier loop        
        return True


def watch_afile_trigger_afunc_stop(filepath_to_watch, event, callback_func):
    """Watch a <filepath_to_watch> on <event>, trigger a <func> if event occurs
    Stop/Exit whenever the <event> occurs
    """
    if event.upper() in 'DELETE':
        pyevent = pyinotify.IN_DELETE
    if event.upper() in 'MODIFY':
        pyevent = pyinotify.IN_MODIFY
    wm = pyinotify.WatchManager()
    wm.add_watch(filepath_to_watch, pyevent)
    notifier = pyinotify.Notifier(wm)
    notifier.loop(callback=callback_func)

    


def main():
    my_cmd = ('sleep', '10')
    #spawn_process(my_cmd)
    #spawn_cmd_and_call_func_on_exit(my_cmd, run_cmd)

    cmd = ('./test.sh')
    cmd = ('echo', 'bash-hello',)
    ret_val = run_cmd_fg(cmd)
    print(ret_val)

    afile = '/tmp/test.file.txt'
    #watch_afile_trigger_afunc_nonstop(afile, 'MODIFY', runCommandHelloBlock)
    watch_afile_trigger_afunc_stop(afile, 'DELETE', runCommandAndStopNotifierLoop)


    print("END")


if __name__ == '__main__':
    main()