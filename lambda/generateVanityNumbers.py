import boto3
import itertools
import json

def generate_vanity_numbers(phone_number):
    # Mapping of digits to their corresponding letters
    digit_mapping = {
        '0': ['0'],
        '1': ['1'],
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'Q', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y', 'Z']
    }
    
    # Generate all possible combinations of letters for each digit
    phone_number_last7digit = phone_number[3:10]
    print('phone_number_last7digit: ', phone_number_last7digit)
    letter_combinations = [digit_mapping[digit] for digit in phone_number_last7digit]
    
    # Generate all possible vanity numbers from the combinations
    vanity_numbers = []
    for combination in itertools.product(*letter_combinations):
        vanity_numbers.append(''.join(combination))
    
    return vanity_numbers

def format_vanity_numbers(vanity_numbers, phone_number):
    # Format vanity numbers with dashes for readability
    print('vanity_numbers: ', vanity_numbers)
    formatted_vanity_numbers = []
    for number in vanity_numbers:
        formatted_number = phone_number[0:3] + number[0:]
        formatted_vanity_numbers.append(formatted_number)
    return formatted_vanity_numbers

def get_best_vanity_numbers(phone_number, num_vanity_numbers):
    # Generate all possible vanity numbers
    all_vanity_numbers = generate_vanity_numbers(phone_number)
    
    # Filter meaningful vanity numbers based on certain criteria (e.g., dictionary words)
    meaningful_vanity_numbers = filter(lambda x: is_meaningful(x), all_vanity_numbers)
    
    # Sort meaningful vanity numbers based on their "meaningfulness"
    sorted_vanity_numbers = sorted(meaningful_vanity_numbers, key=lambda x: rate_meaningfulness(x), reverse=True)
    
    # Return the top n best vanity numbers
    return sorted_vanity_numbers[:num_vanity_numbers]

def is_meaningful(vanity_number):
    # Placeholder function to check if a vanity number is meaningful
    # You can implement your own logic here, such as checking against a dictionary of words
    # For demonstration purposes, we'll just return True for all vanity numbers
    return True
    
def rate_meaningfulness(vanity_number):
    # Placeholder function to rate the meaningfulness of a vanity number
    # You can implement your own logic here, such as scoring based on relevance or memorability
    # For demonstration purposes, we'll just return a fixed score
    return 1
    
def save_to_dynamodb(phone_number, vanity_numbers):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('VanityNumbersTable')  # Replace 'YourTableName' with your actual DynamoDB table name
    
    # Create a dictionary to hold the item to be stored in DynamoDB
    item = {
        'phone_number': phone_number,
        'VanityNumber_1': vanity_numbers[0],
        'VanityNumber_2': vanity_numbers[1],
        'VanityNumber_3': vanity_numbers[2],
        'VanityNumber_4': vanity_numbers[3],
        'VanityNumber_5': vanity_numbers[4]
    }
    
    # Write the item to DynamoDB
    table.put_item(Item=item)

def lambda_handler(event, context):
     # Extract phone number from the event
    phone_number = event['Details']['ContactData']['CustomerEndpoint']['Address']
    
    best_vanity_numbers = get_best_vanity_numbers(phone_number, 5)
    formatted_best_vanity_numbers = format_vanity_numbers(best_vanity_numbers, phone_number)
    
    save_to_dynamodb(phone_number, formatted_best_vanity_numbers)
    
    print("Best Vanity Numbers:")
    for vanity_number in formatted_best_vanity_numbers:
        print(vanity_number)
    
    return {
        'statusCode': 200,
        'body': json.dumps({'BestVanityNumbers': formatted_best_vanity_numbers})
    }