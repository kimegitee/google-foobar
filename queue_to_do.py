'''
Level 3, Challenge 3
Queue To Do
===========

You're almost ready to make your move to destroy the LAMBCHOP doomsday device, but the security checkpoints that guard the underlying systems of the LAMBCHOP are going to be a problem. You were able to take one down without tripping any alarms, which is great! Except that as Commander Lambda's assistant, you've learned that the checkpoints are about to come under automated review, which means that your sabotage will be discovered and your cover blown - unless you can trick the automated review system.

To trick the system, you'll need to write a program to return the same security checksum that the guards would have after they would have checked all the workers through. Fortunately, Commander Lambda's desire for efficiency won't allow for hours-long lines, so the checkpoint guards have found ways to quicken the pass-through rate. Instead of checking each and every worker coming through, the guards instead go over everyone in line while noting their security IDs, then allow the line to fill back up. Once they've done that they go over the line again, this time leaving off the last worker. They continue doing this, leaving off one more worker from the line each time but recording the security IDs of those they do check, until they skip the entire line, at which point they XOR the IDs of all the workers they noted into a checksum and then take off for lunch. Fortunately, the workers' orderly nature causes them to always line up in numerical order without any gaps.

For example, if the first worker in line has ID 0 and the security checkpoint line holds three workers, the process would look like this:
0 1 2 /
3 4 / 5
6 / 7 8
where the guards' XOR (^) checksum is 0^1^2^3^4^6 == 2.

Likewise, if the first worker has ID 17 and the checkpoint holds four workers, the process would look like:
17 18 19 20 /
21 22 23 / 24
25 26 / 27 28
29 / 30 31 32
which produces the checksum 17^18^19^20^21^22^23^25^26^29 == 14.

All worker IDs (including the first worker) are between 0 and 2000000000 inclusive, and the checkpoint line will always be at least 1 worker long.

With this information, write a function answer(start, length) that will cover for the missing security checkpoint by outputting the same checksum the guards would normally submit before lunch. You have just enough time to find out the ID of the first worker to be checked (start) and the length of the line (length) before the automatic review occurs, so your program must generate the proper checksum with just those two values.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) start = 0
    (int) length = 3
Output:
    (int) 2

Inputs:
    (int) start = 17
    (int) length = 4
Output:
    (int) 14

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
'''
def xor_range(start, end):
    if start == end:
        return start
    seq_len = end - start + 1
    s_binary = bin(start)[2:]
    e_binary = bin(end)[2:]
    max_len = max(len(s_binary), len(e_binary))
    s_binary = s_binary.zfill(max_len)
    e_binary = e_binary.zfill(max_len)
    result = _xor_range(s_binary, e_binary, seq_len)
    return int(result, 2)

def _xor_range(a, b, seq_len):
    assert len(a) == len(b)
    if a == '0':
        if seq_len // 2 % 2 == 0:
            return '0'
        else:
            return '1'
    if a == '1':
        if (seq_len + 1) // 2 % 2 == 0:
            return '0'
        else:
            return '1'
    a_head = a[0]
    b_head = b[0]
    a_tail = a[-1]
    b_tail = b[-1]
    a_body = a[1:]
    b_body = b[1:]
    if a_head == '0':
        if b_head == '0':
            result = '0'
        else:
            if b_tail == '0':
                result = '1'
            else:
                result = '0'
    else:
        if b_head == '0':
            if a_tail == '0':
                result = '0'
            else:
                result = '1'
        else:
            if a_tail == b_tail:
                result = '1'
            else:
                result = '0'
    return result + _xor_range(a_body, b_body, seq_len)

def answer(start, length):
    origin = start
    result = 0
    for i, offset in enumerate(range(length)):
        start = origin + i*length
        end = start + length - offset - 1
        result = result ^ xor_range(start, end)
    return result
