from typing import Any, Dict, List

FLAGS: Dict[str, str] = {
    "sqli": "FLAG{sql_injection_master_2026}",
    "xss": "FLAG{cross_site_scripting_expert}",
    "idor": "FLAG{idor_hunter_2026}",
    "path_traversal": "FLAG{directory_traversal_detective}",
    "command_injection": "FLAG{command_injection_ Specialist}",
}

USERS: Dict[int, Dict[str, str]] = {
    1: {"username": "admin", "email": "admin@vulnctf.local", "role": "admin", "secret": FLAGS["idor"]},
    2: {"username": "guest", "email": "guest@vulnctf.local", "role": "user", "secret": "No flag here"},
    3: {"username": "cyber_user", "email": "cyber@vulnctf.local", "role": "user", "secret": "No flag here"},
}

POSTS: List[Dict[str, Any]] = [
    {"id": 1, "user": "admin", "content": "Welcome to VulnCTF! Can someone check if this site is secure?"},
    {"id": 2, "user": "guest", "content": "<script>alert('XSS')</script>"},
    {"id": 3, "user": "admin", "content": "I heard XSS is dangerous... " + FLAGS["xss"]},
]
