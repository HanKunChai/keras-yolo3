import sys
import argparse
from yolo import YOLO,detect_cam
import numpy as np
import yolo
from PIL import Image
def _main():
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    FLAGS = parser.parse_args()
    detect_cam(YOLO(**vars(FLAGS)))

if __name__=="__main__":
    _main()