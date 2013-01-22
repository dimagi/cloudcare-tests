Selenium tests for CloudCare
============================

These are Selenium tests for the CloudCare component of [CommCare HQ][1] written
using [Robot Framework][2].  Copy `Common/Common_Variables.example.txt` to
`Common/Common_Variables.txt` and edit it, then run:

    pip install selenium robotframework robotframework-selenium2library 
    pybot TestCases

 [1]: http://github.com/dimagi/commcare-hq
 [2]: http://code.google.com/p/robotframework/
