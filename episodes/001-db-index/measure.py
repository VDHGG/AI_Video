"""Local SQLite demo for episode 001. Stdlib only. Numbers on screen come from one recorded run, not from a re-run."""

import os
import sqlite3
import statistics
import time

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "demo.db")


def samples(con, sql, n=9):
    con.execute(sql).fetchone()
    out = []
    for _ in range(n):
        t0 = time.perf_counter()
        con.execute(sql).fetchone()
        out.append((time.perf_counter() - t0) * 1000)
    return out


def time_insert(indexed, n=8000, repeats=5):
    vals = []
    data = [(i % 100, "row") for i in range(n)]
    for _ in range(repeats):
        c = sqlite3.connect(":memory:")
        c.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, bucket INTEGER, note TEXT)")
        if indexed:
            c.execute("CREATE INDEX idx_t_bucket ON t(bucket)")
        c.execute("BEGIN")
        t0 = time.perf_counter()
        c.executemany("INSERT INTO t (bucket, note) VALUES (?, ?)", data)
        c.commit()
        vals.append((time.perf_counter() - t0) * 1000)
        c.close()
    return vals


def main():
    if os.path.exists(PATH):
        os.remove(PATH)
    con = sqlite3.connect(PATH)
    con.execute("PRAGMA journal_mode=DELETE")
    con.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, bucket INTEGER, note TEXT)")
    con.executemany(
        "INSERT INTO orders (bucket, note) VALUES (?, ?)",
        [(i % 100, "row") for i in range(50000)],
    )
    con.commit()
    size_before = os.path.getsize(PATH)
    sql = "SELECT count(*) FROM orders WHERE bucket = 7"
    print("PLAN_NO_INDEX")
    for row in con.execute("EXPLAIN QUERY PLAN " + sql):
        print(row[3])
    no_idx = samples(con, sql)
    print("SELECT_NO_INDEX_MS", [round(x, 3) for x in no_idx], "median", round(statistics.median(no_idx), 3))
    con.execute("CREATE INDEX idx_orders_bucket ON orders(bucket)")
    con.commit()
    size_after = os.path.getsize(PATH)
    print("PLAN_INDEX")
    for row in con.execute("EXPLAIN QUERY PLAN " + sql):
        print(row[3])
    with_idx = samples(con, sql)
    print("SELECT_INDEX_MS", [round(x, 3) for x in with_idx], "median", round(statistics.median(with_idx), 3))
    print("SIZE_BEFORE", size_before, "SIZE_AFTER", size_after, "INDEX_BYTES", size_after - size_before)
    print("MATCHES", con.execute(sql).fetchone()[0])
    ins_no = time_insert(False)
    ins_yes = time_insert(True)
    print("INSERT_8000_NO_INDEX_MS", [round(x, 1) for x in ins_no], "median", round(statistics.median(ins_no), 1))
    print("INSERT_8000_INDEX_MS", [round(x, 1) for x in ins_yes], "median", round(statistics.median(ins_yes), 1))
    con.close()
    os.remove(PATH)
    print("DB_REMOVED")


if __name__ == "__main__":
    main()
