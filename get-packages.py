# Simply look through all dirs and get a list of unique package names.
import os, sys


def main():
    if len(sys.argv) < 1:
        print("Please pass abs path of dir to traverse")
    path=sys.argv[1]
    if not os.stat(path):
        print("no permission to path %s" % path)
    elif os.path.isdir(path):
        pkg_list = set()
        do_work(path, pkg_list)
        pkg_str = ''
        for p in pkg_list:
            pkg_str = p + ',' + pkg_str
        print pkg_str
    else:
        print("Directory %s not found." % path)

def do_work(dirname, pkgs):
    for root, _, files in os.walk(dirname):
        for p in files:
            filename, file_extension = os.path.splitext(p)
            if file_extension == '.go':
                fp = root+'/'+p
                with open(fp, 'r') as f:
                    for line in f.readlines():
                        tokens = line.strip().split()
                        if "package" in tokens and len(tokens) == 2:
                            pkgs.add(tokens[1])
    return pkgs

if __name__ == "__main__":
        main()
