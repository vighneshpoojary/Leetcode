class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        cur = prev = res = 0
        cur_op = "+"
        stack = []

        while i < len(s):
            cur_char = s[i]

            if cur_char.isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                i -= 1

                if cur_op == "+":
                    res += cur
                    prev = cur
                elif cur_op == "-":
                    res -= cur
                    prev = -cur
                elif cur_op == "*":
                    res -= prev
                    res += prev * cur
                    prev = cur * prev
                else:
                    res -= prev
                    res += int(prev / cur)
                    prev = int(prev / cur)

                cur = 0

            elif cur_char == "(":
                stack.append(res)
                stack.append(cur_op)
                res = 0
                cur_op = "+"

            elif cur_char == ")":
                prev_op = stack.pop()
                prev_res = stack.pop()

                if prev_op == "+":
                   res = prev_res + res
                else:
                   res = prev_res - res

                   prev = res

            elif cur_char != " ":
                cur_op = cur_char

            i += 1

        return res