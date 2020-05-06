# EmailChecker
A simple CSV email verifier that validates an email with regex. 

This script runs offline, it doesn't check the email with SMTP or any web service.

### Why not validate_email?
Had too many false positives for me.

### Usage

To use the Email Checker script, make sure that your email list is in CSV format and the emails on the 1st column, as in the example.csv file 

Then just run it :
```sh
$ ./checkem.py yourfile.csv
```

This will produce a yourfile_export.csv output with the result of the analysis !
And your done !

License
----

MIT