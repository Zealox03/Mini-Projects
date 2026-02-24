# The re module in Python provides support for working with regular expressions. Tasks like string matching, searching and manipulation

import tkinter as tk
from tkinter import ttk, messagebox # Modern, styled widgets
import sqlite3 # Database to store users and tasks
import hashlib # Encrypts password (SHA-256 hashing)
import secrets # Generates secure random numbers (salting method)
import re 
from enum import Enum # Creates enumerations
from abc import ABC, abstractmethod # Creates abstract classes
from datetime import datetime
from typing import List, Optional

# We use Enum as special class that defines fixed values
# this is to prevent SQL injection
# We cannot use Priority.Super_High for example
class Priority(Enum):
    Low = "Low"
    Medium = "Medium"
    High = "High"

class UserRole(Enum):
    # User role for access control
    Admin = "Admin"
    Guest = "Guest"

class TaskStatus(Enum):
    Pending = "Pending"
    Completed = "Completed"

class SecurityUtils:
    # Abstraction and Static Methods include Security operations abstracted away
    # Static is essential as they don't need instance data and purely utility functions
    # All password operations are cryptographic functions
    @staticmethod
    def hash_password(password: str, salt: Optional[str] = None) -> tuple:
        if salt is None:
            salt = secrets.token_hex(32) # Cryptographically create random salt
        
        # SHA-256 hashing with salt (industry standard)
        pwd_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        return pwd_hash, salt
    
    # Verify password
    @staticmethod
    def verify_password(password: str, stored_hash: str, salt: str) -> bool:
        # Clean way of returning tuple data, return first one but ignore the other one
        pwd_hash, _ = SecurityUtils.hash_password(password, salt)
        return pwd_hash == stored_hash
    
    # r"/d": Looks for ANY digit (0-9)
    @staticmethod
    # Validate password
    def validate_password_strength(password: str) -> tuple:
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"
        if not re.search(r"[A-Z]", password):
            return False, "Password must contain uppercase letter"
        if not re.search(r"[a-z]", password):
            return False, "Password must contain lowercase letter"
        if not re.search(r"\d", password):
            return False, "Password must contain a number"
        return True, ""
    
    # Sanitize input to prevent SQL Injection
    def sanitize_input(text: str) -> str:
        dangerous = ["--",";","/*","*/","xp_","sp_","DROP","DELETE","SELECT","INSERT"]
        sanitized = text
        for pattern in dangerous:
            sanitized = sanitized.replace(pattern, "")
        return sanitized.strip()
    
# User Class # This is also the parent class
class User(ABC):
    def __init__(self, username: str, role: UserRole):
        self._username = username # Protected attribute
        self._role = role
        self._session_active = False # Tracks whether user is active
    
    @abstractmethod
    def get_permissions(self) -> List[str]:
        """ABSTRACTION: Each user type defines its own permissions"""
        pass

    def authenticate(self, password: str, stored_hash: str, salt: str):
        is_valid = SecurityUtils.verify_password(password, stored_hash, salt)

        if is_valid:
            self._session_active = True
        return is_valid # This will return False/ True
    
    def logout(self):
        self._session_active = False

    @property
    def username(self):
        """ENCAPSULATION: Read-only access to username"""
        # Hackers cannot access and modify self.username = "hacker"
        return self._username
    
    @property
    def role(self):
        return self._role
    
    @property
    def is_authenticated(self):
        return self._session_active

class RegularUser(User):
    """INHERITANCE: Regular Users inherits from User base class
    but with limited permissions"""
    def __init__ (self, username: str):
        super().__init__(username, UserRole.Guest)

    def get_permissions(self) -> List[str]:
        return ["create_task","edit_own_task","delete_own_task"]

class AdminUser(User):
    def __init__ (self, username: str):
        super().__init__(username, UserRole.Admin)

    def get_permissions(self) -> List[str]:
        return ["create_task","edit_any_task","delete_any_task","view_all_users","delete_users"]
    

"""TASK MODEL CLASS"""
class Task:
    """MODEL: Represents a single task
    ENCAPSULATION: Private attributes with controlled access"""

    def __init__ (self, task_id: str, title: str, description: str, priority: Priority, owner: str, status: TaskStatus = TaskStatus.Pending):
        self._id = task_id
        self._title = SecurityUtils.sanitize_input(title)
        self._description = SecurityUtils.sanitize_input(description)
        self._priority = priority
        self._owner = owner
        self._status = status
        self._created_at = datetime.now()
    
    @property
    def id(self):
        return self._id
    
    @property
    def title(self):
        return self._title
    
    @property
    def status(self):
        return self._status
    
    @property
    def priority(self):
        return self._priority
    
    def mark_complete(self):
        self._status = TaskStatus.Completed

    """MAGIC METHOD: Convert object into human readable string"""
    def __str__(self):
        return f"[{self.priority.value}] {self.title} - {self.status.value}"
    
    
