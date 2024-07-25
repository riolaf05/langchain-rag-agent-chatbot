from semantic_router import Route

time_route = Route(
    name="get_time",
    utterances=[
        "what time is it?",
        "when should I eat my next meal?",
        "how long should I rest until training again?",
        "when should I go to the gym?",
    ],
)

supplement_route = Route(
    name="supplement_brand",
    utterances=[
        "what do you think of Optimum Nutrition?",
        "what should I buy from MyProtein?",
        "what brand for supplements would you recommend?",
        "where should I get my whey protein?",
    ],
)

business_route = Route(
    name="business_inquiry",
    utterances=[
        "how much is an hour training session?",
        "do you do package discounts?",
    ],
)

product_route = Route(
    name="product",
    utterances=[
        "do you have a website?",
        "how can I find more info about your services?",
        "where do I sign up?",
        "how do I get hench?",
        "do you have recommended training programmes?",
    ],
)

turn_on_ec2_route = Route(
    name="turn_on_ec2",
    utterances = [
    "Start my EC2 instance.",
    "Power on my AWS virtual machine.",
    "Turn on the EC2 VM.",
    "Activate the AWS EC2 instance.",
    "Boot up my EC2 VM on AWS.",
    "Launch my EC2 instance.",
    "Switch on the EC2 server.",
    "Initialize the AWS EC2 virtual machine.",
    "Power up my EC2 instance.",
    "Turn on my Amazon VM.",
    "Start the EC2 server on AWS.",
    "Activate the virtual machine on EC2.",
    "Begin the EC2 instance.",
    "Switch on my Amazon EC2 instance.",
    "Wake up the EC2 VM.",
    "Enable the EC2 instance.",
    "Start running my EC2 virtual machine.",
    "Fire up the AWS EC2 VM.",
    "Switch on the AWS EC2 instance.",
    "Turn on the cloud VM on EC2.",
    "Power on the virtual machine in AWS.",
    "Bring up the EC2 instance on AWS.",
    "Get my EC2 VM running.",
    "Start the AWS EC2 server.",
    "Turn on the instance in EC2.",
    "Launch the AWS virtual machine.",
    "Activate the EC2 cloud instance.",
    "Start my VM on EC2.",
    "Turn on the Amazon EC2 virtual machine.",
    "Start up the EC2 instance on AWS."
]
)

turn_off_ec2_route = Route(
    name="turn_off_ec2",
    utterances = [
    "Stop my EC2 instance.",
    "Power off my AWS virtual machine.",
    "Turn off the EC2 VM.",
    "Deactivate the AWS EC2 instance.",
    "Shut down my EC2 VM on AWS.",
    "Shutdown my EC2 instance.",
    "Switch off the EC2 server.",
    "Terminate the EC2 instance.",
    "Deactivate the virtual machine on EC2.",
    "Stop running my EC2 virtual machine.",
    "Fire off the AWS EC2 VM.",
    "Switch off the AWS EC2 instance.",
    "Turn off the cloud VM on EC2.",
    "Power off the virtual machine in AWS.",
    "Bring down the EC2 instance on AWS.",
    "Stop the AWS EC2 server.",
    "Turn off the instance in EC2.",
    "Shutdown the AWS virtual machine.",
    "Turn off the EC2 instance.",
    "Stop the EC2 VM.",
    "Deactivate the EC2 cloud instance.",
    "Stop my VM on EC2.",
    "Turn off the Amazon EC2 virtual machine.",
    "Stop running the EC2 instance on AWS."
]
)

search_events= Route(
    name="search_events",
    utterances=[
        "What are the events happening today?",
        "What are the upcoming events?",
        "Can you tell me about the events in my area?",
        "I'm interested in learning more about the events happening in my city.",
        "What events are happening in my area?",
        "Can you provide information about the events in my city?",
        "I want to know about the events happening in my neighborhood.",
        "What events are happening in my neighborhood?",
        "Can you tell me about the events in my area?",
        "I'm interested in learning more about the events happening in my city.",
    ],
)
