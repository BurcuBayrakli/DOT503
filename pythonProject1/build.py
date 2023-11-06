import subprocess

def run_tests():
    subprocess.run(["pytest"])

def build_package():
    subprocess.run(["python", "setup.py", "bdist_wheel"])

if __name__ == "__main__":
    run_tests()
    build_package()