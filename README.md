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
 ## 设计概述

采用基于余弦相似度算法的词袋模型，设计了该论文查重功能，并通过DocumentComparator类来封装整个查重算法功能，并采用面向对象的方式组织代码，确保模块化和可维护性

 ## 函数设计以及调用模块展示
 ### 核心函数DocumentComparator类包括以下函数

 1._ init _():初始化jieba分词器
 
 2.fetch_document_data(): 读取文档内容
 
 3.process_content(): 对内容进行分词和预处理，同时构建词汇表
 
 4.compute_document_similarity(): 余弦相似度算法计算两个文档的相似度
 
 5.execute_comparison(): 执行完整的比较流程

 ### 辅助函数primary_function()则负责处理命令行参数和程序流程
 ### 各函数之间调用模块关系如下

<img width="5722" height="5824" alt="diagram" src="https://github.com/user-attachments/assets/3fb6d80d-f320-40e4-8548-63a4266eb713" />

 ## 算法设计与流程展示

 1.对指定的文本进行jieba分词器处理，将文本处理成词语序列，同时过滤处理文本中出现的符号

 2.读取源文档和目标文档，并对两个文档进行分词和过滤处理

 3.使用gensim构建词袋模型(Bag-of-Words Model)

 4.计算文本余弦相似度，并将结果标准化到[0,1]范围

 5.输出结果至文件

 核心函数DocumentComparator 流程图如下

<img width="2663" height="6533" alt="4e4ac3f0d27a53bf62d2b7fc46da9462" src="https://github.com/user-attachments/assets/c7543c01-3c7c-4f70-8c60-fc16c0baf788" />

 算法的关键点在于文本分词以及词袋模型的构建，文本分词为文档转换成词频向量做了铺垫，而词袋模型的构建是文本查重算法实现的基础核心
 
 该算法实现简单，无需复杂的语义分析，适合处理大量文档，且对词序不敏感能够实现检测内容重复而非结构化抄袭，同时不依赖词典库

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

 如下展示两个相似文本orig.txt和orig_0.8_add.txt的运行结果

 将两个文本的路径代入后，输入两个txt文件的路径，显示运行结果图如下

 <img width="2549" height="292" alt="image" src="https://github.com/user-attachments/assets/e9c52fee-401d-433d-b425-625aba9d731f" />

 显示结果为99.17%，符合结果预期
 
 # 测试运行展示

考虑篇幅限制，此处仅展示10类测试用例

1.基本功能测试

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

 # 模块部分异常处理说明

 ## 异常一：文档读取阶段异常
 目标：当用户传入的文档路径无效（如文件不存在、无权限、编码错误等），避免程序因 FileNotFoundError、UnicodeDecodeError等异常而中断
 处理方式：使用 try-except捕获所有可能的读取异常，打印具体错误信息，并返回空字符串 ""作为兜底内容
 ```python
 def fetch_document_data(self, document_location):
    try:
        with open(document_location, 'r', encoding='UTF-8') as file_obj:
            return file_obj.read()
    except Exception as error:
        print(f"文档读取异常 {document_location}: {error}")
        return ""
 ```
 对应代码测试片段如下
 ```python
 class TestDocumentFetcher(unittest.TestCase):
    def test_fetch_nonexistent_file(self):
        comparator = DocumentComparator()
        result = comparator.fetch_document_data("dummy_nonexistent_file_12345.txt")
        self.assertEqual(result, "")  # 应返回空字符串
 ```
 ## 异常二：内容处理阶段异常
 目标：对读取到的原始内容进行分词和过滤，但如果传入的内容为空（比如上个阶段读取失败返回了 ""），则直接返回空列表，避免后续处理出错。
 处理方式​​：首先判断 content_data是否为空，如果是，则返回空列表 []，而不是继续分词。
 ```python
 def process_content(self, content_data):
    if not content_data:  # 处理空字符串（包括空文件）
        return []
    segmented_data = jieba.lcut(content_data)
    filtered_result = []
    for segment in segmented_data:
        if re.match(r"[a-zA-Z0-9\u4e00-\u9fa5]", segment):  # 保留中/英文字符和数字
            filtered_result.append(segment)
    return filtered_result
 ```
 对应代码测试片段如下
 ```python
 def test_process_empty_content(self):
    comparator = DocumentComparator()
    result = comparator.process_content("")
    self.assertEqual(result, [])  # 空内容应返回空列表
 ```

# 模型改进建议及使用说明

## 模型改进建议

该模型存在以下局限性

1.对于短文本且近义词占比较多的相似文本，算法难以区分其相似度并会给出低于期望的相似度

2.难以区分极少数可能存在前后文关系的亦或是语序关系的文本

基于该局限性，给出如下可能改进方向

1.引入新模型，考虑词汇序列等信息

2.结合语义向量，使用深度学习模型

## 使用说明

### main.py

运行时，用户需往命令行里输入对应格式

 python main.py [原文文件路径] [抄袭版论文的文件路径] [答案文件路径]

 <img width="2458" height="301" alt="image" src="https://github.com/user-attachments/assets/37a478b1-8d26-4f60-b690-33e9dbe5d6c7" />

输入后，函数将输出结果至答案txt文件中

<img width="744" height="659" alt="image" src="https://github.com/user-attachments/assets/3b8991d8-8238-45e6-a6a1-b3fb56787b4a" />

### paperchecker.py

运行时，需确保main.py文件存在且包含DocumentComparator类,往命令行输入python paperchecker.py即可运行18种单元测试，并给出对应结果

<img width="2412" height="1304" alt="image" src="https://github.com/user-attachments/assets/ed6e93c3-8ecd-4f3e-8395-6d70cc68c98b" />
