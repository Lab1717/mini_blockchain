# Mini Blockchain 🛠️

Welcome to the **Mini Blockchain**! This program lets you experience how **Bitcoin mining** works with simple code. It’s designed for fun, and you’ll learn how blocks are mined and rewards are earned!

### How Mining Works ⛏️

1. **Mining a Block**: To mine a block, you need to find the correct **nonce** (a number) that, when combined with the block’s data, creates a **hash** smaller than a specific target number. This is done using **SHA-256**, a special math function.
   
2. **Difficulty**: Mining becomes harder over time. After every even-numbered block, the **difficulty** increases by **2%**, which means it will take longer to find the right nonce. This keeps mining challenging.

3. **Block Reward**: When a block is mined, the miner earns a reward in **Bitcoin**. The reward starts at **50 BTC** but gets halved every few blocks (called **halving**), just like in real Bitcoin mining.

### Key Terms

- **Hash**: A secret code that represents the data in the block.
- **Nonce**: A number that miners adjust to find the correct hash.
- **Difficulty**: How hard it is to find a valid block. It increases every few blocks.
- **Target**: The number the hash must be smaller than to mine a block.
- **Block Reward**: The Bitcoin earned for mining a block. This decreases over time.

### Why Difficulty Increases

Instead of adjusting the difficulty based on how long mining takes (which would be too complex for this demo), we simply increase the **difficulty** by **2%** after every even-numbered block. This keeps things simple and fun, while still mimicking real-world Bitcoin mining.

### Features

- **Progressive Difficulty**: Difficulty increases by 2% every even-numbered block.
- **Halving Reward**: Block rewards start at 50 BTC and get halved.
- **Wallet**: Track your Bitcoin balance as you mine blocks.
- **Blockchain**: View the blocks you’ve mined so far!

### How to Use

1. **Start Mining**: Begin mining new blocks.
2. **View Blockchain**: Check out the blocks you’ve mined.
3. **View Wallet**: See your total Bitcoin balance.
4. **Wipe Blockchain & Wallet**: Reset everything and start fresh.
5. **Exit**: Close the program when you're done.

### How to Run the Code

1. **Install Python**: Make sure you have Python installed on your computer. You can download it from [python.org](https://www.python.org/).
   
2. **Download the Code**: Copy the Python code into a new file, for example `blockchain.py`.

3. **Run the Program**:
   - Open your terminal or command prompt.
   - Navigate to the folder where your `blockchain.py` file is located.
   - Run the program with the following command:
     ```
     python blockchain.py
     ```

4. **Interact with the Program**:
   - The program will present you with a menu.
   - Choose options to start mining, view the blockchain, check your wallet, or reset everything.

Enjoy mining and exploring how blockchain works!

---

### Local Blockchain Explanation

In this **Mini Blockchain**, the blockchain operates **locally**, meaning there are **no nodes** involved like in a decentralized network. Instead, the entire blockchain and its mining process are managed on your local machine using a simple file system.

1. **Local Blockchain**: All the blocks you mine and their data are stored in a local file on your computer. This file acts as the **"blockchain,"** recording each block as you mine it. There are no other peers or nodes involved in validating or distributing these blocks.

2. **No Decentralization**: Unlike real Bitcoin, which is decentralized and spread across many computers (nodes), this mini blockchain is purely **centralized** on your local machine. Everything is self-contained within the program, and there's no communication with other computers or nodes.

3. **Mining and Difficulty**: The mining algorithm works locally, and difficulty is increased based on the block count, with no external network participants adjusting the difficulty. The process is simplified for educational and fun purposes, and it doesn’t involve network consensus or block propagation.

4. **Blockchain File**: The blockchain itself is stored in a local file (such as a simple text or JSON file), which keeps a record of all the mined blocks. Every time you mine a new block, it’s added to this file, and the mining difficulty is adjusted according to the predefined rules.

5. **Wallet and Rewards**: The Bitcoin rewards you earn from mining are also tracked locally within the program, meaning your balance and rewards are kept in memory and updated in the local system. There's no external ledger like the one used in real-world Bitcoin networks.

In summary, this **Mini Blockchain** is a **local simulation** of the mining process and blockchain creation. It’s a fun way to explore how Bitcoin works at a basic level, but remember, it's not connected to any real network, and there are no other nodes or miners involved. Everything happens on your own machine!
