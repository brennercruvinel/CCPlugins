#!/usr/bin/env python3
"""
Jira Integration for CCPlugins MCP Server
"""

import os
import requests
import json
from typing import Dict, List, Optional
from base64 import b64encode

class JiraIntegration:
    def __init__(self):
        self.url = os.getenv('JIRA_URL')
        self.email = os.getenv('JIRA_EMAIL')
        self.api_token = os.getenv('JIRA_API_TOKEN')
        self.session = requests.Session()
        
        if self.url and self.email and self.api_token:
            # Setup basic auth
            auth_string = f"{self.email}:{self.api_token}"
            auth_bytes = auth_string.encode('ascii')
            auth_b64 = b64encode(auth_bytes).decode('ascii')
            
            self.session.headers.update({
                'Authorization': f'Basic {auth_b64}',
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            })
    
    def is_configured(self) -> bool:
        """Check if Jira integration is properly configured"""
        return all([self.url, self.email, self.api_token])
    
    async def create_issue(self, summary: str, description: str = "", 
                          project: str = "", issue_type: str = "Task") -> Dict:
        """Create a new issue in Jira"""
        if not self.is_configured():
            return {
                "success": False,
                "error": "Jira integration not configured. Set JIRA_URL, JIRA_EMAIL, and JIRA_API_TOKEN environment variables."
            }
        
        # Get project key if not provided
        if not project:
            projects = await self.get_projects()
            if projects and len(projects) > 0:
                project = projects[0]['key']
            else:
                return {"success": False, "error": "No projects found and no project specified"}
        
        # Create issue payload
        payload = {
            "fields": {
                "project": {"key": project},
                "summary": summary,
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": description or "Created via CCPlugins MCP integration"
                                }
                            ]
                        }
                    ]
                },
                "issuetype": {"name": issue_type}
            }
        }
        
        try:
            response = self.session.post(
                f"{self.url}/rest/api/3/issue",
                data=json.dumps(payload)
            )
            
            if response.status_code == 201:
                issue_data = response.json()
                return {
                    "success": True,
                    "issue": {
                        "key": issue_data['key'],
                        "url": f"{self.url}/browse/{issue_data['key']}",
                        "summary": summary
                    }
                }
            else:
                return {
                    "success": False,
                    "error": f"Failed to create issue: {response.status_code} - {response.text}"
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": f"Exception creating issue: {str(e)}"
            }
    
    async def get_projects(self) -> List[Dict]:
        """Get list of available projects"""
        if not self.is_configured():
            return []
        
        try:
            response = self.session.get(f"{self.url}/rest/api/3/project/search")
            if response.status_code == 200:
                data = response.json()
                return [{"key": p["key"], "name": p["name"]} for p in data.get("values", [])]
            return []
        except Exception:
            return []
    
    async def get_issue_types(self, project_key: str) -> List[Dict]:
        """Get available issue types for a project"""
        if not self.is_configured():
            return []
        
        try:
            response = self.session.get(f"{self.url}/rest/api/3/issuetype")
            if response.status_code == 200:
                data = response.json()
                return [{"name": it["name"], "description": it.get("description", "")} 
                       for it in data if not it.get("subtask", False)]
            return []
        except Exception:
            return []

    async def search_issues(self, jql: str, max_results: int = 50) -> List[Dict]:
        """Search issues using JQL"""
        if not self.is_configured():
            return []
        
        try:
            params = {
                "jql": jql,
                "maxResults": max_results,
                "fields": "summary,status,assignee,created,updated"
            }
            
            response = self.session.get(
                f"{self.url}/rest/api/3/search",
                params=params
            )
            
            if response.status_code == 200:
                data = response.json()
                issues = []
                for issue in data.get("issues", []):
                    issues.append({
                        "key": issue["key"],
                        "summary": issue["fields"]["summary"],
                        "status": issue["fields"]["status"]["name"],
                        "url": f"{self.url}/browse/{issue['key']}"
                    })
                return issues
            return []
        except Exception:
            return []