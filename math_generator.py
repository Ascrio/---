import sys
import random
import re
from fractions import Fraction
from typing import List, Tuple, Union, Optional, Set
Number = Union[int, Fraction]  # 定义数字类型，可以是整数或分数
def gcd(a: int, b: int) -> int:  # 计算最大公约数
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
class FractionNumber:
    def __init__(self, numerator: int, denominator: int):  # 分数类初始化
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        common_divisor = gcd(numerator, denominator)  # 约分
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor
        if self.denominator < 0:  # 确保分母为正
            self.numerator *= -1
            self.denominator *= -1
    @classmethod
    def from_string(cls, s: str) -> 'FractionNumber':  # 从字符串解析分数
        s = s.strip()
        if "'" in s:  # 处理带分数格式
            parts = s.split("'", 1)
            whole_part = int(parts[0])
            frac_part = parts[1]
            num, den = map(int, frac_part.split('/'))
            total = whole_part * den + num
            return cls(total, den)
        elif '/' in s:  # 处理真分数格式
            num, den = map(int, s.split('/'))
            return cls(num, den)
        else:  # 处理整数格式
            return cls(int(s), 1)
    def to_string(self) -> str:  # 将分数转换为字符串表示
        if self.denominator == 1:
            return str(self.numerator)
        elif abs(self.numerator) > self.denominator:  # 转换为带分数
            whole = self.numerator // self.denominator
            remainder = abs(self.numerator) % self.denominator
            if remainder == 0:
                return f"{whole}"
            else:
                return f"{whole}'{remainder}/{self.denominator}"
        else:  # 真分数格式
            return f"{self.numerator}/{self.denominator}"
    def __add__(self, other: 'FractionNumber') -> 'FractionNumber':  # 加法运算
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return FractionNumber(new_num, new_den)
    def __sub__(self, other: 'FractionNumber') -> 'FractionNumber':  # 减法运算
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return FractionNumber(new_num, new_den)
    def __mul__(self, other: 'FractionNumber') -> 'FractionNumber':  # 乘法运算
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return FractionNumber(new_num, new_den)
    def __truediv__(self, other: 'FractionNumber') -> 'FractionNumber':  # 除法运算
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        return FractionNumber(new_num, new_den)
    def __eq__(self, other: object) -> bool:  # 相等比较
        if not isinstance(other, FractionNumber):
            return False
        return self.numerator == other.numerator and self.denominator == other.denominator
    def is_positive(self) -> bool:  # 检查是否为正数
        return self.numerator > 0
    def value(self) -> Fraction:  # 获取Fraction对象
        return Fraction(self.numerator, self.denominator)
MAX_OPERATORS = 3  # 最大运算符数量
def is_proper_fraction(fraction: FractionNumber) -> bool:  # 检查是否为真分数
    return abs(fraction.numerator) < fraction.denominator and fraction.denominator > 1
def generate_number(r: int) -> FractionNumber:  # 生成随机数
    if r <= 0:
        return FractionNumber(0, 1)
    strategy = random.randint(0, 100)  # 随机选择生成策略
    if strategy < 20:  # 20%概率生成整数
        return FractionNumber(random.randint(0, r - 1), 1)
    elif strategy < 40:  # 20%概率生成真分数
        den = random.randint(2, 20)
        num = random.randint(1, den - 1)
        return FractionNumber(num, den)
    elif strategy < 60:  # 20%概率生成任意分数
        den = random.randint(2, 25)
        max_num = min(den * r - 1, 50)
        num = random.randint(1, max_num)
        return FractionNumber(num, den)
    elif strategy < 80:  # 20%概率生成带分数
        whole = random.randint(0, r - 1)
        if whole == r - 1:
            return FractionNumber(whole, 1)
        else:
            den = random.randint(2, 20)
            max_frac_value = r - whole
            max_num = min(den - 1, int(max_frac_value * den) - 1)
            num = random.randint(0, max_num)
            return FractionNumber(whole * den + num, den)
    else:  # 20%概率完全随机
        den = random.randint(1, 30)
        max_num = r * den - 1
        num = random.randint(0, max_num)
        return FractionNumber(num, den)
def generate_number_for_division(r: int) -> FractionNumber:  # 为除法运算生成合适的数字
    choice = random.randint(0, 3)
    if choice == 0:  # 生成较小的真分数
        den = random.randint(2, 8)
        num = random.randint(1, den - 1)
        return FractionNumber(num, den)
    elif choice == 1:  # 生成稍大的真分数
        den = random.randint(3, 12)
        num = random.randint(1, min(den - 1, 5))
        return FractionNumber(num, den)
    elif choice == 2:  # 生成小整数
        return FractionNumber(random.randint(1, 3), 1)
    else:  # 正常随机生成
        return generate_number(r)
