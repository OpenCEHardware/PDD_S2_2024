from datetime import datetime
import os
import re
from enum import Enum

import Utils as U
import yaml_reader as yr
#=======================================================================================================
# Enums
#=======================================================================================================
class Sources(Enum):
    QUARTUS     = "quartus"
    COCOTB      = "cocotb"
    SIM         = "sim"
#=======================================================================================================
# Globals
#=======================================================================================================
QUARTUS_FILENAME = 'quartus_report.rpt'
g_quartus_file_content = ''


TESTS_ERROR_FILENAME = 'tests_errors.rpt'
g_tests_error_file_content = ''

TESTS_WARNING_FILENAME = 'tests_warnings.rpt'
g_tests_warning_file_content = ''

TESTS_GENERAL_ERROR_FILENAME = 'general_errors.rpt'
g_tests_general_error_file_content = ''

TESTS_GENERAL_WARNING_FILENAME = 'general_warnings.rpt'
g_tests_general_warning_file_content = ''

TEST_PATTERN = r'cocotb.regression\s+running\s+'
NAME_PATTERN = r'[A-z0-9_]+'
#=======================================================================================================
# Defs
#=======================================================================================================
def log(metadata: yr.Metadata, result, source: Sources):
    """Logs the output of the tests based on the source.

    Parameters:
    - metadata: Metadata object containing error and warning patterns.
    - result: Result object containing stdout, stderr, and return code.
    - source: Enum source indicating the type of the source.

    Populates global variables with the processed log data for Quartus and Cocotb tests.
    """
    global g_quartus_file_content           \
    ,g_tests_error_file_content             \
    ,g_tests_warning_file_content           \
    ,g_tests_general_error_file_content     \
    ,g_tests_general_warning_file_content

    stdout = result.stdout
    stderr = result.stderr
    returncode = result.returncode

    if source.value == Sources.QUARTUS.value:
        if stdout:
            g_quartus_file_content += U.get_dash_line('-') + '\n'
            g_quartus_file_content += 'STDOUT' + '\n'
            g_quartus_file_content += U.get_dash_line('-') + '\n'
            g_quartus_file_content += stdout + '\n'

        if stderr:
            g_quartus_file_content += U.get_dash_line('-') + '\n'
            g_quartus_file_content += 'STDERR' + '\n'
            g_quartus_file_content += U.get_dash_line('-') + '\n'
            g_quartus_file_content += stderr + '\n'

        g_quartus_file_content += U.get_dash_line('-') + '\n'
        g_quartus_file_content += 'RETURN CODE' + '\n'
        g_quartus_file_content += U.get_dash_line('-') + '\n'
        g_quartus_file_content += f'{returncode}' + '\n'

    if source.value == Sources.COCOTB.value:

        if stdout:
            # Errors and warnings by test
            g_tests_error_file_content += extract_tests_data(stdout, metadata.test_error_pattern, U.get_dash_line())
            g_tests_warning_file_content += extract_tests_data(stdout, metadata.test_warning_pattern, U.get_dash_line())
            g_tests_general_error_file_content += extract(stdout, metadata.general_error_pattern, U.get_dash_line())
            g_tests_general_warning_file_content += extract(stdout, metadata.general_warning_pattern, U.get_dash_line())

        if stderr:

            g_tests_general_error_file_content += extract(stderr, metadata.general_error_pattern, U.get_dash_line())
            g_tests_general_error_file_content += U.get_dash_line('-') + '\n'
            g_tests_general_error_file_content += 'RETURN CODE' + '\n'
            g_tests_general_error_file_content += U.get_dash_line('-') + '\n'
            g_tests_general_error_file_content += f'{returncode}' + '\n'



def extract_tests_data(stdout, pattern, separator) -> str:
    """Extracts test data based on a given pattern and separates results by test cases.

    Parameters:
    - stdout: The standard output of the executed test.
    - pattern: Regex pattern to identify relevant data.
    - separator: Line separator used for formatting.

    Returns:
    Formatted string with extracted test data for error or warning logs.
    """
    result = ''

    test_start_pattern = re.compile(r"INFO\s+cocotb\.regression\s+running\s+(\S+)\s+\(\d+/\d+\)")
    pattern = re.compile(pattern)
    
    tests = {}
    current_test = None
    collecting = False

    for line in stdout.splitlines():
        if "*************" in line:
            break

        test_start = test_start_pattern.search(line)

        if test_start and not collecting:        
            # print('10')
            current_test = test_start.group(1)
            tests[current_test] = []
            collecting = True

        elif not test_start and collecting and pattern.search(line):
        # elif not test_start and collecting:
            # print('01')
            tests[current_test].append(line)

        elif test_start and collecting:
            # print('11')
            current_test = test_start.group(1)
            tests[current_test] = []
        
        # if not test_start and not collecting:
            # print('00')

    for test, lines in tests.items():
        if lines:
            result += separator + '\n'
            result += test + '\n'
            result += '\n'.join(lines) + '\n'

    return result


def extract(text, pattern, separator) -> str:
    """Extracts lines matching a pattern from text.

    Parameters:
    - text: Text to search for matching lines.
    - pattern: Regex pattern to match.
    - separator: Line separator used for formatting.

    Returns:
    String with all matching lines, formatted with the separator.
    """
    result = ''

    if pattern:
        pattern = re.compile(pattern)

        for line in text.splitlines():
            if pattern.search(line):
                result += line + '\n'
    else:
        result = text

    return result


def report():
    """Generates report files based on the logged data for different types of test outputs.

    Saves reports in a specified directory. Includes metadata such as timestamp and return codes.

    Exceptions:
    Handles OSError if files or directories cannot be created or written to.
    """
    global g_quartus_file_content           \
    ,g_tests_error_file_content             \
    ,g_tests_warning_file_content           \
    ,g_tests_general_error_file_content     \
    ,g_tests_general_warning_file_content

    path = U.g_reports_dir
    time = U.get_dash_line('-') + '\n' + f"Datetime: {datetime.now()}\n"

    try:

        if not os.path.exists(path):
            os.makedirs(path)

        if g_quartus_file_content:
            g_quartus_file_content = time + g_quartus_file_content
            with open(os.path.join(path, QUARTUS_FILENAME), 'w') as report_file:
                report_file.write(g_quartus_file_content)

        if g_tests_error_file_content:
            g_tests_error_file_content = time + g_tests_error_file_content
            with open(os.path.join(path, TESTS_ERROR_FILENAME), 'w') as report_file:
                report_file.write(g_tests_error_file_content)

        if g_tests_warning_file_content:
            g_tests_warning_file_content = time + g_tests_warning_file_content
            with open(os.path.join(path, TESTS_WARNING_FILENAME), 'w') as report_file:
                report_file.write(g_tests_warning_file_content)

        if g_tests_general_error_file_content:
            g_tests_general_error_file_content = time + U.get_dash_line('-') + '\n' + g_tests_general_error_file_content
            with open(os.path.join(path, TESTS_GENERAL_ERROR_FILENAME), 'w') as report_file:
                report_file.write(g_tests_general_error_file_content)

        if g_tests_general_warning_file_content:
            g_tests_general_warning_file_content = time + U.get_dash_line('-') + '\n' + g_tests_general_warning_file_content
            with open(os.path.join(path, TESTS_GENERAL_WARNING_FILENAME), 'w') as report_file:
                report_file.write(g_tests_general_warning_file_content)

    except OSError as e:
        print(f"Error: Can't write {QUARTUS_FILENAME}: {e}")

