#! /usr/bin/env python3
import topthreearticles
import topthreeauthors
import error_log
import sys
sys.stdout = open("output.txt", "w")


def main():
    topthreearticles.layout_top_three_articles()
    topthreeauthors.layout_top_three_authors()
    error_log.layout_error_logs()


if __name__ == '__main__':
    main()
    sys.stdout = open("output.txt", "w")
