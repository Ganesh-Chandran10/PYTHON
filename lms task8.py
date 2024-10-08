'''AUTHOR:GANESH
08/10/2024
Familiarize time and date in various formats '''

from datetime import datetime
current=datetime.now()
print(current)
format_1=current.strftime("%m-%d-%Y")
print(format_1)
format_2=current.strftime("%A,%m %d,%Y")
print(format_2)
format_3=current.strftime("%A,%m %d,%Y %I %p")
print(format_3)
format_4=current.strftime("%a-%b-%d %I %Z %Y")
print(format_4)
format_5=current.strftime("%a-%b-%d %I %Z %Y")
print(format_5)
print(current.isoformat())
print(current.strftime("%d"))
print(current.strftime("%I"))
print(current.strftime("%m"))
print(current.strftime("%Y"))
