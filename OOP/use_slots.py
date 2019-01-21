class Father(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称


class Son(Father):
    pass


if __name__ == "__main__":
    # 创建实例
    father = Father()
    # 绑定属性name
    father.name = 'tom'
    # 绑定属性age
    father.age = 40
    # ERROR: AttributeError: 'Student' object has no attribute 'score'
    try:
        father.money = 100
    except AttributeError as e:
        print('attribute', e)

    son = Son()
    son.money = 100
    print('son.money = ', son.money)
