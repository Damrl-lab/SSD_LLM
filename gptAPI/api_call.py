import openai
import time
import Levenshtein
import re

from sqlite_utils.cli import query


def calculate_string_similarity_percentage(str1, str2):
    lev_distance = Levenshtein.distance(str1, str2)
    max_len = max(len(str1), len(str2))
    similarity_percentage = ((max_len - lev_distance) / max_len) * 100
    return similarity_percentage


def parse_output(text):
    """
    Parses tail-latency percentiles and degradation ranges from a given report text.
    Returns a dictionary mapping each percentile to a (min, max) tuple of percentage increases.
    """
    pattern = r"(\d{2,2}\.?\d* percentile): ↑ (\d+)[–-](\d+)%"
    matches = re.findall(pattern, text)

    result = {}
    for percentile, low, high in matches:
        result[percentile.strip()] = (int(low), int(high))

    return result


# Set up your OpenAI API key



# Function to communicate with GPT-4 API
def gpt4_response(prompt, api_key, retrieved_data, query):
    openai.api_key = api_key
    prompt_template = prompt + retrieved_data + query


    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt_template}
            ],
            max_tokens=300,
            temperature=0
        )

        # Extract and return the response text
        res = response['choices'][0]['message']['content'].strip()
        res = parse_response(res)
        return res
    except Exception as e:
        print(e)
        print("Rate limit reached. Retrying after a delay...")
        time.sleep(60)  # Delay for 60 seconds and retry
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0
        )

        # Extract and return the response text
        res = response['choices'][0]['message']['content'].strip()
        res = parse_response(res)
        return res


def parse_response(response):
    print(response)
    # Run the parser
    parsed_latency = parse_output(response)
    return parsed_latency

