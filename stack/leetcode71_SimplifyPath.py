"""
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. 
For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.

 

Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.


"""

# Several cases
# . current directly, should be removed
# .. go back to one level up, should be removed if there is a parent level
# ... keep the same as it is treated as file/directory name
# several /// in the same place, should be replaced by '/', can be handled by split 

import unittest
def simplifyPath(path):
    l = path.split('/')
    stack = []
    for i, v in enumerate(l):
        if v not in ('.', '..', ' '):
            stack.append(v) # isalpha and ...
        elif v == '..' and stack:
            stack.pop()
    return '/' + '/'.join(stack)


# simplifyPath("/home//foo/")
class TestAddFunction(unittest.TestCase):

    def test_function_1(self):
        self.assertEqual(simplifyPath("//.../"), "/...")

    def test_function_2(self):
        self.assertEqual(simplifyPath("/../ "), "/")

    def test_function_3(self):
        self.assertEqual(simplifyPath("/home//foo/"), "/home/foo")

if __name__ == '__main__':
    unittest.main()


