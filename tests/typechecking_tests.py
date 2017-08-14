import unittest

import typy


class MyTestCase(unittest.TestCase):
    def test1(self):
        print("Test 1 starting")

        @typy.typed
        def f1(string, val: int, keyval: (str, int)):
            pass

        f1("hello", 33, ("num", 6))

        self.assertRaises(typy.TypeException, f1, 3, "33", ("num", 6))
        self.assertRaises(typy.TypeException, f1, 3, 33, ("num", "ok"))
        self.assertRaises(typy.TypeException, f1, True, 33, ("num", 8, 6))

    def test2(self):
        print("Test 2 starting")

        @typy.typed
        def f2(numeric: {int, float}, dirtree: [dict, [dict, str]] = {"hello": {"there": "nice_file.txt"}}) -> bool:
            return True

        f2(3.0, {"dir": {"subdir": "file.txt"}})
        f2(3, {"dir": {"subdir": "file.txt"}, "dir2": {"subdir2": "file2.txt"}})
        f2(35)

        self.assertRaises(typy.TypeException, f2, True, {})
        self.assertRaises(typy.TypeException, f2, True, {"hello": 3})
        self.assertRaises(typy.TypeException, f2, True, {"hello": {"there": 33}})

    def test3(self):
        print("Test 3 starting")

        @typy.typed
        def f3(string_array: [list, str]) -> type(None):
            return

        class MyStr(str):
            def __init__(self):
                super().__init__()

        f3([MyStr(), MyStr()])
        self.assertRaises(typy.TypeException, f3, [3, 3])

    def test4(self):
        print("Test 4 starting")

        @typy.typed
        def f4(error: 3):
            pass

        self.assertRaises(typy.InvalidTypeCheckException, f4, 55)


if __name__ == '__main__':
    unittest.main()
