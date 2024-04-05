def find_accuracy(x_an, x0):
    acc = 0
    if x0 > 0:
        len_x0 = len(str(x0)) - 2
        if format(x_an, ".6f")[2] != format(x0, ".6f")[2]:
            return acc
        else:
            acc += 1
            len_x0 -= 1
            if len_x0 == 0:
                return acc
            if format(x_an, ".6f")[3] == format(x0, ".6f")[3]:
                acc += 1
                len_x0 -= 1
                if len_x0 == 0:
                    return acc
                if format(x_an, ".6f")[4] == format(x0, ".6f")[4]:
                    acc += 1
                    len_x0 -= 1
                    if len_x0 == 0:
                        return acc
                    if format(x_an, ".6f")[5] == format(x0, ".6f")[5]:
                        acc += 1
                        len_x0 -= 1
                        if len_x0 == 0:
                            return acc
    else:
        len_x0 = len(str(x0)) - 3
        if (format(x_an, ".6f")[3] != format(x0, ".6f")[3]) or (format(x_an, ".6f")[1] != format(x0, ".6f")[1]):
            return acc
        else:
            acc += 1
            len_x0 -= 1
            if len_x0 == 0:
                return acc
            if format(x_an, ".6f")[4] == format(x0, ".6f")[4]:
                acc += 1
                len_x0 -= 1
                if len_x0 == 0:
                    return acc
                if format(x_an, ".6f")[5] == format(x0, ".6f")[5]:
                    acc += 1
                    len_x0 -= 1
                    if len_x0 == 0:
                        return acc
                    if format(x_an, ".6f")[6] == format(x0, ".6f")[6]:
                        acc += 1
                        len_x0 -= 1
                        if len_x0 == 0:
                            return acc
                        if format(x_an, ".6f")[7] == format(x0, ".6f")[7]:
                            acc += 1
                            len_x0 -= 1
                            if len_x0 == 0:
                                return acc
    return acc



