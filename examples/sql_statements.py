import sqlalchemy

# bad
query = "SELECT * FROM foo WHERE id = '%s'" % identifier
query = "INSERT INTO foo VALUES ('a', 'b', '%s')" % value
query = "DELETE FROM foo WHERE id = '%s'" % identifier
query = "UPDATE foo SET value = 'b' WHERE id = '%s'" % identifier
query = """WITH cte AS (SELECT x FROM foo)
SELECT x FROM cte WHERE x = '%s'""" % identifier
# bad alternate forms
query = "SELECT * FROM foo WHERE id = '" + identifier + "'"
query = f"SELECT * FROM foo WHERE id = '{identifier}'"

# bad
cur.execute("SELECT * FROM foo WHERE id = '%s'" % identifier)
cur.execute("INSERT INTO foo VALUES ('a', 'b', '%s')" % value)
cur.execute("DELETE FROM foo WHERE id = '%s'" % identifier)
cur.execute("UPDATE foo SET value = 'b' WHERE id = '%s'" % identifier)
# bad alternate forms
cur.execute("SELECT * FROM foo WHERE id = '" + identifier + "'")
cur.execute(f"SELECT * FROM foo WHERE id = '{identifier}'")

# good
cur.execute("SELECT * FROM foo WHERE id = '%s'", identifier)
cur.execute("INSERT INTO foo VALUES ('a', 'b', '%s')", value)
cur.execute("DELETE FROM foo WHERE id = '%s'", identifier)
cur.execute("UPDATE foo SET value = 'b' WHERE id = '%s'", identifier)

# bug: https://bugs.launchpad.net/bandit/+bug/1479625
def a():
    def b():
        pass
    return b

a()(f"SELECT {val} FROM foo")

# real world false positives
choices=[('server_list', _("Select from active instances"))]
print("delete from the cache as the first argument")
