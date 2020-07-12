import random

from ply import lex
from ply.yacc import yacc

# =======================================================
# CMBASIC EXAMPLE PROGRAMS
# =======================================================

program0 = """
BEGIN
END
"""

program1 = """
BEGIN
10 RUN
END
"""

program2 = """
BEGIN
10 RUN
20 JUMP
30 SLIDE
END
"""

program3 = """
BEGIN
10 RUN
20 JUMP
30 SLIDE
40 RUN
50 IF TROLL IS NOT ORANGE THEN JUMP
60 IF GEMS IS NOT 6 THEN RUN
END
"""

program4 = """
BEGIN
10 RUN
20 JUMP
30 SLIDE
40 RUN
50 IF GEMS IS NOT 6 THEN JUMP
60 IF GEMS IS 6 THEN RUN ELSE SLIDE
END
"""

program5 = """
BEGIN
10 RUN
20 JUMP
30 SLIDE
40 RUN
50 IF TROLL IS ORANGE THEN JUMP
60 IF TROLL IS NOT PURPLE THEN RUN ELSE SLIDE
END
"""

program6 = """
BEGIN
10 RUN
20 JUMP
30 SLIDE
40 RUN
50 IF TROLL IS ORANGE THEN JUMP
60 IF TROLL IS NOT PURPLE THEN RUN ELSE SLIDE
70 IF TROLL IS NOT PURPLE THEN LOOP
>>> RUN
>>> JUMP
80 RUN
END
"""

program7 = """
BEGIN
10 RUN
20 JUMP
30 SLIDE
40 RUN
50 IF TROLL IS ORANGE THEN JUMP
60 IF TROLL IS NOT PURPLE THEN RUN ELSE SLIDE
70 IF GEMS IS NOT 4 THEN LOOP
>>> RUN
>>> JUMP
80 RUN
90 IF GEMS IS NOT 2 THEN GOTO 30
END
"""

program8 = """
BEGIN
10 RUN
20 IF GEMS IS NOT 2 THEN GOTO 30
30 SLIDE
END
"""

# =======================================================
# Lexer
# =======================================================


tokens = (
    'BEGIN',
    'END',
    'WHOLENUMBER',
    'ACTION',
    'IF',
    'THEN',
    'ELSE',
    'GOTO',
    'LOOP',
    'GEMS',
    'TROLL',
    'INDENT',
    'BOOLOP',
    'COLOR',
)

t_ignore = ' \t'

t_BEGIN = r'BEGIN'
t_END = r'END'
t_IF = r'IF'
t_THEN = r'THEN'
t_ELSE = r'ELSE'
t_GOTO = r'GOTO'
t_LOOP = r'LOOP'
t_INDENT = r'\>\>\>'
t_COLOR = r'ORANGE|PURPLE'
t_GEMS = r'GEMS'
t_TROLL = r'TROLL'
t_ACTION = r'RUN|JUMP|SLIDE'
t_BOOLOP = r'IS(?:\s+NOT)?'


def t_WHOLENUMBER(t):
    r'[1-9][0-9]*'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Invalid Token:", t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


# lexer.input(program)
# for tok in lexer:
#     print(tok)


# =======================================================
# Parser
# =======================================================

def p_prog(p):
    'prog : BEGIN instructions END'
    p[0] = [p[1]] + p[2] + [p[3]]


def p_prog_empty(p):
    'prog : BEGIN END'
    p[0] = [p[1], p[2]]


def p_instructions_multiple(p):
    'instructions : instructions instruction'
    p[0] = p[1] + [p[2]]


def p_instructions_single(p):
    'instructions : instruction'
    p[0] = [p[1]]


def p_instruction(p):
    'instruction : WHOLENUMBER statement'
    p[0] = (p[1], p[2])


def p_action_statement(p):
    'statement : ACTION'
    p[0] = p[1], ()


def p_if_then_action_statement(p):
    'statement : IF cond THEN ACTION'
    p[0] = 'IF_THEN_ACTION', (p[2], p[4])


