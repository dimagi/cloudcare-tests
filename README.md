Selenium tests for CloudCare
============================

These are Selenium tests for the CloudCare component of [CommCare HQ][1] written
using [Robot Framework][2].  First install necessary dependencies:

    pip install selenium robotframework robotframework-selenium2library 

Then copy `Common/Common_Variables.example.txt` to `Common/Common_Variables.txt`
and `Common/Login_Test_Data.example.txt` to `Common/Login_Test_Data.txt` and
edit them appropriately, then run:

    pybot TestCases

 [1]: http://github.com/dimagi/commcare-hq
 [2]: http://code.google.com/p/robotframework/
