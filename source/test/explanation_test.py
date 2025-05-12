#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
# http://aws.amazon.com/apache2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
"""
Test script to verify that the EXPLANATION.md file is properly referenced in the README.md.
"""

import os
import sys

def test_explanation_reference():
    """Test that README.md references EXPLANATION.md."""
    # Get the repository root directory
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    
    # Check if EXPLANATION.md exists
    explanation_path = os.path.join(repo_root, 'EXPLANATION.md')
    if not os.path.exists(explanation_path):
        print("ERROR: EXPLANATION.md file does not exist")
        return False
    
    # Check if README.md references EXPLANATION.md
    readme_path = os.path.join(repo_root, 'README.md')
    if not os.path.exists(readme_path):
        print("ERROR: README.md file does not exist")
        return False
    
    with open(readme_path, 'r') as f:
        readme_content = f.read()
    
    if 'EXPLANATION.md' not in readme_content:
        print("ERROR: README.md does not reference EXPLANATION.md")
        return False
    
    if '[EXPLANATION.md](EXPLANATION.md)' not in readme_content:
        print("ERROR: README.md does not contain a proper link to EXPLANATION.md")
        return False
    
    print("SUCCESS: README.md properly references EXPLANATION.md")
    return True

if __name__ == "__main__":
    success = test_explanation_reference()
    sys.exit(0 if success else 1)