import hashlib
import json
import time
import os
import random
import string

BLOCKCHAIN_FILE = "blockchain.txt"
WALLET_FILE = "wallet.txt"

# Constants
INITIAL_DIFFICULTY = 19.5
BTC_REWARD = 50
HALVING_INTERVAL = 12
MIN_BTC_REWARD = 1

def get_difficulty(chain):
    if not chain:
        return INITIAL_DIFFICULTY
    prev_difficulty = chain[-1]['difficulty']
    if len(chain) % 2 == 0:
        new_difficulty = prev_difficulty * 1.01
        print(f"\nBlock count reached: {len(chain)}. Increasing difficulty to: {new_difficulty:.2f}")
        return new_difficulty
    return prev_difficulty

def get_block_reward(block_index):
    reward = BTC_REWARD / (2 ** (block_index // HALVING_INTERVAL))
    if block_index % HALVING_INTERVAL == 0 and block_index != 0:
        print(f"\nHALVING OCCURRED AT BLOCK {block_index}!")
        print("BLOCK REWARD HAS BEEN CUT IN HALF. THIS IS DONE TO SLOW DOWN THE CREATION OF NEW BITCOINS, MAINTAINING A FINITE SUPPLY. ")
        print("THE REWARD WILL CONTINUE TO DECREASE UNTIL IT REACHES 0, ENSURING BITCOIN'S SUPPLY IS CAPPED AT 21 MILLION.")
        print("THIS IS PART OF THE BITCOIN ECONOMICS TO MAINTAIN SCARCITY AND VALUE.")
        time.sleep(12)  # Pause for 10 seconds to allow reading
    return max(reward, MIN_BTC_REWARD)

def double_sha256(data):
    return hashlib.sha256(hashlib.sha256(data).digest()).hexdigest()

def convert_hashrate(tries_per_sec):
    """Converts hashrate from H/s to higher units like kH/s, MH/s, GH/s, and TH/s."""
    if tries_per_sec >= 1e12:
        return f"{tries_per_sec / 1e12:.2f} TH/s"
    elif tries_per_sec >= 1e9:
        return f"{tries_per_sec / 1e9:.2f} GH/s"
    elif tries_per_sec >= 1e6:
        return f"{tries_per_sec / 1e6:.2f} MH/s"
    elif tries_per_sec >= 1e3:
        return f"{tries_per_sec / 1e3:.2f} kH/s"
    else:
        return f"{tries_per_sec:.2f} H/s"

def create_block(index, prev_hash, data, difficulty):
    timestamp = int(time.time())
    nonce = 0
    target = 2 ** (256 - int(difficulty))
    print(f"\nMining block #{index}...")
    print(f"Difficulty: {difficulty:.2f}")
    print(f"Target: {hex(int(target))}\n")
    tries = 0
    start_time = time.time()
    while True:
        block_content = {
            'index': index,
            'timestamp': timestamp,
            'data': data,
            'prev_hash': prev_hash,
            'nonce': nonce,
            'difficulty': difficulty
        }
        block_string = json.dumps(block_content, sort_keys=True).encode()
        hash_result = double_sha256(block_string)
        hash_int = int(hash_result, 16)
        tries += 1

        if tries % 100000 == 0:
            elapsed = time.time() - start_time
            hashrate = tries / elapsed if elapsed > 0 else 0
            print(f"Hashes tried: {tries}, Hashrate: {convert_hashrate(hashrate)}, Current nonce: {nonce}, Hash: {hash_result}")

        if hash_int < target:
            block_content['hash'] = hash_result
            elapsed = time.time() - start_time
            print(f"\nBlock #{index} mined in {elapsed:.2f}s!")
            print(f"Nonce: {nonce}")
            print(f"Hash: {hash_result}")
            print(f"Tries: {tries}")
            print(f"Hashrate: {convert_hashrate(tries / elapsed)}")
            print(f"Block data: {data}\n")
            time.sleep(2)
            return block_content
        nonce += 1

def save_block(block):
    with open(BLOCKCHAIN_FILE, 'a') as f:
        f.write(json.dumps(block) + '\n')

def load_blockchain():
    if not os.path.exists(BLOCKCHAIN_FILE):
        return []
    with open(BLOCKCHAIN_FILE, 'r') as f:
        return [json.loads(line) for line in f]

def create_genesis_block():
    # Embed the historical message into the genesis block's data field
    genesis_data = "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"
    return create_block(0, "0" * 64, genesis_data, INITIAL_DIFFICULTY)

def update_wallet(amount, block):
    wallet = load_wallet()
    transaction = {
        'timestamp': time.ctime(block['timestamp']),
        'block_hash': block['hash'],
        'amount': amount
    }
    if 'transactions' not in wallet:
        wallet['transactions'] = []
    wallet['balance'] += amount
    wallet['transactions'].append(transaction)
    with open(WALLET_FILE, 'w') as f:
        json.dump(wallet, f)
    print(f"\n{amount} BTC added to wallet. New balance: {wallet['balance']} BTC")

def load_wallet():
    if not os.path.exists(WALLET_FILE):
        return {'balance': 0, 'transactions': []}
    with open(WALLET_FILE, 'r') as f:
        return json.load(f)

def generate_random_data(length=64):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def print_chain():
    chain = load_blockchain()
    print("\n=== Blockchain ===")
    for block in chain:
        print(f"\nBlock #{block['index']}")
        print(f"Timestamp : {time.ctime(block['timestamp'])}")
        print(f"Data      : {block['data']}")
        print(f"Nonce     : {block['nonce']}")
        print(f"Hash      : {block['hash']}")
        print(f"Prev Hash : {block['prev_hash']}")
        print(f"Difficulty: {block['difficulty']:.2f}")

def view_wallet():
    wallet = load_wallet()
    print(f"\n--- Wallet ---")
    print(f"Balance: {wallet['balance']} BTC")
    print("\n--- Transactions ---")
    for tx in wallet['transactions']:
        print(f"Timestamp: {tx['timestamp']}, Block Hash: {tx['block_hash']}, Amount: {tx['amount']} BTC")

def reset_all():
    if os.path.exists(BLOCKCHAIN_FILE):
        os.remove(BLOCKCHAIN_FILE)
    if os.path.exists(WALLET_FILE):
        os.remove(WALLET_FILE)
    print("Blockchain and wallet have been reset.")

def continuous_mining():
    print("\n--- Mining Started ---")
    chain = load_blockchain()
    if not chain:
        print("Creating genesis block...")
        genesis = create_genesis_block()
        save_block(genesis)
        update_wallet(BTC_REWARD, genesis)
        chain.append(genesis)

    while True:
        last = chain[-1]
        new_difficulty = get_difficulty(chain)
        new_data = generate_random_data()
        new_block = create_block(
            index=last['index'] + 1,
            prev_hash=last['hash'],
            data=new_data,
            difficulty=new_difficulty
        )
        save_block(new_block)
        block_reward = get_block_reward(last['index'] + 1)
        update_wallet(block_reward, new_block)
        chain.append(new_block)

if __name__ == "__main__":
    while True:
        print("\n--- Mini Blockchain ---")
        print("1. Start mining")
        print("2. View blockchain")
        print("3. View wallet")
        print("4. Wipe blockchain and wallet")
        print("5. Exit")
        choice = input("Select: ").strip()
        if choice == '1':
            continuous_mining()
        elif choice == '2':
            print_chain()
        elif choice == '3':
            view_wallet()
        elif choice == '4':
            reset_all()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")
