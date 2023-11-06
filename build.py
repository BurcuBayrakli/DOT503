import subprocess
import sys
import os

# Define your project name and version
project_name = "calculator"
project_version = "1.0.0"

# Define a function to run shell commands
def run_command(command, cwd=None):
    try:
        subprocess.check_call(command, shell=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)

# Clean previous build artifacts
print("Cleaning previous build artifacts...")
run_command("rm -rf build dist", cwd=os.path.dirname(__file__))

# Run tests using pytest (modify the test command as needed)
print("Running tests...")
test_command = "pytest"
run_command(test_command)

# Build source distribution and wheel
print("Building source distribution and wheel...")
build_command = f"python setup.py sdist bdist_wheel"
run_command(build_command)

# Output distribution files to the 'dist' directory
print("Distribution files are located in the 'dist' directory.")

# You can add more build steps here if needed

# Optionally, you can create a standalone executable (e.g., with pyinstaller)
# executable_command = f"pyinstaller your_script.py --onefile"
# run_command(executable_command)

# Provide instructions for packaging

print("\nPackage build complete.")
print(f"Your package name: {project_name}")
print(f"Version: {project_version}")
print("You can now distribute the package or executable as needed.")
