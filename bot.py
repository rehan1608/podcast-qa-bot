import json
import webbrowser
import requests

def load_transcript():
    with open("transcript_segments.json", "r", encoding="utf-8") as f:
        return json.load(f)

def find_relevant_segment(query, segments):
    best_match = None
    highest_count = 0
    
    keywords = query.lower().split()
    for segment in segments:
        text = segment["text"].lower()
        matches = sum(1 for word in keywords if word in text)
        if matches > highest_count:
            highest_count = matches
            best_match = segment
            
    return best_match if best_match else segments[0]

def ask_bot(query):
    segments = load_transcript()
    matched_segment = find_relevant_segment(query, segments)
    
    context = matched_segment["text"]
    start_time_seconds = int(matched_segment["start"])
    
    prompt = (
        "Answer the user's question based strictly on this context from a podcast.\n\n"
        f"Context: {context}\n\n"
        f"Question: {query}"
    )
    
    print("Sending request to Puter AI Endpoint...")
    
    url = "https://api.puter.com/puterai/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response_json = response.json()
        
        # Safe check: if 'choices' exists, use standard parsing
        if "choices" in response_json:
            answer = response_json["choices"][0]["message"]["content"]
        # If Puter returns a direct string error or alternative key
        elif "error" in response_json:
            answer = f"Puter API Error: {response_json['error']}"
        else:
            # Fallback: Just display the raw response text or use context directly
            answer = response_json.get("message", "Could not parse text response, using context fallback:\n" + context)
            
    except Exception as e:
        # Fallback to the text context we found if the network or API completely acts up
        answer = f"Context snippet found: {context} (API parse error: {str(e)})"
    
    # Generate the YouTube link with the exact timestamp parameter (?t=seconds)
    base_url = "https://www.youtube.com/watch?v=Rni7Fz7208c"
    timestamp_url = f"{base_url}&t={start_time_seconds}s"
    
    return answer, timestamp_url, start_time_seconds

if __name__ == "__main__":
    user_query = "What do you emotionally get out of friendship?"
    print(f"User Asked: {user_query}\n")
    
    answer, url, seconds = ask_bot(user_query)
    
    print(f"Bot Answer:\n{answer}\n")
    print(f"Exact Timestamp Match: {seconds} seconds in.")
    print(f"Opening Video Link: {url}")
    
    # Automatically open the browser to that exact timestamp!
    webbrowser.open(url)