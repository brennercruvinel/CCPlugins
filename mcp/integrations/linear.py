#!/usr/bin/env python3
"""
Linear Integration for CCPlugins MCP Server
"""

import os
import requests
import json
from typing import Dict, List, Optional

class LinearIntegration:
    def __init__(self):
        self.api_token = os.getenv('LINEAR_API_TOKEN')
        self.api_url = "https://api.linear.app/graphql"
        self.session = requests.Session()
        
        if self.api_token:
            self.session.headers.update({
                'Authorization': f'Bearer {self.api_token}',
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            })
    
    def is_configured(self) -> bool:
        """Check if Linear integration is properly configured"""
        return bool(self.api_token)
    
    async def create_issue(self, title: str, description: str = "", 
                          team_id: str = "", priority: int = 2) -> Dict:
        """Create a new issue in Linear"""
        if not self.is_configured():
            return {
                "success": False,
                "error": "Linear integration not configured. Set LINEAR_API_TOKEN environment variable."
            }
        
        # Get team ID if not provided
        if not team_id:
            teams = await self.get_teams()
            if teams and len(teams) > 0:
                team_id = teams[0]['id']
            else:
                return {"success": False, "error": "No teams found and no team specified"}
        
        # GraphQL mutation to create issue
        mutation = """
        mutation IssueCreate($input: IssueCreateInput!) {
            issueCreate(input: $input) {
                success
                issue {
                    id
                    identifier
                    title
                    url
                }
            }
        }
        """
        
        variables = {
            "input": {
                "title": title,
                "description": description or "Created via CCPlugins MCP integration",
                "teamId": team_id,
                "priority": priority
            }
        }
        
        try:
            response = self.session.post(
                self.api_url,
                data=json.dumps({
                    "query": mutation,
                    "variables": variables
                })
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("data", {}).get("issueCreate", {}).get("success"):
                    issue = data["data"]["issueCreate"]["issue"]
                    return {
                        "success": True,
                        "issue": {
                            "id": issue["id"],
                            "identifier": issue["identifier"],
                            "title": issue["title"],
                            "url": issue["url"]
                        }
                    }
                else:
                    return {
                        "success": False,
                        "error": "Failed to create issue in Linear"
                    }
            else:
                return {
                    "success": False,
                    "error": f"Linear API error: {response.status_code} - {response.text}"
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": f"Exception creating Linear issue: {str(e)}"
            }
    
    async def get_teams(self) -> List[Dict]:
        """Get list of available teams"""
        if not self.is_configured():
            return []
        
        query = """
        query Teams {
            teams {
                nodes {
                    id
                    name
                    key
                }
            }
        }
        """
        
        try:
            response = self.session.post(
                self.api_url,
                data=json.dumps({"query": query})
            )
            
            if response.status_code == 200:
                data = response.json()
                teams = data.get("data", {}).get("teams", {}).get("nodes", [])
                return [{"id": t["id"], "name": t["name"], "key": t["key"]} for t in teams]
            return []
        except Exception:
            return []
    
    async def get_issues(self, team_id: str = "", limit: int = 50) -> List[Dict]:
        """Get issues from Linear"""
        if not self.is_configured():
            return []
        
        # Build query filter
        filter_clause = ""
        if team_id:
            filter_clause = f'filter: {{ team: {{ id: {{ eq: "{team_id}" }} }} }}'
        
        query = f"""
        query Issues {{
            issues({filter_clause} first: {limit}) {{
                nodes {{
                    id
                    identifier
                    title
                    state {{
                        name
                    }}
                    assignee {{
                        name
                    }}
                    url
                    createdAt
                }}
            }}
        }}
        """
        
        try:
            response = self.session.post(
                self.api_url,
                data=json.dumps({"query": query})
            )
            
            if response.status_code == 200:
                data = response.json()
                issues = data.get("data", {}).get("issues", {}).get("nodes", [])
                return [
                    {
                        "id": issue["id"],
                        "identifier": issue["identifier"],
                        "title": issue["title"],
                        "state": issue["state"]["name"],
                        "assignee": issue.get("assignee", {}).get("name", "Unassigned"),
                        "url": issue["url"],
                        "created": issue["createdAt"]
                    }
                    for issue in issues
                ]
            return []
        except Exception:
            return []
    
    async def get_states(self, team_id: str) -> List[Dict]:
        """Get workflow states for a team"""
        if not self.is_configured():
            return []
        
        query = f"""
        query WorkflowStates {{
            team(id: "{team_id}") {{
                states {{
                    nodes {{
                        id
                        name
                        type
                        color
                    }}
                }}
            }}
        }}
        """
        
        try:
            response = self.session.post(
                self.api_url,
                data=json.dumps({"query": query})
            )
            
            if response.status_code == 200:
                data = response.json()
                states = data.get("data", {}).get("team", {}).get("states", {}).get("nodes", [])
                return [
                    {
                        "id": state["id"],
                        "name": state["name"],
                        "type": state["type"],
                        "color": state["color"]
                    }
                    for state in states
                ]
            return []
        except Exception:
            return []