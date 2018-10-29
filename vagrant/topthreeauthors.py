#! /usr/bin/env python3
import psycopg2
from formatter import repeat_separator


def fetch_top_three_authors():
    conn = psycopg2.connect(database="news",
                            user="vagrant",
                            password="vagrant")
    c = conn.cursor()
    c.execute('''SELECT AUTHORS.NAME, COUNT(PATH) AS hits
                 FROM ARTICLES, AUTHORS, LOG
                 WHERE LOG.STATUS = '200 OK'
                 AND ARTICLES.SLUG = SUBSTR(LOG.PATH, LENGTH('/article/') +1)
                 AND ARTICLES.AUTHOR = AUTHORS.ID
                 GROUP BY AUTHORS.NAME
                 ORDER BY hits DESC;
              ''')
    results = c.fetchall()
    conn.close()
    return results


def layout_top_three_authors():
    print("Top Authors:")
    repeat_separator()
    for items in fetch_top_three_authors():
        print(" The total views for the author '" + str(items[0]) +
              "' are " + str(items[1]) + '.\n')
    repeat_separator()


if __name__ == '__main__':
    layout_top_three_authors()
