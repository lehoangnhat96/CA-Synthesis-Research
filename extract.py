import json
import sys

transcript_path = r"C:\Users\ADMIN\.gemini\antigravity\brain\a3a10d42-34a8-4035-986a-c3a73f524db0\.system_generated\logs\transcript.jsonl"

found_call = None

with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            if 'tool_calls' in data:
                for call in data['tool_calls']:
                    if call['name'] == 'multi_replace_file_content':
                        found_call = call
        except:
            pass

if found_call:
    with open('extracted_texts.txt', 'w', encoding='utf-8') as out:
        for chunk in found_call['args']['ReplacementChunks']:
            out.write("==== TARGET ====\n")
            out.write(chunk['TargetContent'])
            out.write("\n==== REPLACEMENT ====\n")
            out.write(chunk['ReplacementContent'])
            out.write("\n")
