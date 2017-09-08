import unittest

import typy


class MyTestCase(unittest.TestCase):
    def test1(self):
        print("Test 1 starting")

        @typy.typed
        def f1(string, val: int, keyval: (str, int)):
            pass

        f1("hello", 33, ("num", 6))

        self.assertRaises(TypeError, f1, 3, "33", ("num", 6))
        self.assertRaises(TypeError, f1, 3, 33, ("num", "ok"))
        self.assertRaises(TypeError, f1, True, 33, ("num", 8, 6))

    def test2(self):
        print("Test 2 starting")

        @typy.typed
        def f2(numeric: {int, float}, dirtree: [dict, str, [dict, str, str]] = {"hello": {"there": "nice_file.txt"}}) -> bool:
            return True

        f2(3.0, dirtree={"dir": {"subdir": "file.txt"}})
        f2(3, dirtree={"dir": {"subdir": "file.txt"}, "dir2": {"subdir2": "file2.txt"}})
        f2(35)

        self.assertRaises(TypeError, f2, True, {})
        self.assertRaises(TypeError, f2, 3, {4: 3})
        self.assertRaises(TypeError, f2, True, {"hello": {"there": 33}})

    def test3(self):
        print("Test 3 starting")

        @typy.typed
        def f3(string_array: [list, str]) -> type(None):
            return

        class MyStr(str):
            def __init__(self):
                super().__init__()

        f3([MyStr(), MyStr()])
        self.assertRaises(TypeError, f3, [3, 3])

    def test4(self):
        print("Test 4 starting")

        @typy.typed
        def f4(error: 3):
            pass

        self.assertRaises(typy.InvalidTypeCheckException, f4, 55)


    def test5(self):
        print("Test 5 starting")

        @typy.none_safe
        def f5(a, b, c=3):
            pass

        self.assertRaises(TypeError, f5, 4, None)
        self.assertRaises(TypeError, f5, 4, 6, c=None)

    def test6(self):
        print("Test 6 starting")

        @typy.typed
        def f6(a: {int: [typy.NOT_SUBCLASS]}, b: {str: [typy.NONE_SAFE]}, c: {int: [typy.NONE_SAFE, typy.NOT_SUBCLASS]}):
            pass

        class sub_int(int):
            pass

        class sub_str(str):
            pass

        self.assertRaises(TypeError, f6, 3, None, 4)
        self.assertRaises(TypeError, f6, sub_int(), "", 4)
        self.assertRaises(TypeError, f6, 3, "", sub_int())
        self.assertRaises(TypeError, f6, 3, "", None)
        f6(3, "", 4)
        f6(None, sub_str(), 4)

    def test7(self):
        print("Test 7 starting")

        @typy.typed
        def f7(a: [int, float]):
            pass

        @typy.typed
        def f7_2(a: [dict, int, float, bool]):
            pass

        @typy.typed
        def f7_3(a: {int: {typy.NONE_SAFE}}):
            pass

        @typy.typed
        def f7_4(a: {int: [44]}):
            pass

        self.assertRaises(typy.InvalidTypeCheckException, f7, 3)
        self.assertRaises(typy.InvalidTypeCheckException, f7_2, {3 : 4.0})
        self.assertRaises(typy.InvalidTypeCheckException, f7_3, 8)
        self.assertRaises(typy.InvalidTypeCheckException, f7_4, 8)

    def test8(self):
        print("Test 8 starting")

        @typy.typed
        def f8(a: int, b: {bool, float}, c: [dict, int, [list, str]],\
               d: (bool, int, str), e: float) -> (bool, str):
            return (True, "OK")

        f8(3, True, {3: ["one", "two"]}, (False, 33, "hello"), 34.0)
if __name__ == '__main__':
    unittest.main()
