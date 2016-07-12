# copyediting-scripts
Scripts developed for copyediting work

## find.math.exp.py

This script finds (by default) all math expressions in a .tex file and and creates a new .tex file listing these expression types and providing their token counts, from most to least frequent.  Optionally, an extra argument can be provided for a custom regex search. This argument, if provided, should be the regular expression itself, excluding the r'<...>' wrapper.

If you want to typeset the output file and it requires special packages, custom macros, or other frontmatter to typeset properly, then

1. you may save these in a file called 'frontmatter.tex' and it will automatically be included in the output file, or
2. you may save these in a file of your choice, and when you receive an error during typsetting of the newfile, provide the correct file name at the prompt. 

```
! LaTeX Error: File 'frontmatter.tex' not found.

Type X to quit or <RETURN> to proceed,
or enter new name. (Default extension: tex)

Enter file name: 
```

If you receive the error message, but do not require any additional packages, just hit return.  

Assuming you are performing the default math delimiter search, then you should keep in mind the fact that if there are any escaped $'s or if there are an odd number of $'s in commented-out material, then your output will suffer.  Future additions to this script may guard against these pitfalls.


### Usage

`python find.math.exp.py <source.tex> <newfile.tex> [alternateRegex]`
