import os
import subprocess

def run_script(script_name):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, script_name)

    try:
        subprocess.check_call(['python', script_path])
        print(f'{script_name} 已成功执行')
    except subprocess.CalledProcessError as e:
        print(f'在执行 {script_name} 时出错')
        exit(1)

def run_command(command):
    try:
        subprocess.check_call(command, shell=True)
        print(f'命令 {command} 已成功执行')
    except subprocess.CalledProcessError as e:
        print(f'在执行命令 {command} 时出错')
        exit(1)

if __name__ == "__main__":
    step_list = [("开始", None), 
                 ("第一步", 'py/genalgolia.py'), 
                 ("第二步", 'hugo'), 
                 ("第三步", 'py/update.py'), 
                 ("结束", None)]

    for step, command in step_list:
        print("=========={}==========".format(step))
        if command:
            if command.endswith('.py'):
                run_script(command)
            else:
                run_command(command)