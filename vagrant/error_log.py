#! /usr/bin/env python3
import psycopg2
from formatter import repeat_separator


def error_log_perc():
    conn = psycopg2.connect(database="news",
                            user="vagrant",
                            password="vagrant")
    c = conn.cursor()
    c.execute('''WITH T AS
                        (SELECT DATE(LOG.TIME) AS FAILDATE,
                                ROUND((SUM(CASE WHEN
                                LOG.STATUS = '404 NOT FOUND'
                                THEN 1
                                ELSE 0
                                END
                          ) * 100.0)::DECIMAL /
                        (COUNT(LOG.STATUS)), 1) AS TOTALFAILURES
                        FROM LOG GROUP BY DATE(LOG.TIME)
                        )
                        SELECT CONCAT(T.TOTALFAILURES, '%') AS FAILURE,
                        TO_CHAR(T.FAILDATE, 'DD MONTH YYYY') AS DATE
                        FROM T
                        GROUP BY T.TOTALFAILURES, T.FAILDATE
                        HAVING T.TOTALFAILURES > 1
                        ''')

    results = c.fetchall()
    conn.close
    return results


def layout_error_logs():
    print("Errors:")
    repeat_separator()
    for items in error_log_perc():
        print("The total errors for the date'" + str(items[1]) +
              "' are " + str(items[0]) + '.')
    repeat_separator()


if __name__ == '__main__':
    layout_error_logs()
