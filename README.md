# Automated Cloud Compliance Auditor

Automated DevSecOps platform for auditing and remediating AWS resources using AWS Config, Security Hub, Lambda, and related services.


---

## Overview

This project provides an automated compliance auditing and remediation system for AWS environments. It continuously monitors cloud infrastructure against security and compliance standards (e.g., CIS AWS Foundations, HIPAA, PCI-DSS) and integrates compliance checks into CI/CD pipelines. High-risk findings, such as publicly accessible S3 buckets, are automatically remediated.

Key features include:

* Automated detection of non-compliant resources using AWS Security Hub and AWS Config.
* Automatic remediation of critical findings with AWS Lambda (e.g., enforcing S3 Block Public Access).
* Integration into CI/CD pipelines to ensure security and compliance during deployments.
* Notifications and logging of compliance actions for auditing purposes.

---

## Architecture

The solution uses the following AWS services:

* AWS Security Hub – Aggregates security findings and monitors compliance.
* AWS Config – Provides automated compliance checks against defined rules.
* AWS Lambda – Remediates findings automatically (e.g., public S3 buckets).
* Amazon S3 – Storage service used as the main example resource for remediation.
* Amazon SNS – Optional notifications for alerting on findings and remediation actions.
* IAM – Roles and policies to securely allow Lambda and Config to manage resources.
* CloudTrail – Tracks API activity for auditing purposes.
* EventBridge – Triggers Lambda based on Security Hub findings.

---

## Getting Started
### Prerequisites

* AWS account with administrative access.
* AWS CLI configured with credentials.
* Python 3.9+ (for Lambda deployment code).
