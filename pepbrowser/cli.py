import argparse

def pep_number(num):
    if len(num) > 4 or not num.isdigit():
        raise argparse.ArgumentError(f"Invalid pep number format: {num}")

    return num.zfill(4)


def get_args():
    parser = argparse.ArgumentParser(prog="pepbrowser", description="Browse python enhancement proposals in your terminal")
    parser.add_argument("pep", type=pep_number, help="The number of the pep you wish to see")
    parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Verbose output")
    parser.add_argument("-t", "--theme", action="store_true", dest="theme", default="monokai", help="Theme to use for code blocks")
    
    args = parser.parse_args()
    return args
