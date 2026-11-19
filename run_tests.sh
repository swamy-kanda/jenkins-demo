
#!/bin/bash

gcc -Wall -Wextra -Werror -o test_app test.c

mkdir -p test-reports

./test_app
result=$?

if [ "$result" -eq 0 ]; then
    cat > test-reports/results.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<testsuite name="Embedded C Tests" tests="2" failures="0" errors="0" skipped="0">
    <testcase classname="EmbeddedC" name="Addition test"/>
    <testcase classname="EmbeddedC" name="Second addition test"/>
</testsuite>
EOF
else
    cat > test-reports/results.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<testsuite name="Embedded C Tests" tests="2" failures="2" errors="0" skipped="0">
    <testcase classname="EmbeddedC" name="Addition test">
        <failure message="Test application failed"/>
    </testcase>
    <testcase classname="EmbeddedC" name="Second addition test">
        <failure message="Test application failed"/>
    </testcase>
</testsuite>
EOF
fi

exit "$result"