def p_if_then_else_action_statement(p):
    'statement : IF cond THEN ACTION ELSE ACTION'
    p[0] = ('IF_THEN_ACTION', (p[2], p[4], p[6]))


def p_if_then_goto_statement(p):
    'statement : IF cond THEN GOTO WHOLENUMBER'
    p[0] = ('IF_THEN_GOTO', (p[2], p[5]))


def p_if_then_loop_statement(p):
    'statement : IF cond THEN LOOP actionlist'
    p[0] = ('WHILE_LOOP', (p[2], p[5]))


def p_actionlist_multiple(p):
    'actionlist : actionlist indentedaction'
    p[0] = p[1] + [p[2]]


def p_actionlist_single(p):
    'actionlist : indentedaction'
    p[0] = [p[1]]


def p_indented_action(p):
    'indentedaction : INDENT ACTION'
    p[0] = p[2]


def p_gem_cond(p):
    '''
    cond : GEMS BOOLOP WHOLENUMBER
         | TROLL BOOLOP COLOR
    '''
    p[0] = p[1], p[2], p[3]


parser = yacc()


# =====================================================================
# Interpreter
# =====================================================================

# TODO : load level
# TODO : level should include (map_state_machine, code_template, assets)
# TODO : assets should include(gems, trolls, actions, decisions)
class CMBasicProgram:
    def __init__(self, debug=False):
        self.debug = debug
        self._parser = parser
        self._instructions = []
        self._ic = 0
        self._gems = 0
        self._troll = None
        self._fns = {
            'RUN': self._action_run,
            'JUMP': self._action_jump,
            'SLIDE': self._action_slide,
            'IF_THEN_ACTION': self._if_then_action,
            'IF_THEN_GOTO': self._if_then_goto,
            'WHILE_LOOP': self._while_loop,
        }

    def load(self, user_code):
        self._instructions = self._parser.parse(user_code)

    def run(self):
        while self._ic < len(self._instructions):
            current_instruction = self._instructions[self._ic]
            if current_instruction == 'BEGIN':
                self._print_debug(current_instruction)
                self._ic += 1
            elif current_instruction == 'END':
                self._print_debug(current_instruction)
                self._ic = len(self._instructions)
            else:
                self._process_instruction(current_instruction)

    def _print_debug(self, *args):
        if self.debug:
            print(f'# {" ".join(map(str,args))}')

    def _process_instruction(self, instruction):
        self._ic += 1
        (lineno, (fn, args)) = instruction
        self._print_debug(lineno, fn, args)
        self._fns[fn](*args)

    def _action_run(self):
        print('I am running!')

    def _action_jump(self):
        print('I am jumping!')

    def _action_slide(self):
        print('I am sliding!')

    def _if_then_action(self, cond, action, alt_action=None):
        if self._test(*cond):
            self._fns[action]()
        elif alt_action:
            self._fns[alt_action]()

    def _while_loop(self, cond, actions):
        while self._test(*cond):
            for action in actions:
                self._fns[action]()

    def _if_then_goto(self, cond, goto):
        if self._test(*cond):
            try:
                self._ic = [i for i, t in enumerate(self._instructions) if type(t) == tuple and t[0] == goto][0]
            except IndexError:
                current_lineno = self._instructions[self._ic-1][0]
                raise RuntimeError(f"Error lineno({current_lineno})\nGOTO {goto} :no such value: ")

    def _test(self, lhs, op, rhs):
        if lhs == 'GEMS':
            val = self._gems
        else:
            val = self._troll

        ret_val = val == rhs
        if op == 'IS NOT':
            ret_val = not ret_val
        self._print_debug("\t", lhs , op, rhs, "==", ret_val)
        return ret_val


def main(user_code):
    program = CMBasicProgram(debug=True)
    program.load(user_code)
    program.run()


if __name__ == '__main__':
    main(program8)
