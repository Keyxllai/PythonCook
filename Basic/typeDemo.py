import types
import datetime

'''
'''
def show_type(val):
    if val is None:
        return
    val_type, val_mem_id = type(val), id(val)
    print(u"value: {val}, type: {val_type}, memery: {id}".format(
        val_type=val_type,
        val=val,
        id=val_mem_id))

def fun():
    pass

class Person(object):
    def show(self):
        pass

if __name__ == "__main__":
    show_type(1)
    show_type(1.5)
    show_type(123456789L)
    show_type('hi')
    show_type(fun())
    show_type(Person)
    show_type(Person())
    show_type(Person.show)

    print("DateTime:{time}".format(time=datetime.datetime.now()))