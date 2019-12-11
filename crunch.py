
name = "Paul C. Nnaoji"

language = "Python"

def math_function():
	return 9 + 9 

def iter_commands(script_body):
    """
    Sadly, we cannot rely on splitting commands by ";" since it could be
    part of a comment. So we need to make more complicated things to split
    based on commands
    """
    cmd_num, line_num, cmd_start_line = 1, 0, 1
    cmd = []

    for _line in script_body.splitlines():
        line_num += 1
        line = _line.strip()
        cmd.append(_line)  # Append original unstripped line
        if line.endswith(";") and not line.startswith("#"):
            yield (line_num, cmd_start_line, cmd_num, "\n".join(cmd))
            cmd_num += 1
            cmd_start_line = line_num + 1
            cmd = [] # my guess is this is a redundant assignment of the 'cmd' variable as array within a loop is not needed and can potentially be a bug if the input of the function is faulty