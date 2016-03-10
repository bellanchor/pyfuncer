## 用处 Usage 

根据数学等式，生成python函数

Generate python funtions from math equation.

## 使用步骤 Steps

以*fin_model*为例。

Let's take *fin_model* as an example. Don't bother yourself with the name, it's just nothing.

1. 编写fin_model.func文件，填写数学等式。Create fin_model.func, and math equations in it.
    
    注意，因为程序问题:
    Attention: 

    1. 所有变量不可包含数字 You can not use any digit in any variable name
    2. 等式需要写在一行 You have to keep the equation in one line

2. 编写fin_model.yaml映射文件。所有fin_model.func中使用到的变量名应该能在fin_model.yaml中找到。 Create fin_model.yaml file, to set the mapping of the variable in the fin_model.func

3. 运行 Run

    ```
    python make_func.py fin_model > test.py
    ```
    也可把make_func.py放进linux下$PATH目录下，并添加可执行权限，随处可用