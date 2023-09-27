import subprocess


def run_script(script_name):
    print(f"! ! ! Starting {script_name} ! ! !")
    subprocess.run(["python", script_name])
    print(f"! ! ! {script_name} Completed ! ! !\n")


def main():
    run_script("data_loader.py")
    run_script("question_1.py")
    run_script("question_2.py")
    print("! ! ! All Tasks Completed ! ! !")


if __name__ == "__main__":
    main()