def number_to_string(num: FractionNumber) -> str:  # 数字转字符串
    return num.to_string()
def format_expression(expr: str) -> str:  # 格式化表达式，添加空格
    expr = expr.replace('+', ' + ').replace('-', ' - ').replace('*', ' × ').replace('/', ' ÷ ')
    expr = expr.replace('(', ' ( ').replace(')', ' ) ')
    return ' '.join(expr.split())
class Node:  # 抽象语法树节点基类
    pass
class NumberNode(Node):  # 数字节点
    def __init__(self, value: FractionNumber):
        self.value = value
    def to_string(self) -> str:  # 转换为字符串
        return number_to_string(self.value)
    def evaluate(self) -> FractionNumber:  # 求值
        return self.value
    def get_structure_hash(self) -> str:  # 获取结构哈希值用于去重
        return f"Num:{self.value.numerator}_{self.value.denominator}"
def preprocess_expression(expr: str) -> str:  # 预处理表达式用于求值
    expr = expr.replace('×', '*').replace('÷', '/')  # 替换运算符
    def replace_mixed(match):  # 替换带分数
        whole = match.group(1)
        num = match.group(2)
        den = match.group(3)
        return f"(Fraction({whole}, 1) + Fraction({num}, {den}))"
    expr = re.sub(r'(\d+)\'(\d+)/(\d+)', replace_mixed, expr)
    def replace_fraction(match):  # 替换分数
        num = match.group(1)
        den = match.group(2)
        return f"Fraction({num}, {den})"
    expr = re.sub(r'(\d+)/(\d+)', replace_fraction, expr)
    expr = expr.replace(' ', '')  # 移除空格
    return expr
def evaluate_expression(expression: str) -> FractionNumber:  # 求值表达式
    expr_processed = preprocess_expression(expression)
    try:
        result = eval(expr_processed)  # 使用eval计算表达式
    except Exception as e:
        raise ValueError(f"表达式求值失败：{e}")
    if isinstance(result, Fraction):  # 处理分数结果
        return FractionNumber(int(result.numerator), int(result.denominator))
    elif isinstance(result, int):  # 处理整数结果
        return FractionNumber(result, 1)
    else:
        raise ValueError(f"无法识别的计算结果类型：{type(result)}")
def compare_answers(exercise_file: str, answer_file: str):  # 比较答案
    correct_indices = []
    wrong_indices = []
    try:
        with open(exercise_file, 'r', encoding='utf-8') as f:
            exercises = f.readlines()
        with open(answer_file, 'r', encoding='utf-8') as f:
            answers = f.readlines()
        if len(exercises) != len(answers):  # 检查题目和答案数量是否匹配
            print(f"❌ 错误：题目数量({len(exercises)}) 与答案数量({len(answers)}) 不相等。")
            return
        correct = 0
        total = len(exercises)
        for i, (ex_line, ans_line) in enumerate(zip(exercises, answers)):  # 逐题比较
            ex_line = ex_line.strip()
            ans_line = ans_line.strip()
            if not ex_line.endswith('='):  # 检查题目格式
                print(f"[第{i + 1}题] 题目格式错误，缺少 '='：{ex_line}")
                wrong_indices.append(i + 1)
                continue
            expr = ex_line[:-1].strip()
            try:
                correct_ans_obj = evaluate_expression(expr)  # 计算正确答案
                correct_ans = correct_ans_obj.to_string()
                user_ans_obj = FractionNumber.from_string(ans_line)  # 解析用户答案
                user_ans = user_ans_obj.to_string()
                if correct_ans == user_ans:  # 比较答案
                    print(f"[第{i + 1}题] ✅ 正确！题目：{expr} =，你的答案：{user_ans}，正确答案：{correct_ans}")
                    correct += 1
                    correct_indices.append(i + 1)
                else:
                    print(f"[第{i + 1}题] ❌ 错误！题目：{expr} =，你的答案：{user_ans}，正确答案：{correct_ans}")
                    wrong_indices.append(i + 1)
            except Exception as e:
                print(f"[第{i + 1}题] ⚠️ 解析失败！题目：{ex_line}，你的答案：{ans_line}，错误：{e}")
                wrong_indices.append(i + 1)
        print(f"\n📊 批改完成！总题数：{total}，正确：{correct}，错误：{total - correct}")
        with open("Grade.txt", "w", encoding="utf-8") as grade_file:  # 写入成绩文件
            grade_file.write(f"Correct: {len(correct_indices)} ({', '.join(map(str, correct_indices))})\n")
            grade_file.write(f"Wrong: {len(wrong_indices)} ({', '.join(map(str, wrong_indices))})")
        print("\n✅ 统计结果已写入文件：Grade.txt")
    except Exception as e:
        print(f"批改时发生错误：{e}")
