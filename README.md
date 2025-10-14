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
