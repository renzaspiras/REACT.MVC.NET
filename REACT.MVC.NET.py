import shutil
import os
import subprocess

def main():
    try:
        # Get project name from user input
        command = input("Project Name: ").strip()

        # Create .NET MVC project
        execute_command(f"dotnet new mvc -n {command}.MVC")

        # Create solution file and add project to it
        execute_command(f"dotnet new sln -n {command}.MVC -o ./{command}.MVC")
        execute_command(f"dotnet sln ./{command}.MVC/{command}.MVC.sln add ./{command}.MVC/{command}.MVC.csproj")

        # Remove default Program.cs (assuming it's not needed)
        execute_command(f"rm ./{command}.MVC/Program.cs")

        # Remove wwwroot directory if it exists
        wwwroot_dir = f"./{command}.MVC/wwwroot"
        if os.path.exists(wwwroot_dir):
            shutil.rmtree(wwwroot_dir)

        # Ensure wwwroot directory is recreated
        os.makedirs(wwwroot_dir, exist_ok=True)

        # Generate dotnet_template.cs script
        generate_dotnet_template(command)

        # Create Vite React project
        create_vite_project(command)

        # Copy built files to .NET MVC project
        copy_vite_build_to_mvc(command)

        print("Build and deployment completed successfully.")

        # Write additional Python script (build.py)
        write_additional_script(command)

    except Exception as e:
        print(f"Error occurred: {e}")

def execute_command(command):
    try:
        # Execute shell command directly
        subprocess.run(command, shell=True, check=True)
        print(f"Command executed successfully: {command}")
    except Exception as e:
        print(f"Error executing command: {command}")
        print(e)

def generate_dotnet_template(command):
    template = f"""
public class Program
{{
    public static void Main(string[] args)
    {{
        var builder = WebApplication.CreateBuilder(args);

        // Add services to the container.
        builder.Services.AddControllersWithViews();

        var app = builder.Build();

        // Configure the HTTP request pipeline.
        if (!app.Environment.IsDevelopment())
        {{
            app.UseExceptionHandler("/Home/Error");
            // The default HSTS value is 30 days. You may want to change this for production scenarios.
            app.UseHsts();
        }}

        app.UseHttpsRedirection();
        app.UseStaticFiles(); // Enable serving static files from wwwroot

        app.UseRouting();

        app.UseAuthorization();

        // Map controller endpoints
        app.MapControllers();

        // Configure endpoint for default index.html file
        app.MapGet("/", async context =>
        {{
            context.Response.ContentType = "text/html";
            await context.Response.SendFileAsync(Path.Combine(app.Environment.ContentRootPath, "wwwroot", "index.html"));
        }});

        app.Run();
    }}
}}
"""
    file_path = f"./{command}.MVC/Program.cs"
    try:
        with open(file_path, 'w') as file:
            file.write(template)
        print(f"Generated Program.cs successfully at {file_path}.")
    except Exception as e:
        print(f"Error generating Program.cs: {e}")

def create_vite_project(command):
    try:
        # Create Vite project using npm
        execute_command(f"npm init vite@latest {command}.REACT -- --template react")
        print(f"Vite project {command}.REACT created successfully.")
    except Exception as e:
        print(f"Error creating Vite project: {e}")

def copy_vite_build_to_mvc(command):
    try:
        # Install dependencies and build Vite project
        os.chdir(f"{command}.REACT")
        execute_command("npm install")
        execute_command("npm run build")

        # Copy built files to .NET MVC project
        os.chdir("../")
        source_dir = f"./{command}.REACT/dist/"
        destination_dir = f"./{command}.MVC/wwwroot/"

        # Ensure destination directory exists
        os.makedirs(destination_dir, exist_ok=True)

        # Copy entire contents of source_dir to destination_dir
        shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)

        print("Files copied successfully.")
    except Exception as e:
        print(f"Error copying files to .NET MVC project: {e}")

def write_additional_script(command):
    try:
        # Write additional script to build.py
        with open("build.py", 'w') as f:
            paragraph = f"""
import shutil
import os
import subprocess

def main():
    try:
        # Change directory to REACT
        react_dir = os.path.join(os.getcwd(), "{command}.REACT")
        os.chdir(react_dir)

        # Build Vite React project
        build_vite_react_project()

        # Copy Vite React build to .NET MVC wwwroot
        copy_vite_build_to_mvc("{command}")

        print("Build and deployment completed successfully.")
        
        os.chdir(f"./{command}.MVC")
        os.system("dotnet run")

    except Exception as e:
        print(f"Error occurred during build and deployment")

def build_vite_react_project():
    try:
        # Run npm build command in REACT directory
        execute_command("npm install")
        execute_command("npm run build")

        print("Vite React project built successfully.")

    except Exception as e:
        print(f"Error building Vite React project")

def copy_vite_build_to_mvc(command):
    try:
        # Change directory back to the original directory (where the script was executed)
        os.chdir("..")

        # Define source and destination directories
        source_dir = os.path.join(os.getcwd(), f"{command}.REACT", "dist")
        destination_dir = os.path.join(os.getcwd(), f"{command}.MVC", "wwwroot")

        # Ensure destination directory exists
        os.makedirs(destination_dir, exist_ok=True)

        # Copy contents of source_dir to destination_dir
        shutil.rmtree(destination_dir)  # Clear existing wwwroot contents
        shutil.copytree(source_dir, destination_dir)

        print(f"Vite React build copied to {command}.MVC/wwwroot successfully.")
    except Exception as e:
        print(f"Error copying Vite React build to .NET MVC project")

def execute_command(command):
    try:
        # Execute shell command
        subprocess.run(command, shell=True, check=True)
        print(f"Command executed successfully: {command}")
    except Exception as e:
        print(f"Error executing command: {command}")
        print(e)

if __name__ == "__main__":
    main()
"""
            f.write(paragraph.strip() + "\n")

        print("build.py generated successfully.")

    except Exception as e:
        print(f"Error writing build.py")

if __name__ == "__main__":
    main()