class BinaryOpNode(Node):  # 二元运算符节点
    def __init__(self, op: str, left: Node, right: Node):
        self.op = op
        self.left = left
        self.right = right
    def to_string(self) -> str:  # 转换为字符串表达式
        left_str = self.left.to_string()
        right_str = self.right.to_string()
        op_map = {'+': '+', '-': '-', '*': '×', '/': '÷'}  # 运算符映射
        return f"({left_str} {op_map[self.op]} {right_str})"  # 添加括号确保优先级
    def evaluate(self) -> FractionNumber:  # 求值运算
        l = self.left.evaluate()
        r = self.right.evaluate()
        if self.op == '+':  # 加法
            return l + r
        elif self.op == '-':  # 减法，检查结果非负
            if l.value() < r.value():
                raise ValueError("Subtraction would result in negative.")
            return l - r
        elif self.op == '*':  # 乘法
            return l * r
        elif self.op == '/':  # 除法，检查除数和结果
            if r.numerator == 0:
                raise ZeroDivisionError("Division by zero")
            res = l / r
            if not is_proper_fraction(res):  # 检查结果为真分数
                raise ValueError("Division result must be a proper fraction (|numerator| < denominator and denominator > 1).")
            return res
        else:
            raise ValueError(f"Unknown operator {self.op}")
    def get_structure_hash(self) -> str:  # 获取结构哈希，用于去重检测
        left_hash = self.left.get_structure_hash()
        right_hash = self.right.get_structure_hash()
        if self.op in '+*':  # 对于交换律运算符，标准化顺序
            if left_hash > right_hash:
                left_hash, right_hash = right_hash, left_hash
        return f"Bin:{self.op}:{left_hash}:{right_hash}"
class UnaryParenNode(Node):  # 括号节点
    def __init__(self, child: Node):
        self.child = child
    def to_string(self) -> str:  # 添加括号
        return f"({self.child.to_string()})"
    def evaluate(self) -> FractionNumber:  # 求值子表达式
        return self.child.evaluate()
    def get_structure_hash(self) -> str:  # 括号不影响结构哈希
        return f"Paren:{self.child.get_structure_hash()}"
def generate_expression(r: int, max_ops: int = MAX_OPERATORS) -> Tuple[str, FractionNumber, str]:  # 生成表达式
    operators = ['+', '-', '*', '/']
    num_tries = 0
    max_tries = 1000  # 最大尝试次数
    while num_tries < max_tries:
        num_tries += 1
        try:
            nodes = []
            ops = []
            num_numbers = random.randint(2, min(4, max_ops + 1))  # 随机确定数字数量
            if num_numbers - 1 > max_ops:
                continue
            for _ in range(num_numbers):  # 生成数字节点
                nodes.append(NumberNode(generate_number(r)))
            for _ in range(num_numbers - 1):  # 生成运算符
                op = random.choice(operators)
                ops.append(op)
            def build_tree(nodes, ops, r):  # 递归构建表达式树
                if not ops:
                    return nodes[0]
                idx = random.randint(0, len(ops) - 1)  # 随机选择运算符位置
                op = ops[idx]
                left = nodes[idx]
                right = nodes[idx + 1]
                if op == '/':  # 特殊处理除法运算
                    max_retries = 10
                    for retry in range(max_retries):
                        try:
                            left_val = left.evaluate()
                            right_val = right.evaluate()
                            if right_val.numerator != 0:  # 检查除数非零
                                result = left_val / right_val
                                if is_proper_fraction(result):  # 检查结果为真分数
                                    break
                            if retry < max_retries - 1:  # 重试生成合适的除数
                                nodes[idx + 1] = NumberNode(generate_number_for_division(r))
                                right = nodes[idx + 1]
                        except:
                            if retry < max_retries - 1:
                                nodes[idx + 1] = NumberNode(generate_number_for_division(r))
                                right = nodes[idx + 1]
                bin_node = BinaryOpNode(op, left, right)  # 创建二元运算符节点
                new_nodes = nodes[:idx] + [bin_node] + nodes[idx + 2:]  # 合并节点
                new_ops = ops[:idx] + ops[idx + 1:]  # 移除已使用的运算符
                return build_tree(new_nodes, new_ops, r)  # 递归构建
            try:
                root = build_tree(nodes, ops, r)  # 构建表达式树
                expr_str = root.to_string()  # 获取表达式字符串
                val = root.evaluate()  # 计算表达式值
                op_count = sum(1 for c in expr_str if c in '+-×÷')  # 统计运算符数量
                if op_count > max_ops:  # 检查运算符数量限制
                    continue
                structure_hash = root.get_structure_hash()  # 获取结构哈希
                return expr_str, val, structure_hash
            except Exception as e:
                continue
        except Exception:
            continue
    raise RuntimeError("Failed to generate valid expression after many tries.")  # 生成失败
