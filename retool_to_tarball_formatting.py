import sys
import os
import tarfile

def combine_file(path_to_re):
    diag_tar = 'tar_ball'
    if not os.path.exists(diag_tar):
        os.makedirs(diag_tar)
    else:
        os.replace(diag_tar, diag_tar)

    out_dir = '%s/nodes' % diag_tar
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    else:
        os.replace(out_dir, out_dir)

    for node in os.listdir(path_to_re[0]):
        node_dir = '%s/%s' % (path_to_re[0], node)
        if node.endswith(".gz"):
            tar = tarfile.open(node_dir, mode='r')
            for member in tar:
                if 'cassandra.yaml' in member.name:
                    f = tar.extractfile(member)
                    content = f.readlines()
                    for line in content:
                        if 'listen_address:' in str(line):
                            ip = str(line[16:].strip())[2:-1]
                            os.rename(node_dir, '%s/%s.tar.gz' % (out_dir,ip))

def indie_file(path_to_re):
    diag_tar = 'tar_ball'
    if not os.path.exists(diag_tar):
        os.makedirs(diag_tar)
    else:
        os.replace(diag_tar, diag_tar)

    out_dir = '%s/nodes' % diag_tar
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    else:
        os.replace(out_dir, out_dir)

    for node in path_to_re:
        if node.endswith(".gz"):
            tar = tarfile.open(node, mode='r')
            for member in tar:
                if 'cassandra.yaml' in member.name:
                    f = tar.extractfile(member)
                    content = f.readlines()
                    for line in content:
                        if 'listen_address:' in str(line):
                            ip = str(line[16:].strip())[2:-1]
                            os.rename(node, '%s/%s.tar.gz' % (out_dir,ip))

option = sys.argv[1]
path_to_re = sys.argv[2:]

if option == '-c' or option == '-combined':
    combine_file(path_to_re)
elif option == '-i' or option == 'individual':
    indie_file(path_to_re)
