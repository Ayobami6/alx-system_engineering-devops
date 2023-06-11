**Postmortem:** Apache returning error 500

**Date:** June 6, 2023

**Summary:** The purpose of the incident analysis is to analyze and learn from the incident of Apache2 500 error which resulted in service outage and impacted our user experience.
Incident Description: June 6, at exactly 12:00 pm, users started reporting inability to access our website due to internal server error 500, the incident lasted for about 4 hours before service was fully restored.

**Root Cause Analysis:**

- Why did this happen?: The web server couldn’t access the file needed to render the web page
- Why couldn’t the server access the file?: The file to be rendered was not available
- Why was the file not available?: The filename was incorrect
- Why was the filename incorrect?: There wasn’t a proper testing measure in place
- Why wasn’t there a proper testing inplace?: Staffs has little or no knowledge of functional and unit testing
- Why do staffs have little or no knowledge of functional and unit testing?: There is no proper training on testing

**Impact Assessment:** The outage lasted for about 4 hours, resulting in loss of finances and users frustration. Approximately 10,000 users were affected by the incident, resulting in users negative feedbacks

**Response and Resolution:** The incident was immediately forwarded to the operations and development teams on call which I was part, we started investigating the issue using strace to diagnose the running process of web server while trying to access the server. Finally we were able to identify the file not found error which is due to wrong filename, we then implemented the fix by renaming the file to get the server back online and active.

**Lesson learned:**

- Ensuring proper team training
- The team should prioritize robust testing before production
- Proactive monitoring of the web servers

**Preventive Measures:**

- Implement automated monitoring and alerting system
- Implement robust testing

**Recommendation:**

- Regular team training on testing
- Implement automated monitoring system

**Conclusion:**
The incident analysis highlighted the need for improved knowledge sharing, testing and proactive monitoring.
