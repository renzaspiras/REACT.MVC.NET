# Using `REACT.MVC.NET.py` Script

This Python script automates the creation of a .NET MVC project alongside a Vite React project, and includes a `build.py` script for building and running both projects. Follow the steps below to use the script effectively.

## Prerequisites

1. **Python Installation**: Ensure Python is installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

2. **Node.js and npm**: Ensure Node.js and npm are installed on your system. You can download them from [nodejs.org](https://nodejs.org/).

3. **Dotnet CLI**: Ensure dotnet CLI is installed on your system. You can download it from [dotnet.microsoft.com](https://dotnet.microsoft.com/download).

## Running the Script

1. **Clone or Download the Script**: Obtain the `REACT.MVC.NET.py` script from your repository or download it from the source.

2. **Open Terminal or Command Prompt**: Navigate to the directory containing `REACT.MVC.NET.py`.

3. **Execute the Script**: Run the script by entering the following command:

   ```bash
   python REACT.MVC.NET.py
   ```

4. **Follow the Prompts**:
   - Enter the desired project name when prompted.
   - The script will then proceed to:
     - Create a `.NET MVC` project named `projectname.MVC`.
     - Create a `Vite React` project named `projectname.REACT`.
     - Generate a `build.py` script for building and running the projects.

## How It Works

The `REACT.MVC.NET.py` script automates the following tasks:

### 1. .NET MVC Project Creation

- **Project Initialization**: Uses `dotnet new mvc` command to create a .NET MVC project named `projectname.MVC`.

- **Solution File**: Creates a solution file (`projectname.MVC.sln`) and adds the MVC project to it using `dotnet new sln` and `dotnet sln add` commands.

- **File Management**: Removes unnecessary `Program.cs` and `wwwroot` directory if it exists, then recreates `wwwroot` to prepare for the React build.

### 2. Vite React Project Creation

- **Project Initialization**: Uses `npm init vite@latest` command to create a Vite React project named `projectname.REACT` with the React template.

- **Dependencies Installation**: Installs necessary dependencies and builds the Vite React project using `npm install` and `npm run build`.

- **Build Integration**: Copies the built React project (`dist` directory) into the `.NET MVC` project's `wwwroot` directory.

### 3. `build.py` Script Generation

- **Python Script**: Generates a `build.py` script that automates the build and deployment process of both projects.

- **Build Automation**: Provides functions to change directory, build the Vite React project, and copy the build output to the `.NET MVC` project's `wwwroot`.

## Using `build.py`

The `build.py` script facilitates building and running both projects (`projectname.MVC` and `projectname.REACT`):

1. **Navigate to Project Directory**: Open a terminal and navigate to the directory containing `build.py`.

2. **Execute the Script**: Run the script by entering the following command:

   ```bash
   python build.py
   ```

3. **Automated Tasks**: The script automates:
   - Changing directory to the React project (`projectname.REACT`).
   - Building the Vite React project.
   - Copying the built React files (`dist` directory) to the `.NET MVC` project's `wwwroot` directory.

## Additional Notes

- **Error Handling**: If any errors occur during script execution, detailed error messages will be displayed in the terminal.

- **Customization**: Feel free to modify `REACT.MVC.NET.py` or `build.py` scripts to suit additional project requirements or customization needs.

---

This README provides a comprehensive guide on using `REACT.MVC.NET.py` to automate the creation and integration of a .NET MVC project with a Vite React project. Ensure all prerequisites are met and follow the outlined steps for seamless project creation, integration, and deployment. Adjustments can be made based on specific project requirements or preferences.
