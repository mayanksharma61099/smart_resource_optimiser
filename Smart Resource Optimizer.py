import boto3
from datetime import datetime, timedelta
import traceback

def get_cpu_utilization(instance_id, region_name='ap-south-1', period=180, minutes_ago=5):
    """Retrieves CPU utilization metrics for a given EC2 instance."""
    cloudwatch = boto3.client('cloudwatch', region_name=region_name)

    end_time = datetime.utcnow()
    start_time = end_time - timedelta(minutes=minutes_ago)

    try:
        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[
                {
                    'Name': 'InstanceId',
                    'Value': instance_id
                },
            ],
            StartTime=start_time,
            EndTime=end_time,
            Period=period,
            Statistics=['Average']
        )

        if response['Datapoints']:
            cpu_utilization = sum(dp['Average'] for dp in response['Datapoints']) / len(response['Datapoints'])
            return cpu_utilization
        else:
            return None  # If No data points available.

    except Exception as e:
        print(f"Error retrieving CPU utilization: {e}")
        traceback.print_exc()
        return None

def lambda_handler(event, context):
    """Lambda handler function."""
    instance_id = 'i-0026cd21a95db7f8d'
    cpu_usage = get_cpu_utilization(instance_id)

    if cpu_usage is not None:
        print(f"CPU Utilization for {instance_id}: {cpu_usage:.2f}%")
        # Here we add the scaling logic based on cpu_usage
        # For now, just print the value.
    else:
        print(f"Could not retrieve CPU Utilization for {instance_id}.")

    return {
        'statusCode': 200,
        'body': 'Function executed successfully.'
    }
