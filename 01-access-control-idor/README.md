# Access Control Vulnerability Assessment (IDOR)

## Project Overview
This practical was completed as part of my AltSchool Africa Cybersecurity Capstone.

The assessment examined an Insecure Direct Object Reference (IDOR) vulnerability in a controlled PortSwigger Web Security Academy lab.

## Objective
Identify weaknesses in authorization controls that could allow users to access resources belonging to other users.

## Tools Used
- Burp Suite
- PortSwigger Web Security Academy

## Methodology
1. Examined the application's normal functionality.
2. Identified a transcript download endpoint using predictable file identifiers.
3. Inspected HTTP requests using Burp Suite.
4. Modified a file identifier within the authorized training lab.
5. Observed whether the application enforced ownership checks.

## Findings
The lab application returned another user's transcript when the requested file identifier was changed.

This demonstrated an IDOR vulnerability caused by missing server-side authorization checks.

## Security Impact
- Unauthorized access to sensitive records
- Potential exposure of personal information
- Confidentiality and privacy risks

## Recommended Remediation
- Enforce server-side authorization on every file request.
- Verify resource ownership before granting access.
- Use unpredictable identifiers as an additional safeguard.
- Log and monitor suspicious access attempts.

## Evidence
Sanitized screenshots from the practical will be added.

## Ethical Considerations
This assessment was performed in an intentionally vulnerable educational environment.
