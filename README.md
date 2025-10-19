# 软件工程结队项目
## 项目参与成员
### 计科三班 ？？？？？ 郭涛
### 计科三班 3123004548 袁智燊
| 这个作业属于哪个课程 | <[https://edu.cnblogs.com/campus/gdgy/SoftwareEngineering2024](https://edu.cnblogs.com/campus/gdgy/Class34Grade23ComputerScience)> |
| ----------------- | ---------------- |
| 这个作业要求在哪里 | [<https://edu.cnblogs.com/campus/gdgy/Class34Grade23ComputerScience/homework/13477>](https://edu.cnblogs.com/campus/gdgy/Class34Grade23ComputerScience/homework/13479) |
| 这个作业的目标 | <实现一个自动生成小学四则运算题目的命令行程序>   |

声明：本算法实现的测试环境为python 3.11

GitHub链接：https://github.com/Ascrio/3123004548

# PSP表格相关记录

<center>

| PSP2 1    | Personal Software Process Stages | 预估耗时（分钟） | 实际耗时（分钟） |
|---|---|---|---|
| Planning    | 计划    |10    |15    |
| Estimate    | 估计这个任务需要多少时间 | 270   | 330   |
| Development    | 开发    | 10   |15    |
| Analysis    | 需求分析（包括学习新技术） | 40   |30    |
| Design Spec    | 生成设计文档 | 20   | 10   |
| Design Review    | 设计复审 | 15   | 30   |
| Coding Standard   | 代码规范（为目前的开发制定合适的规范） | 30   | 20   |
| Design    | 具体设计 | 40   | 50   |
| Coding    | 具体编码 | 120   | 120   |
| Code Review    | 代码复审 |5    | 10   |
| Test    | 测试（自我测试，修改代码，提交修改） |15    | 20   |
| Reporting    | 报告    | 15   | 10   |
| Test Report    | 测试报告 | 15   | 15   |
| Size Measurement    | 计算工作量 | 20    | 20   |
| Postmortem & Process Improvement Plan | 事后总结，并提出过程改进计划 | 15   | 20   |

</center>

# 模块接口的设计与实现过程

FractionNumber类是核心数据结构类，用来处理分数运算。提供从字符串解析和转换为字符串的功能

Node类族用于构建和处理数学表达式的抽象语法树。这些节点类形成了表达式树结构，便于生成、计算和格式化数学表达式

generate_exercises(n, r)是一个关键的函数，它的作用是生成n道题目并保存到文件

题目生成流程通过递归构建表达式树，并用哈希机制避免重复题目；答案批改流程先比较用户答案和正确答案，再输出统计结果到Grade.txt文件，有模块化、严格的分数机制等设计特点

函数的调用关系如下图所示

<img width="1663" height="685" alt="dc414b5d904a449ffe51ee83cb4b125b" src="https://github.com/user-attachments/assets/9689263e-5980-4429-819f-2a36ae6e9399" />

算法流程图如下图所示

# 代码分析及思路说明

 本代码基于递归思想，设计了表达式树结构，其核心为一共分六部分关键代码，相关思路如下：

 1.分数类FractionNumber：负责封装分数运算，确保分数始终保持最简形式，同时自动处理符号，保证分母始终为正，该类支持带分数表示（如2'1/3）

 2.表达式树结构类BinaryOpNode：使用二叉树表示表达式，便于递归求值和去重，并在求值时进行约束检查（此约束为题目要求约束）

 3.题目生成算法generate_expression：递归构建表达式树，并随机选择运算符位置，该模块还配备了以下处理机制：
 
 (1).除法特殊处理：确保运算生成合理题目

 (2).重试机制：当生成不符合条件的运算表达式时自动重试

 4.去重函数get_structure_hash：为每个表达式生成结构哈希值，对满足交换律的运算符进行左右子节点顺序标准化，并通过哈希集合检测重复题目

 5.数字生成策略函数generate_number：利用完全随机的选择策略，设定20%概率生成整数，20%概率生成真分数，20%生成任意分数，20%概率生成带分数，其余20%完全随机生成数，并确保数值在指定范围内，实际概率可根据需求进行修改

 6.答案批改函数comare_answers：解析题目表达式并计算标准答案，并精确比较分数值而非字符串，最后生成详细的批改报告

 该算法涉及表达式树，去重哈希等算法，具备一定高效性
 
# 模块接口的性能改进

设计之初的代码性能分析图如下

<img width="1586" height="957" alt="1939fbcfd38c0849a92e816a4ad52e3b" src="https://github.com/user-attachments/assets/c42c4264-a9ba-47a4-a063-7115ed0a10e7" />

后经验证发现，该算法耗时成本很高，同时存在以下缺陷

1.最大公约数筛选函数gcd采用的基于遍历的递归算法，该算法效率低下

2.generate_number采用的随机生成算法存在随机性过低，且该情况会随着范围的缩小降低（比如降至-r 1时只会生成0与1的数值），同时一些生成数值的逻辑效率过低，有大量冗余算法

经过代码改进，将gcd函数中基于遍历的递归算法改为欧几里得算法，同时将generate_number函数加入随机性逻辑，优化了部分选数逻辑后，效率有所提高

更正后的代码性能分析图如下

<img width="1955" height="956" alt="fdcaae23c3d0bdc0c3cbab7ccd9932b6" src="https://github.com/user-attachments/assets/9eb1c7cd-737e-4a08-9f0e-9a24f7e83232" />

经比较，更正后的代码性能更优，且能快速生成大量运算题

 # 运行结果展示

 1.生成题目
 
 输入python math_generator.py -n <数值a> -r <数值b>，系统会生成a道范围不大于b的运算题Exercises.txt和对应的答案Answers.txt

<img width="286" height="134" alt="image" src="https://github.com/user-attachments/assets/5f139a0a-22ec-4f64-adb7-53bcf91f986a" />

 具体内容请参考测试运行展示部分

 2.批改题目

 输入python math_generator.py -e <exercise.txt> -a <answer.txt>后，系统会判断指定的答案文件相对于练习文件的对错

 <img width="1614" height="361" alt="image" src="https://github.com/user-attachments/assets/680a7ff0-1020-4e60-93a9-72d6da16e1ad" />

 同时，会将结果存入Grade.txt中

 <img width="718" height="361" alt="image" src="https://github.com/user-attachments/assets/167651e8-6cda-4d69-8732-6ef5724523c3" />

 # 测试运行展示

考虑篇幅限制，此处仅展示10类测试用例

1.基本功能-运算测试

命令行输入python math_generator.py -n 5 -r 10生成5个数值范围不大于10的运算题目，生成对应的两个txt

Exercises.txt内容如下

<img width="650" height="273" alt="image" src="https://github.com/user-attachments/assets/745fe504-929b-4015-bf74-7f893fe697f1" />

Answers.txt内容如下

<img width="414" height="213" alt="image" src="https://github.com/user-attachments/assets/5aab8bea-289b-4820-b55c-ed2abcfb8f37" />

经测试，答案正确且运行结果符合预期

2.参数缺失测试

只输入-n 5，此时命令行会发生报错

<img width="1185" height="189" alt="image" src="https://github.com/user-attachments/assets/744ce1d8-96f1-4fc8-be39-fb86cbb9d09e" />

经测试，答案正确且运行结果符合预期

3.大量数据生成测试

命令行输入python math_generator.py -n 10000 -r 10生成10000个数值范围不大于10的运算题目，生成对应的两个txt

Exercises.txt内容如下

<img width="692" height="780" alt="image" src="https://github.com/user-attachments/assets/443accca-5a7f-41a5-a4db-54b8407d1419" />

Answers.txt内容如下

<img width="415" height="789" alt="image" src="https://github.com/user-attachments/assets/febd36cf-229f-493f-8ffb-a372acac9fc4" />

经测试，生成了10000道运算题，答案正确且运行结果符合预期

4.参数错误测试

命令行输入python math_generator.py -n 10 -r abc检测系统是否报错

输入后系统发生报错，内容如下

<img width="1189" height="78" alt="image" src="https://github.com/user-attachments/assets/23cc4be7-c1d8-4590-a460-1e1159d35eec" />

经测试，结果符合预期

5.异常数量测试

命令行输入python math_generator.py -n 10 -r -1检测系统是否报错

输入后，系统发生报错，内容如下

<img width="1177" height="89" alt="image" src="https://github.com/user-attachments/assets/d7437dd3-c074-4804-92ca-0337343c1abd" />

经测试，结果符合预期

 6.分数生成随机性测试

 为验证分数生成的随机性，命令行输入python math_generator.py -n 10 -r 1检测生成分数情况

 得到Exercises.txt文件，文件内容如下

 <img width="594" height="433" alt="image" src="https://github.com/user-attachments/assets/d62014b6-5261-48f5-901e-4c1a0d210119" />

 可见分数生成随机性很高，验证测试成功

 7.基本功能-批改测试

 命令行输入python math_generator.py -e Exercises.txt -a Answers.txt，系统会生成批改结果

 此处为验证预期结果，将部分题目对应的答案故意修改至错误，再次运行后，系统会生成批改结果，其中包括了答案正确的和答案错误的批改情况说明

 <img width="1614" height="361" alt="image" src="https://github.com/user-attachments/assets/680a7ff0-1020-4e60-93a9-72d6da16e1ad" />

 同时，会将结果存入Grade.txt中

 <img width="718" height="361" alt="image" src="https://github.com/user-attachments/assets/167651e8-6cda-4d69-8732-6ef5724523c3" />

 经过测试，批改功能结果符合预期

 8.空文本测试

 将其中的Exercises.txt改成空的文本，并在命令行输入python math_generator.py -e Exercises.txt -a Answers.txt，系统会发生报错

 <img width="1445" height="78" alt="image" src="https://github.com/user-attachments/assets/32189a02-c2db-4302-bdc3-657d0f8e7ab8" />

 经过测试，结果符合预期

 9.错误文本测试

故意修改Exercises.txt中的运算符号

<img width="463" height="221" alt="image" src="https://github.com/user-attachments/assets/18150459-23d5-47e9-b1cf-e4f8c88922d6" />

修改后运行，系统会批改除了有异常符号的题目的其余部分题目，并在出问题的题目处给予报错信息

<img width="2057" height="367" alt="image" src="https://github.com/user-attachments/assets/57fe6cec-444f-452d-bb48-43f8b5244493" />

经过测试，结果符合预期

 10.文件不存在测试

 删除Answers.txt文件，并运行python math_generator.py -e Exercises.txt -a Answers.txt，系统会发生报错，内容如下

 <img width="1446" height="76" alt="image" src="https://github.com/user-attachments/assets/a0640f25-1bfe-44a9-8721-764f9e5d05d8" />

 经过测试，结果符合预期
 
 # 模块部分异常处理说明

## 异常处理一：规则检查处理

目标： 检查数学运算中不符合题目规则要求的情况

对应代码片段如下：

``` python
def __truediv__(self, other: 'FractionNumber') -> 'FractionNumber': # 除零异常检查
    if other.numerator == 0: # 检查是否存在除数为零的情况
        raise ZeroDivisionError("Cannot divide by zero.")
    new_num = self.numerator * other.denominator
    new_den = self.denominator * other.numerator
    return FractionNumber(new_num, new_den)
def __sub__(self, other: 'FractionNumber') -> 'FractionNumber': # 减法结果负值异常检查
    new_num = self.numerator * other.denominator - other.numerator * self.denominator
    new_den = self.denominator * other.denominator
    return FractionNumber(new_num, new_den)
elif self.op == '-': # 检查是否存在e1 < e2的情况
    if l.value() < r.value():
        raise ValueError("Subtraction would result in negative.")
    return l - r
def is_proper_fraction(fraction: FractionNumber) -> bool: # 真分数约束检查
    return abs(fraction.numerator) < fraction.denominator and fraction.denominator > 1
if op == '/': # 在除法运算后的验证
    res = l / r # 严格检查除法结果是否为真分数
    if not is_proper_fraction(res):
        raise ValueError("Division result must be a proper fraction...")
```

## 异常处理二：表达式解析异常处理

目标：处理用户输入表达式格式错误

对应代码片段如下：

``` python
def evaluate_expression(expression: str) -> FractionNumber:
    expr_processed = preprocess_expression(expression)
    try:
        result = eval(expr_processed)
    except Exception as e:
        raise ValueError(f"表达式求值失败：{e}")
    if isinstance(result, Fraction): # 类型检查
        return FractionNumber(int(result.numerator), int(result.denominator))
    elif isinstance(result, int):
        return FractionNumber(result, 1)
    else:
        raise ValueError(f"无法识别的计算结果类型：{type(result)}")
```

## 异常处理三：文件操作异常处理

目标：确保文件读写操作的可靠性

对应代码片段如下：

``` python
def compare_answers(exercise_file: str, answer_file: str):
    try:
        with open(exercise_file, 'r', encoding='utf-8') as f:
            exercises = f.readlines()
        with open(answer_file, 'r', encoding='utf-8') as f:
            answers = f.readlines() 
        if len(exercises) != len(answers):
            print(f"❌ 错误：题目数量({len(exercises)}) 与答案数量({len(answers)}) 不相等。")
            return
    except Exception as e:
        print(f"批改时发生错误：{e}")
```

## 异常处理四：题目生成重试机制

目标：处理生成过程中的临时错误，确保最终输出

对应代码片段如下：

``` python
def generate_expression(r: int, max_ops: int = MAX_OPERATORS) -> Tuple[str, FractionNumber, str]:
    num_tries = 0
    max_tries = 1000
    
    while num_tries < max_tries:
        num_tries += 1
        try: # 生成逻辑
            return expr_str, val, structure_hash
        except Exception as e:
            continue  # 静默重试
    raise RuntimeError("Failed to generate valid expression after many tries.")
```

## 异常处理五：参数验证异常

目标：确保输入参数的合法性

对应代码片段如下：

``` python
def main():  # 参数解析
    if r < 1:
        print("❌ 错误：-r 后的数值范围必须 >= 1，例如：-r 10")
        return
    except ValueError:
        print("❌ 错误：-n 后必须跟一个整数，表示题目数量。例如：-n 10")
        return
```

 # 项目总结

通过此次结对项目，通过结对编程，代码质量明显提升，减少了很多低级错误，同伴在算法设计方面的经验帮助我更好地理解了表达式树的构建和比较，诸如在解决题目去重问题时，我们共同讨论的多种方案最终找到了最优解，同时通过合作，我们共同攻克了分数运算和表达式生成的难点，在这次合作中，同伴在代码规范和模块化设计方面给了我很多启发，为我后续开发其他项目奠定基础
 
通过这次结对编程项目，我们不仅成功实现了需求规格中的所有功能，还在合作过程中相互学习、共同成长。结对编程模式显著提高了代码质量和开发效率，减少了后期调试的时间。我们也总结出不少彼此的闪光点：袁智燊同学的闪光点是善于编码，且有丰富的调试和性能分析经验。建议以后也可以把代码编写和调试的任务再进一步拆分。郭涛同学的闪光点是能够从整体架构角度思考问题，避免陷入细节陷阱，同时在调试复杂逻辑时表现出极大的耐心和细致

同时在此次项目中，我们也意识到我们在逻辑严谨性上仍旧存在进步空间，同时对代码的问题查找效率略慢，在此后的项目设计中仍需改进，但是总体而言，这次项目设计相当成功，所有的输出均符合期望结果