def is_duplicate(new_hash: str, existing_hashes: Set[str]) -> bool:  # 检查是否重复
    return new_hash in existing_hashes
def generate_exercises(n: int, r: int):  # 生成练习题
    exercises = []
    answers = []
    hashes = set()  # 用于存储已生成题目的哈希值
    count = 0
    attempts = 0
    max_attempts = n * 10  # 最大尝试次数
    while count < n and attempts < max_attempts:  # 生成指定数量的题目
        attempts += 1
        try:
            expr_str, ans, struct_hash = generate_expression(r)
            if not is_duplicate(struct_hash, hashes):  # 检查是否重复
                raw_expr = expr_str
                if len(raw_expr) >= 2 and raw_expr.startswith('(') and raw_expr.endswith(')'):  # 移除外层括号
                    raw_expr = raw_expr[1:-1].strip()
                exercises.append(raw_expr + " =")  # 添加等号
                answers.append(ans)
                hashes.add(struct_hash)  # 记录已生成的题目
                count += 1
        except:
            continue
    if count < n:  # 警告信息
        print(f"Warning: Only generated {count} unique exercises after many attempts.", file=sys.stderr)
    with open("Exercises.txt", "w", encoding="utf-8") as f:  # 写入题目文件
        for ex in exercises:
            f.write(ex + "\n")
    with open("Answers.txt", "w", encoding="utf-8") as f:  # 写入答案文件
        for ans in answers:
            f.write(ans.to_string() + "\n")
    print(f"Generated {count} exercises saved to Exercises.txt and Answers.txt")  # 输出结果
def main():  # 主函数
    args = sys.argv[1:]
    if not args:  # 检查参数
        print("❌ 未提供任何参数。")
        print("用法：")
        print("  生成题目：python math_generator.py -n <题目数量> -r <数值范围>")
        print("  批改答案：python math_generator.py -e <exercises.txt> -a <answers.txt>")
        return
    n = None
    r = None
    ex_file = None
    ans_file = None
    i = 0
    while i < len(args):  # 解析命令行参数
        arg = args[i]
        if arg == '-n':  # 处理题目数量参数
            if i + 1 < len(args):
                try:
                    n = int(args[i + 1])
                    i += 2
                except ValueError:
                    print("❌ 错误：-n 后必须跟一个整数，表示题目数量。例如：-n 10")
                    return
            else:
                print("❌ 错误：-n 后缺少题目数量。例如：-n 10")
                return
        elif arg == '-r':  # 处理数值范围参数
            if i + 1 < len(args):
                try:
                    r = int(args[i + 1])
                    if r < 1:
                        print("❌ 错误：-r 后的数值范围必须 >= 1，例如：-r 10")
                        return
                    i += 2
                except ValueError:
                    print("❌ 错误：-r 后必须跟一个整数，表示数值范围。例如：-r 10")
                    return
            else:
                print("❌ 错误：-r 后缺少数值范围。例如：-r 10")
                return
        elif arg == '-e':  # 处理题目文件参数
            if i + 1 < len(args):
                ex_file = args[i + 1]
                i += 2
            else:
                print("❌ 错误：-e 后缺少题目文件名。例如：-e Exercises.txt")
                return
        elif arg == '-a':  # 处理答案文件参数
            if i + 1 < len(args):
                ans_file = args[i + 1]
                i += 2
            else:
                print("❌ 错误：-a 后缺少答案文件名。例如：-a Answers.txt")
                return
        else:  # 处理未知参数
            print(f"⚠️ 忽略未知参数：{arg}")
            i += 1
    if n is not None and r is not None:  # 生成题目模式
        generate_exercises(n, r)
    elif ex_file is not None and ans_file is not None:  # 批改答案模式
        compare_answers(ex_file, ans_file)
    else:  # 参数不完整
        print("❌ 参数不完整或无效。")
        print("请按如下方式运行：")
        print("  生成题目：python math_generator.py -n <题目数量> -r <数值范围>")
        print("  批改答案：python math_generator.py -e <exercises.txt> -a <answers.txt>")
if __name__ == '__main__':
    main()