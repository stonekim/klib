

import argparse

parser = argparse.ArgumentParser(description="spark antiporn parse args")
parser.add_argument('--input', help='spark input hdfs path', required=True)
parser.add_argument('--output', help='spark output hdfs path', required=True)
parser.add_argument('--batch_size', help='spark batch_size', type=int, default=0)
parser.add_argument('--total_num', help='spark total num', type=int, default=0)
parser.add_argument('--coalesce_num', help='spark coalesce num', type=int, default=0)

args = parser.parse_args()
print args
