# -*- coding:utf-8 -*-
# Author：Steve

product_list = [
    ('iphone', 5000),
    ('Mac Pro', 9800),
    ('Bike', 1000),
    ('Watch', 3200),
    ('Coffee', 33),
    ('Book', 59),
]

shopping_list = []
salary = input("input your salary:")

if salary.isdigit():
    salary = int(salary)
    while True:
        '''下面的for循环无法实现取出商品列表下标
        for item in product_list:
            print(item)
        '''
        # 取商品下标实现：
        '''
        for item in product_list:
            print(product_list.index(item), item)
        '''
        # 取商品下标优化：
        # enumerate使用下标，内容组合，直接取出下标
        for index, item in enumerate(product_list):
            print(index, item)

        user_choice = input("请选择商品：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            # len()直接判断列表长度
            # if user_choice < len(product_list) and user_choice >= 0:
            if 0 <= user_choice < len(product_list):
                product_item = product_list[user_choice]
                if product_item[1] <= salary:     # 买得起
                    shopping_list.append(product_item)    # add choosed-products to shopping list
                    salary -= product_item[1]             # 计算剩余的钱
                    # %s输出对应变量后面对应%(变量1，变量2...)
                    # \033[31;1m %s \033[0m，变量对应输出颜色，31是红色，32是绿色
                    print("Added %s into shopping cart, your current balance is \033[31;5m %s \033[0m" % (product_item,
                                                                                                          salary))
                else:
                    print("\033[41;1m 你的余额只剩 [%s]，请迅速充值 \033[0m" % salary)
                    print("exit...")
                    exit()
            else:
                print("product code [%s] is not exist!" % user_choice)
        elif user_choice == 'q':
            print("----------shopping list----------")
            for p in shopping_list:
                print(p)
            print("your current balance:", salary)
            print("exit...")
            exit()
        else:
            print("invalid choice.")


