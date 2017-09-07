#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print

print """
<script>
function cpaas()
{
document.location='cpaas.py';
}
</script>
"""
print """
<script>
function cpppaas()
{
document.location='cpppaas.py';
}
</script>
"""
print """
<script>
function pypaas()
{
document.location='pypaas.py';
}
</script>
"""
print """
<script>
function javapaas()
{
document.location='javapaas.py';
}
</script>
"""
print "<h2> CODE PLATFORM!! </h2>"
print """
<input value='C' type='button' onclick='cpaas()' /> <input value='C++' type='button' onclick='cpppaas()' /> <input value='Python' type='button' onclick='pypaas()' /> <input value='Java' type='button' onclick='javapaas()' />
"""


