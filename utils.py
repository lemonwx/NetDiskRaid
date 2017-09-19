
def construct_create_file_cookies(create_file_cookies):
    res = {}
    tmp = [x.strip() for x in create_file_cookies.split(";")]
    for x in create_file_cookies.split(";"):
        x = x.strip()
        idx = x.find("=")
        res[x[:idx]] = x[idx+1:]
    return res