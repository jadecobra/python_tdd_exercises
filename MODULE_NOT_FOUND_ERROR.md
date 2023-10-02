# How to solve the ModuleNotFoundError in python

Let us step through solving a `ModuleNotFoundError` in python using Test Driven Development

### Prerequisites

- [Setup a Test Driven Development Environment](./TDD_SETUP.md)

---

# ModuleNotFoundError

The `ModuleNotFoundError` is raised when you try to import a module that does not exist.
A Python Module is a file that ends in `.py` or a directory that contains an `__init__.py`.
Programming allows us to gain from our previous efforts as well as the efforts of others in the form of packages and modules that can be distributed for other people to use. To use these packages in python we have to import them.

### <span style="color:red">**RED**</span>: make it fail

Open a new file in your editor and save it as `test_module_not_found_error.py` in the `tests` folder you created in [Setup a Test Driven Development Environment](./TDD_SETUP.md)
Type the following in the file

```python
import module_0
import module_1
import module_2
import module_3
import module_4
import module_5
import module_6
import module_7
import module_8
import module_9
import module_10
import module_11
import module_12
import module_13
import module_14
import module_15
import module_16
import module_17
import module_18
import module_19
import module_20
import module_21
import module_22
import module_23
import module_24
import module_25
import module_26
import module_27
import module_28
import module_29
import module_30
import module_34
import module_32
import module_33
import module_34
import module_35
import module_36
import module_37
import module_38
import module_39
import module_40
import module_41
import module_42
import module_43
import module_44
import module_45
import module_46
import module_47
import module_48
import module_49
import module_50
import module_51
import module_52
import module_53
import module_54
import module_55
import module_56
import module_57
import module_58
import module_59
import module_60
import module_61
import module_62
import module_63
import module_64
import module_65
import module_66
import module_67
import module_68
import module_69
import module_70
import module_71
import module_72
import module_73
import module_74
import module_75
import module_76
import module_77
import module_78
import module_79
import module_80
import module_81
import module_82
import module_83
import module_84
import module_85
import module_86
import module_87
import module_88
import module_89
import module_90
import module_91
import module_92
import module_93
import module_94
import module_95
import module_96
import module_97
import module_98
import module_99
```

If you left `pytest-watch` running from [Setup a Test Driven Development Environment](./TDD_SETUP.md) you should see something like the following in your terminal

```python
    import module_0
E   ModuleNotFoundError: No module named 'module_0'
```

Looking at the traceback starting from the bottom
- `ModuleNotFoundError` - this error is raised when an import statement fails because python cannot find a module/package with the given name, in this case `module_0` does not exist
- `import module_0` - the line of code that caused the failure
- Add the errors to the running list of Exceptions encountered
    ```python
    # Exceptions Encountered
    # AssertionError
    # ImportError
    # ModuleNotFoundError
    ```
For more information about imports you can read [The Import Statement](https://docs.python.org/3/reference/simple_stmts.html#import)

### <span style="color:green">**GREEN**</span>: make it pass

- create `module_0.py` in the `<PROJECT_NAME>` folder and the terminal shows
    ```python
        import module_1
    E   ModuleNotFoundError: No module named 'module_1'
    ```
- create `module_1.py` in the `<PROJECT_NAME>` folder, the terminal shows the same error for a new line
    ```python
        import module_2
    E   ModuleNotFoundError: No module named 'module_2'
    ```
- create `module_2.py` in the `<PROJECT_NAME>` folder, the terminal will update to show the following
    ```python
        import module_3
    E   ModuleNotFoundError: No module named 'module_3'
    ```
- this is the pattern, repeat it until you have created `module_99.py` and the terminal will update to show a passing test
    ```python
    tests/test_<PROJECT_NAME>.py .                           [100%]

    ================= 1 passed in 0.06s =========================
    ```

*WELL DONE!*
You are on your way to being a troubleshooting master.
You now know how to solve `ModuleNotFoundError`