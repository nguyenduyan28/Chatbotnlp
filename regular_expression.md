## Special Characters:
- '.' : Match any character except a newline. If DOTALL flag has been specified, it will match newline.
- '^' : Matches the start of the string
- '$' : Matches end of string
- '*' : Causes the resulting RE to match 0 or more repittions of the preceding RE. 'ab*' will match ab, a, abbb, abbbbbbbbbbbbbbb.
- '+' : Causes the resulting RE to match 1 or more repittions of the preceding RE. 'ab+' will match ab, abbb, abbbbbbbbbbbbbbb.
- '?' : Causes the resulting RE to match 1 or 0 repititions of preceding RE. 'ab?' will match 'ab' or 'a'
- 