from tusha.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_TUSHA_PROMOTIONS_TOPIC_ARN
import boto3

sns_client = boto3.client(
    'sns',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


def all_subscriptions(topic_arn):
    return sns_client.list_subscriptions_by_topic(TopicArn=topic_arn)


def add_subscription(endpoint):
    sns_client.subscribe(
        TopicArn=AWS_TUSHA_PROMOTIONS_TOPIC_ARN,
        Protocol='sms',
        Endpoint=endpoint
    )


def remove_subscription(endpoint):
    subscriptions = sns_client.list_subscriptions_by_topic(TopicArn=AWS_TUSHA_PROMOTIONS_TOPIC_ARN)
    [sns_client.unsubscribe(SubscriptionArn=sub['SubscriptionArn'])
     for sub in subscriptions['Subscriptions'] if sub['Endpoint'] == '+' + endpoint]


def notify_subscriptions(message):
    sns_client.publish(
        TopicArn=AWS_TUSHA_PROMOTIONS_TOPIC_ARN,
        Message=message
    )
