

def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)




scope_test()

print("In global scope:", spam)




"""
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
"""

"""
注意：local 赋值语句是无法改变 scope_test 的 spam 绑定。nonlocal 赋值语句改变了 scope_test 的 spam 绑定，
并且 global 赋值语句从模块级改变了 spam 绑定。

你也可以看到在 global 赋值语句之前对 spam 是没有预先绑定的。
"""