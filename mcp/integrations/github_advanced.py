#!/usr/bin/env python3
"""
Enhanced GitHub Integration for CCPlugins MCP Server
Extends the existing todos-to-issues functionality with advanced features
"""

import os
import subprocess
import json
from typing import Dict, List, Optional
from pathlib import Path

class GitHubAdvancedIntegration:
    def __init__(self):
        self.token = os.getenv('GITHUB_TOKEN')
        self.gh_cli_available = self._check_gh_cli()
    
    def _check_gh_cli(self) -> bool:
        """Check if GitHub CLI is available"""
        try:
            result = subprocess.run(['gh', '--version'], capture_output=True, text=True)
            return result.returncode == 0
        except FileNotFoundError:
            return False
    
    def is_configured(self) -> bool:
        """Check if GitHub integration is properly configured"""
        return self.gh_cli_available
    
    async def bulk_issue_operations(self, operations: List[Dict]) -> Dict:
        """Perform bulk operations on GitHub issues"""
        if not self.is_configured():
            return {
                "success": False,
                "error": "GitHub CLI not available or not authenticated"
            }
        
        results = []
        errors = []
        
        for operation in operations:
            try:
                if operation['type'] == 'create':
                    result = await self._create_issue_advanced(operation['data'])
                elif operation['type'] == 'update':
                    result = await self._update_issue(operation['data'])
                elif operation['type'] == 'close':
                    result = await self._close_issue(operation['data'])
                else:
                    result = {"success": False, "error": f"Unknown operation: {operation['type']}"}
                
                results.append(result)
                if not result.get('success', False):
                    errors.append(result.get('error', 'Unknown error'))
                    
            except Exception as e:
                error_msg = f"Error in operation {operation['type']}: {str(e)}"
                errors.append(error_msg)
                results.append({"success": False, "error": error_msg})
        
        return {
            "success": len(errors) == 0,
            "results": results,
            "errors": errors,
            "summary": f"Completed {len(results)} operations, {len(errors)} errors"
        }
    
    async def _create_issue_advanced(self, data: Dict) -> Dict:
        """Create issue with advanced features"""
        title = data.get('title', 'Untitled Issue')
        body = data.get('body', '')
        labels = data.get('labels', [])
        assignees = data.get('assignees', [])
        milestone = data.get('milestone', '')
        project = data.get('project', '')
        
        # Build gh command
        cmd = ['gh', 'issue', 'create', '--title', title, '--body', body]
        
        if labels:
            cmd.extend(['--label', ','.join(labels)])
        
        if assignees:
            cmd.extend(['--assignee', ','.join(assignees)])
        
        if milestone:
            cmd.extend(['--milestone', milestone])
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                issue_url = result.stdout.strip()
                return {
                    "success": True,
                    "issue_url": issue_url,
                    "title": title
                }
            else:
                return {
                    "success": False,
                    "error": f"Failed to create issue: {result.stderr}"
                }
        except Exception as e:
            return {
                "success": False,
                "error": f"Exception creating issue: {str(e)}"
            }
    
    async def _update_issue(self, data: Dict) -> Dict:
        """Update existing issue"""
        issue_number = data.get('number')
        if not issue_number:
            return {"success": False, "error": "Issue number required for update"}
        
        cmd = ['gh', 'issue', 'edit', str(issue_number)]
        
        if 'title' in data:
            cmd.extend(['--title', data['title']])
        
        if 'body' in data:
            cmd.extend(['--body', data['body']])
        
        if 'add_labels' in data:
            cmd.extend(['--add-label', ','.join(data['add_labels'])])
        
        if 'remove_labels' in data:
            cmd.extend(['--remove-label', ','.join(data['remove_labels'])])
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                return {
                    "success": True,
                    "message": f"Updated issue #{issue_number}"
                }
            else:
                return {
                    "success": False,
                    "error": f"Failed to update issue: {result.stderr}"
                }
        except Exception as e:
            return {
                "success": False,
                "error": f"Exception updating issue: {str(e)}"
            }
    
    async def _close_issue(self, data: Dict) -> Dict:
        """Close issue"""
        issue_number = data.get('number')
        if not issue_number:
            return {"success": False, "error": "Issue number required to close"}
        
        cmd = ['gh', 'issue', 'close', str(issue_number)]
        
        if 'comment' in data:
            cmd.extend(['--comment', data['comment']])
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                return {
                    "success": True,
                    "message": f"Closed issue #{issue_number}"
                }
            else:
                return {
                    "success": False,
                    "error": f"Failed to close issue: {result.stderr}"
                }
        except Exception as e:
            return {
                "success": False,
                "error": f"Exception closing issue: {str(e)}"
            }
    
    async def analyze_repository(self, path: str = ".") -> Dict:
        """Analyze repository for potential improvements"""
        analysis = {
            "has_readme": False,
            "has_license": False,
            "has_gitignore": False,
            "has_ci_cd": False,
            "has_contributing": False,
            "has_changelog": False,
            "open_issues_count": 0,
            "pr_count": 0,
            "recommendations": []
        }
        
        try:
            # Check for common files
            repo_path = Path(path)
            analysis["has_readme"] = any(repo_path.glob("README*"))
            analysis["has_license"] = any(repo_path.glob("LICENSE*"))
            analysis["has_gitignore"] = (repo_path / ".gitignore").exists()
            analysis["has_contributing"] = any(repo_path.glob("CONTRIBUTING*"))
            analysis["has_changelog"] = any(repo_path.glob("CHANGELOG*"))
            
            # Check for CI/CD
            github_dir = repo_path / ".github" / "workflows"
            analysis["has_ci_cd"] = github_dir.exists() and any(github_dir.glob("*.yml"))
            
            # Get repository stats
            try:
                # Get issue count
                result = subprocess.run(['gh', 'issue', 'list', '--state', 'open', '--json', 'number'], 
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    issues = json.loads(result.stdout)
                    analysis["open_issues_count"] = len(issues)
                
                # Get PR count
                result = subprocess.run(['gh', 'pr', 'list', '--state', 'open', '--json', 'number'], 
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    prs = json.loads(result.stdout)
                    analysis["pr_count"] = len(prs)
            except:
                pass  # Continue even if we can't get stats
            
            # Generate recommendations
            if not analysis["has_readme"]:
                analysis["recommendations"].append("Add a README file to describe your project")
            
            if not analysis["has_license"]:
                analysis["recommendations"].append("Add a LICENSE file to clarify usage rights")
            
            if not analysis["has_gitignore"]:
                analysis["recommendations"].append("Add a .gitignore file to exclude unnecessary files")
            
            if not analysis["has_ci_cd"]:
                analysis["recommendations"].append("Set up GitHub Actions for CI/CD")
            
            if not analysis["has_contributing"]:
                analysis["recommendations"].append("Add CONTRIBUTING.md to guide contributors")
            
            if analysis["open_issues_count"] > 10:
                analysis["recommendations"].append("Consider triaging and closing stale issues")
            
            return {
                "success": True,
                "analysis": analysis
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Exception analyzing repository: {str(e)}"
            }
    
    async def create_pr_from_branch(self, branch: str, title: str, body: str = "") -> Dict:
        """Create pull request from branch"""
        if not self.is_configured():
            return {
                "success": False,
                "error": "GitHub CLI not available"
            }
        
        cmd = ['gh', 'pr', 'create', '--head', branch, '--title', title, '--body', body]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                pr_url = result.stdout.strip()
                return {
                    "success": True,
                    "pr_url": pr_url,
                    "title": title
                }
            else:
                return {
                    "success": False,
                    "error": f"Failed to create PR: {result.stderr}"
                }
        except Exception as e:
            return {
                "success": False,
                "error": f"Exception creating PR: {str(e)}"
            }
    
    async def get_repository_insights(self) -> Dict:
        """Get repository insights and metrics"""
        if not self.is_configured():
            return {
                "success": False,
                "error": "GitHub CLI not available"
            }
        
        insights = {}
        
        try:
            # Get repository info
            result = subprocess.run(['gh', 'repo', 'view', '--json', 
                                   'name,description,stargazerCount,forkCount,issues,pullRequests'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                repo_data = json.loads(result.stdout)
                insights.update(repo_data)
            
            # Get recent activity
            result = subprocess.run(['gh', 'issue', 'list', '--limit', '5', '--json', 
                                   'number,title,createdAt,state'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                insights["recent_issues"] = json.loads(result.stdout)
            
            result = subprocess.run(['gh', 'pr', 'list', '--limit', '5', '--json', 
                                   'number,title,createdAt,state'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                insights["recent_prs"] = json.loads(result.stdout)
            
            return {
                "success": True,
                "insights": insights
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Exception getting insights: {str(e)}"
            }