import hashlib
import json
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Genesis Block", self.calculate_hash(0, "0", int(time.time()), "Genesis Block"))

    def calculate_hash(self, index, previous_hash, timestamp, data):
        value = f"{index}{previous_hash}{timestamp}{data}"
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_index = latest_block.index + 1
        new_timestamp = int(time.time())
        new_hash = self.calculate_hash(new_index, latest_block.hash, new_timestamp, data)
        new_block = Block(new_index, latest_block.hash, new_timestamp, data, new_hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != self.calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
import requests
from bs4 import BeautifulSoup

def scrape_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text()
    return ""

def verify_content(blockchain, scraped_content):
    for block in blockchain.chain:
        if block.data in scraped_content:
            print(f"Verified content in block {block.index}")
        else:
            print(f"Content in block {block.index} not found in scraped content")

# Example usage
blockchain = Blockchain()
blockchain.add_block("Community response about https://www.nytimes.com/")
blockchain.add_block("Another response about https://www.hindustantimes.com/")


import networkx as nx

def calculate_hits_scores(known_urls):
    G = nx.DiGraph()

    # Add nodes and edges from crawled data
    for url, links in known_urls.items():
        for link in links:
            G.add_edge(url, link)  # Only add outgoing edges

    # Debug: Print the graph edges
    print("Graph edges:")
    print(list(G.edges()))

    # Check if the graph is empty or has isolated nodes
    isolated_nodes = list(nx.isolates(G))
    if len(G) == 0 or isolated_nodes:
        print("The graph has isolated nodes or is empty.")
        print("Isolated nodes:", isolated_nodes)
        return {}, {}

    # Calculate HITS scores
    authority_scores, hub_scores = nx.hits(G, max_iter=100, tol=1.0e-8, normalized=True)

    return authority_scores, hub_scores

# Define the URLs and known outgoing links
known_urls_hindu = {'https://www.hindustantimes.com/': ['https://www.hindustantimes.com/technology', 'https://www.hindustantimes.com/books']}
known_urls_zhdk = {'https://www.zhdk.ch/': ['https://www.zhdk.ch/news/', 'https://www.zhdk.ch/events/']}
known_urls_aljazeera = {'https://www.aljazeera.com/': ['https://www.aljazeera.com/news/', 'https://www.aljazeera.com/opinion/']}
known_urls_nytimes = {'https://www.nytimes.com/': ['https://www.nytimes.com/world/', 'https://www.nytimes.com/opinion/']}
known_urls_fake = {'https://krishi1211.github.io/fake_website/': ['https://www.indianewsnetwork.com', 'https://www.jigyasaonline.org']}

# Combine all URLs and known outgoing links
all_known_urls = {**known_urls_zhdk, **known_urls_aljazeera, **known_urls_nytimes, **known_urls_hindu, **known_urls_fake}

# Apply the HITS algorithm
authority_scores, hub_scores = calculate_hits_scores(all_known_urls)

# Rank the websites based on authority scores
sorted_authority_scores = sorted(authority_scores.items(), key=lambda x: x[1], reverse=True)

# Print the ranked websites based on authority scores
print("Ranked websites based on authority scores:")
for url, score in sorted_authority_scores:
    print(f"{url}: {score}")

# Rank the websites based on hub scores
sorted_hub_scores = sorted(hub_scores.items(), key=lambda x: x[1], reverse=True)

# Print the ranked websites based on hub scores
print("\nRanked websites based on hub scores:")
for url, score in sorted_hub_scores:
    print(f"{url}: {score}")

# Scrape content from a URL and verify with blockchain
scraped_content = scrape_content('https://www.nytimes.com/')
verify_content(blockchain, scraped_content)
