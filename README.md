## 用处 Usage 

根据简单的数学等式，生成python函数

Generate python funtions from basic math equation.

## 需要安装 Requirements

* PyYAML


## 使用步骤 Steps

以*test*为例。

Let's take *test* as an example. Don't bother yourself with the name, it's just nothing.

1. 编写`test.func`文件，填写数学等式。Create `test.func`, add math equations in it.

    *$*: 如果要使用python的函数，则在前面加上`$`

    注意，因为程序问题:
    Attention: 

    1. 所有变量不可包含数字 You can not use any digit in any variable name
    2. 等式需要写在一行 You have to keep the equation in one line

2. 编写`test.yaml`映射文件。所有`test.func`中使用到的变量名应该能在`test.yaml`中找到。 Create `test.yaml` file, to set the mapping of the variable in the test.func

3. 运行 Run

    ```
    python funcer.py test > test.py
    ```
    也可把`funcer.py`放进linux下$PATH目录下，并添加可执行权限，随处可用

    你可以在example中看到实例 See the files in `example`.
