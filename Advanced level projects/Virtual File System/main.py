## Virtual File System:
import os
import time
from collections import defaultdict

class VirtualFileSystem:
    def __init__(self):
        self.files = {}  # Stores file content and metadata
        self.directories = {'/': {}}  # Stores directory structure
        self.links = {}  # Stores symbolic links
        self.permissions = defaultdict(lambda: 'rwxr-xr-x')  # Default permissions

    def create_file(self, path, content=""):
        """Create a new file with the given content."""
        if os.path.dirname(path) not in self.directories:
            print(f"Directory {os.path.dirname(path)} does not exist.")
            return

        self.files[path] = {
            'content': content,
            'size': len(content),
            'ctime': time.time(),
            'mtime': time.time()
        }
        self.directories[os.path.dirname(path)][os.path.basename(path)] = 'file'

    def read_file(self, path):
        """Read the content of a file."""
        if path in self.files:
            return self.files[path]['content']
        else:
            print(f"File {path} does not exist.")
            return None

    def write_file(self, path, content):
        """Write content to a file."""
        if path in self.files:
            self.files[path]['content'] = content
            self.files[path]['size'] = len(content)
            self.files[path]['mtime'] = time.time()
        else:
            print(f"File {path} does not exist.")

    def delete_file(self, path):
        """Delete a file."""
        if path in self.files:
            del self.files[path]
            del self.directories[os.path.dirname(path)][os.path.basename(path)]
        else:
            print(f"File {path} does not exist.")

    def create_directory(self, path):
        """Create a new directory."""
        if os.path.dirname(path) not in self.directories and path != '/':
            print(f"Parent directory {os.path.dirname(path)} does not exist.")
            return

        self.directories[path] = {}
        if path != '/':
            self.directories[os.path.dirname(path)][os.path.basename(path)] = 'directory'

    def delete_directory(self, path):
        """Delete a directory."""
        if path in self.directories:
            if len(self.directories[path]) > 0:
                print(f"Directory {path} is not empty.")
                return

            del self.directories[path]
            del self.directories[os.path.dirname(path)][os.path.basename(path)]
        else:
            print(f"Directory {path} does not exist.")

    def create_symlink(self, target, link_name):
        """Create a symbolic link."""
        self.links[link_name] = target

    def read_symlink(self, link_name):
        """Read the target of a symbolic link."""
        if link_name in self.links:
            return self.links[link_name]
        else:
            print(f"Link {link_name} does not exist.")
            return None

    def set_permissions(self, path, permissions):
        """Set file or directory permissions."""
        if path in self.files or path in self.directories:
            self.permissions[path] = permissions
        else:
            print(f"Path {path} does not exist.")

    def get_permissions(self, path):
        """Get file or directory permissions."""
        if path in self.files or path in self.directories:
            return self.permissions[path]
        else:
            print(f"Path {path} does not exist.")
            return None

# Example usage
vfs = VirtualFileSystem()
vfs.create_directory('/home')
vfs.create_directory('/home/user')
vfs.create_file('/home/user/file.txt', 'Hello, World!')
vfs.create_symlink('/home/user/file.txt', '/home/user/link_to_file')

print(vfs.read_file('/home/user/file.txt'))  # Output: Hello, World!
print(vfs.read_symlink('/home/user/link_to_file'))  # Output: /home/user/file.txt
print(vfs.get_permissions('/home/user/file.txt'))  # Output: rwxr-xr-x

vfs.write_file('/home/user/file.txt', 'New content')
print(vfs.read_file('/home/user/file.txt'))  # Output: New content

vfs.set_permissions('/home/user/file.txt', 'rw-------')
print(vfs.get_permissions('/home/user/file.txt'))  # Output: rw-------
