'''
After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6
After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?
'''


def load():
    cmds = []
    with open('./input.txt') as f:
        for l in f.readlines():
            cmd, n = l.strip().split(' ')
            n = int(n)
            cmds.append((cmd, n))
    return cmds


def terminates(cmds):
    acc = 0
    i = 0
    visited = set()
    while i not in visited:
        if i >= len(cmds):
            return acc
        visited.add(i)
        cmd, n = cmds[i]
        if cmd == 'acc':
            acc += n
            i += 1
        elif cmd == 'jmp':
            i += n
        elif cmd == 'nop':
            i += 1
        else:
            raise Exception()
    return None


def run():
    cmds = load()
    for i in range(len(cmds)):
        original = cmds[i]
        cmd, n = original
        if cmd == 'jmp':
            cmds[i] = ('nop', n)
        elif cmd == 'nop':
            cmds[i] = ('jmp', n)
        result = terminates(cmds)
        if result is not None:
            return result
        cmds[i] = original


print(run())
