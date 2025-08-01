#!/usr/bin/env python3
"""
Project Scaffolding and Templates for CCPlugins MCP Server
"""

import os
import shutil
from pathlib import Path
from typing import Dict, List, Optional
import json

class ProjectScaffolder:
    def __init__(self):
        self.templates_dir = Path(__file__).parent.parent / "templates"
        self.templates_dir.mkdir(exist_ok=True)
        self._init_default_templates()
    
    def _init_default_templates(self):
        """Initialize default project templates"""
        templates = {
            "python-cli": self._python_cli_template,
            "web-app": self._web_app_template,
            "api-service": self._api_service_template,
            "claude-plugin": self._claude_plugin_template
        }
        
        for template_name, template_func in templates.items():
            template_dir = self.templates_dir / template_name
            if not template_dir.exists():
                template_func(template_dir)
    
    def get_available_templates(self) -> List[Dict]:
        """Get list of available templates"""
        templates = []
        for template_dir in self.templates_dir.iterdir():
            if template_dir.is_dir():
                config_file = template_dir / "template.json"
                if config_file.exists():
                    try:
                        with open(config_file, 'r') as f:
                            config = json.load(f)
                        templates.append({
                            "name": template_dir.name,
                            "description": config.get("description", "No description"),
                            "category": config.get("category", "general"),
                            "variables": config.get("variables", [])
                        })
                    except:
                        # Fallback for templates without config
                        templates.append({
                            "name": template_dir.name,
                            "description": f"{template_dir.name} template",
                            "category": "general",
                            "variables": []
                        })
        return templates
    
    async def scaffold_project(self, template_name: str, project_name: str, 
                              target_dir: str, options: Dict = None) -> Dict:
        """Generate project from template"""
        if options is None:
            options = {}
        
        template_dir = self.templates_dir / template_name
        if not template_dir.exists():
            return {
                "success": False,
                "error": f"Template '{template_name}' not found"
            }
        
        target_path = Path(target_dir) / project_name
        if target_path.exists():
            return {
                "success": False,
                "error": f"Directory '{target_path}' already exists"
            }
        
        try:
            # Copy template files
            shutil.copytree(template_dir, target_path)
            
            # Process template variables
            variables = {
                "PROJECT_NAME": project_name,
                "PROJECT_NAME_SNAKE": project_name.lower().replace("-", "_"),
                "PROJECT_NAME_CAMEL": "".join(word.capitalize() for word in project_name.split("-")),
                **options
            }
            
            await self._process_template_files(target_path, variables)
            
            # Remove template.json from final project
            config_file = target_path / "template.json"
            if config_file.exists():
                config_file.unlink()
            
            return {
                "success": True,
                "path": str(target_path),
                "template": template_name,
                "variables_used": variables
            }
            
        except Exception as e:
            # Clean up on error
            if target_path.exists():
                shutil.rmtree(target_path)
            return {
                "success": False,
                "error": f"Error scaffolding project: {str(e)}"
            }
    
    async def _process_template_files(self, project_path: Path, variables: Dict):
        """Process template files and replace variables"""
        for file_path in project_path.rglob("*"):
            if file_path.is_file() and file_path.name != "template.json":
                try:
                    # Read file content
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    # Replace template variables
                    for var_name, var_value in variables.items():
                        placeholder = f"{{{{{var_name}}}}}"
                        content = content.replace(placeholder, str(var_value))
                    
                    # Write back
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                        
                except (UnicodeDecodeError, PermissionError):
                    # Skip binary files or files we can't process
                    continue
    
    def _python_cli_template(self, template_dir: Path):
        """Create Python CLI template"""
        template_dir.mkdir(parents=True, exist_ok=True)
        
        # Template configuration
        config = {
            "description": "Python CLI application template",
            "category": "python",
            "variables": [
                {"name": "AUTHOR_NAME", "description": "Author name", "default": "Your Name"},
                {"name": "AUTHOR_EMAIL", "description": "Author email", "default": "you@example.com"}
            ]
        }
        
        with open(template_dir / "template.json", 'w') as f:
            json.dump(config, f, indent=2)
        
        # Create directory structure
        (template_dir / "src" / "{{PROJECT_NAME_SNAKE}}").mkdir(parents=True, exist_ok=True)
        (template_dir / "tests").mkdir(exist_ok=True)
        
        # Main CLI file
        main_py = template_dir / "src" / "{{PROJECT_NAME_SNAKE}}" / "__init__.py"
        main_py.write_text('''#!/usr/bin/env python3
"""
{{PROJECT_NAME}}
A CLI application built with Python
"""

import argparse
import sys
from typing import List, Optional

def main(args: Optional[List[str]] = None) -> int:
    """Main entry point for {{PROJECT_NAME}}"""
    parser = argparse.ArgumentParser(description="{{PROJECT_NAME}} CLI")
    parser.add_argument("--version", action="version", version="{{PROJECT_NAME}} 1.0.0")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    
    parsed_args = parser.parse_args(args)
    
    if parsed_args.verbose:
        print("Running {{PROJECT_NAME}} in verbose mode")
    
    print("Hello from {{PROJECT_NAME}}!")
    return 0

if __name__ == "__main__":
    sys.exit(main())
''')
        
        # Setup.py
        setup_py = template_dir / "setup.py"
        setup_py.write_text('''from setuptools import setup, find_packages

setup(
    name="{{PROJECT_NAME}}",
    version="1.0.0",
    author="{{AUTHOR_NAME}}",
    author_email="{{AUTHOR_EMAIL}}",
    description="A Python CLI application",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "{{PROJECT_NAME}}={{PROJECT_NAME_SNAKE}}:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
''')
        
        # README
        readme = template_dir / "README.md"
        readme.write_text('''# {{PROJECT_NAME}}

A Python CLI application.

## Installation

```bash
pip install -e .
```

## Usage

```bash
{{PROJECT_NAME}} --help
```

## Development

```bash
# Install in development mode
pip install -e .

# Run tests
python -m pytest tests/
```
''')
        
        # Basic test
        test_file = template_dir / "tests" / "test_{{PROJECT_NAME_SNAKE}}.py"
        test_file.write_text('''import pytest
from {{PROJECT_NAME_SNAKE}} import main

def test_main():
    """Test main function"""
    result = main(["--version"])
    assert result == 0
''')
    
    def _web_app_template(self, template_dir: Path):
        """Create web app template"""
        template_dir.mkdir(parents=True, exist_ok=True)
        
        config = {
            "description": "Web application starter template",
            "category": "web",
            "variables": [
                {"name": "PORT", "description": "Server port", "default": "3000"}
            ]
        }
        
        with open(template_dir / "template.json", 'w') as f:
            json.dump(config, f, indent=2)
        
        # Basic structure
        (template_dir / "src").mkdir(exist_ok=True)
        (template_dir / "public").mkdir(exist_ok=True)
        
        # Package.json
        package_json = template_dir / "package.json"
        package_json.write_text('''{
  "name": "{{PROJECT_NAME}}",
  "version": "1.0.0",
  "description": "Web application",
  "main": "src/index.js",
  "scripts": {
    "start": "node src/index.js",
    "dev": "nodemon src/index.js"
  },
  "dependencies": {
    "express": "^4.18.0"
  },
  "devDependencies": {
    "nodemon": "^2.0.0"
  }
}
''')
        
        # Main server file
        index_js = template_dir / "src" / "index.js"
        index_js.write_text('''const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || {{PORT}};

// Serve static files
app.use(express.static(path.join(__dirname, '../public')));

// Basic route
app.get('/', (req, res) => {
    res.send('<h1>Welcome to {{PROJECT_NAME}}!</h1>');
});

app.listen(PORT, () => {
    console.log(`{{PROJECT_NAME}} server running on port ${PORT}`);
});
''')
    
    def _api_service_template(self, template_dir: Path):
        """Create API service template"""
        template_dir.mkdir(parents=True, exist_ok=True)
        
        config = {
            "description": "REST API service template",
            "category": "api",
            "variables": [
                {"name": "API_VERSION", "description": "API version", "default": "v1"}
            ]
        }
        
        with open(template_dir / "template.json", 'w') as f:
            json.dump(config, f, indent=2)
        
        # Basic structure for API
        (template_dir / "src" / "routes").mkdir(parents=True, exist_ok=True)
        (template_dir / "src" / "models").mkdir(exist_ok=True)
        (template_dir / "src" / "middleware").mkdir(exist_ok=True)
        
        # Package.json for API
        package_json = template_dir / "package.json"
        package_json.write_text('''{
  "name": "{{PROJECT_NAME}}-api",
  "version": "1.0.0",
  "description": "REST API service",
  "main": "src/server.js",
  "scripts": {
    "start": "node src/server.js",
    "dev": "nodemon src/server.js"
  },
  "dependencies": {
    "express": "^4.18.0",
    "cors": "^2.8.5",
    "helmet": "^6.0.0",
    "dotenv": "^16.0.0"
  },
  "devDependencies": {
    "nodemon": "^2.0.0"
  }
}
''')
    
    def _claude_plugin_template(self, template_dir: Path):
        """Create Claude Code CLI plugin template"""
        template_dir.mkdir(parents=True, exist_ok=True)
        
        config = {
            "description": "Claude Code CLI plugin template",
            "category": "claude",
            "variables": [
                {"name": "COMMAND_NAME", "description": "Command name", "default": "my-command"}
            ]
        }
        
        with open(template_dir / "template.json", 'w') as f:
            json.dump(config, f, indent=2)
        
        # Commands directory
        commands_dir = template_dir / "commands"
        commands_dir.mkdir(exist_ok=True)
        
        # Sample command
        command_file = commands_dir / "{{COMMAND_NAME}}.md"
        command_file.write_text('''# {{PROJECT_NAME_CAMEL}} Command

I'll help you with {{PROJECT_NAME}} functionality.

This command demonstrates how to create custom Claude Code CLI commands.

## What I'll do:

1. Analyze the current project context
2. Perform the requested {{PROJECT_NAME}} operation
3. Provide clear feedback on the results

Let me start by checking the project structure and understanding what you need.

```bash
# Check current directory
pwd
ls -la

# Show project structure
find . -type f -name "*.py" -o -name "*.js" -o -name "*.md" | head -20
```

Based on the project context, I'll customize the approach for your specific needs.
''')
        
        # Installation script
        install_py = template_dir / "install.py"
        install_py.write_text('''#!/usr/bin/env python3
"""
{{PROJECT_NAME}} Plugin Installer
"""

import os
import shutil
import sys
from pathlib import Path

def main():
    script_dir = Path(__file__).parent.absolute()
    commands_source = script_dir / "commands"
    claude_dir = Path.home() / ".claude"
    commands_dest = claude_dir / "commands"
    
    print("{{PROJECT_NAME}} Plugin Installer")
    print("=" * 40)
    
    if not commands_source.exists():
        print(f"[ERROR] Commands directory not found at {commands_source}")
        sys.exit(1)
    
    commands_dest.mkdir(parents=True, exist_ok=True)
    print(f"[OK] Target directory: {commands_dest}")
    
    command_files = list(commands_source.glob("*.md"))
    if not command_files:
        print(f"[ERROR] No .md files found in {commands_source}")
        sys.exit(1)
    
    print(f"\\n[INSTALL] Installing {len(command_files)} commands:")
    for file in command_files:
        dest_file = commands_dest / file.name
        shutil.copy2(file, dest_file)
        print(f"  + {file.name}")
    
    print("\\n[SUCCESS] {{PROJECT_NAME}} plugin installed!")
    print("\\nUsage:")
    print("  1. Open Claude Code CLI")
    print("  2. Type / to see available commands")
    print(f"  3. Use /{{COMMAND_NAME}} to run your command")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\\n[ERROR] Installation failed: {e}")
        sys.exit(1)
''')
        
        # README
        readme = template_dir / "README.md"
        readme.write_text('''# {{PROJECT_NAME}}

A Claude Code CLI plugin.

## Installation

```bash
python install.py
```

## Usage

After installation, use the command in Claude Code CLI:

```
/{{COMMAND_NAME}}
```

## Development

To modify the command, edit `commands/{{COMMAND_NAME}}.md` and reinstall.
''')