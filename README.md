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

## Project Structure

Upon successful execution, the script will create the following directory structure:

```
projectname.MVC/
│   projectname.MVC.csproj
│   Program.cs
│   ...
│
projectname.REACT/
│   node_modules/
│   public/
│   src/
│   ...
│
build.py
```

## Using `build.py`

The `build.py` script is generated to assist with building and running the projects. Here’s how to use it:

1. **Navigate to Project Directory**: Open a terminal and navigate to the directory containing `build.py`.

2. **Execute the Script**: Run the script by entering the following command:

   ```bash
   python build.py
   ```

3. **Follow the Instructions**: The script will guide you through building and running both projects (`projectname.MVC` and `projectname.REACT`).

## Additional Notes

- **Error Handling**: If any errors occur during script execution, detailed error messages will be displayed in the terminal.

- **Customization**: Feel free to modify `REACT.MVC.NET.py` or `build.py` scripts to suit additional project requirements or customization needs.

---

This README provides a comprehensive guide on using `REACT.MVC.NET.py` to generate and manage your .NET MVC and Vite React projects. Ensure all prerequisites are met and follow the outlined steps for seamless project creation and execution. Adjustments can be made based on specific project requirements or preferences.
