def md_new(nrow = 2, ncol = 2, align = None, header = None):
    '''
    Creates a bare bone for generating a markdown table. Alignments and size of the table can be input by users.

    Parameters:
        ncol, nrow : positive integer number of columns and row for the markdown table
        align   : Column alignment: a string of 'l' (left), 'c' (center) or 'r' (right). If align = 'l', all columns are left aligned. e.t.c.
        header   : A string list of len(header) = ncol to be used for the header of the table. Default None.
    Return:
        A string of the markdown source code

    '''

    class InputError(Exception):
        """
        Raised when there is any error from inputs that no base Python exceptions cover.
        """
        pass

    ## check type of ncol and nrow
    if not isinstance(ncol, int) or not isinstance(nrow, int) :
        raise TypeError("'ncol' and 'nrow' expect positive integer number")

    if (ncol <=0 or nrow <=0) and (isinstance(ncol,int) or isinstance(ncol,int)):
        raise InputError("'ncol' and 'nrow' expect positive integer number")

    ## check type of align:
    if not align == None:
        if not isinstance(align, str):
            raise TypeError("Expect a string of 'l', 'c', or 'r'")
        if not len(align) ==1 :
            raise InputError("'align' should be length 1")
        if not align in ["l", "c", "r"]:
            raise InputError("'align' should be either 'l', 'c', or 'r'")

    ## check type of header:
    if not header == None:
        if not all(isinstance(n, str) for n in header) or not isinstance(header,list):
            raise TypeError("Expect a list of strings")
        if len(header) != ncol:
            raise InputError("Expect 'len(header) = ncol'")


    column = ["|    "]
    cols= column * ncol
    cols.append("|")

    # create row format
    row = "".join(cols)
    rows = "\n".join([row]*nrow)

    # create alignment
    l = ["|:---"]
    c = ["|:--:"]
    r = ["|---:"]
    if align == None:
        al = l * ncol
        al.append("|")
        al = "".join(al)
    elif align in ["c","l","r"]:
        al = eval(align) * ncol
        al.append("|")
        al = "".join(al)
    else:
        raise InputError("Expect a string of 'l', 'c', or 'r'")

    # header
    if header == None:
        top = row
    else:
        h =[]
        for name in header:
            head = ["| ", name]
            h.extend(head)
        h.append("|")
        top = "".join(h)

    tbl = [top, al, rows]
    tbl = "\n".join(tbl)
    print(tbl)
    return tbl
