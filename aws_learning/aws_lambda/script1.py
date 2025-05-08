import boto3

aws_management_console = boto3.session.Session(profile_name='default')
# iam_console = aws_management_console.resource("iam")

print(dir(aws_management_console))
print(aws_management_console.get_available_resources())

# for each_user in iam_console.users.all():
#     print(each_user.name)