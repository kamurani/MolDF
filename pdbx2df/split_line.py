import shlex

def split_line(line: str, delimeter: str = ' ') -> list:
    """
    Split a string line into tokens separated by delimeters, assuming all ' and " in the start character
    or following a delimeter are paired to quote a token.

    Args:
        line (str): line as a string                                                                                                                                                                                                          
        delimeter (str|' '): delimeter to split the line

    Returns:
        A list of tokens: words
    """
    words = []
    # wihtout quotes, using shlex
    if '"' not in line and "'" not in line:
        return shlex.split(line)

    # with quotes
    single_start = False
    double_start = False
    tmp = []
    for i, l in enumerate(line):
        # quoted by single quotes ''
        if i == 0 and l == "'":  # line starting with '
            single_start = True
        elif l == "'" and line[i-1] == delimeter and not double_start and not single_start:  # a new part quoted with ' 
            single_start = True
        elif l == "'" and single_start:  # a part quoted with ' ended
            single_start = False  # reset
        # quoted by double quotes ""
        elif i == 0 and l == '"':  # line starting with "                                                                                                                                                                                     
            double_start = True
        elif l == '"'  and line[i-1] == delimeter and not double_start and not single_start:  # a new part quoted with "
            double_start = True
        elif l == '"' and double_start:  # a part quoted with " ended
            double_start = False  # reset
        elif l in [delimeter, '\n', '\r'] and not single_start and not double_start:   # a part not quoted ended
            if tmp:
                words.append(''.join(tmp))
                tmp = []
        else:  # Other characters including space in quotes
            tmp.append(l)
        if tmp and i == len(line) -1:  # in case no '\r', '\n', or delimeter is at the end
            words.append(''.join(tmp))
    if single_start or double_start:
        raise ValueError(f'Bad line: quotes not paired!')

    return words
