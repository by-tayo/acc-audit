import json
import boto3
from typing import Dict, Any

s3 = boto3.client("s3")


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Auto-remediate public S3 buckets detected by AWS Security Hub.
    This function enforces S3 Block Public Access.
    """

    try:
        findings = event.get("detail", {}).get("findings", [])
        for finding in findings:
            resources = finding.get("Resources", [])
            for resource in resources:
                if resource.get("Type") == "AwsS3Bucket":
                    bucket_name = resource.get("Id").split(":::")[-1]

                    s3.put_public_access_block(
                        Bucket=bucket_name,
                        PublicAccessBlockConfiguration={
                            "BlockPublicAcls": True,
                            "IgnorePublicAcls": True,
                            "BlockPublicPolicy": True,
                            "RestrictPublicBuckets": True,
                        },
                    )

                    print(f"Remediated public access for bucket: {bucket_name}")

        return {
            "statusCode": 200,
            "body": json.dumps("S3 remediation completed successfully"),
        }

    except Exception as exc:
        print(f"Error during remediation: {exc}")
        raise
