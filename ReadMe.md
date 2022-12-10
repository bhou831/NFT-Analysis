# Reference
[NFT Data Extraction Toolkit](https://github.com/a16z/nft-analyst-starter-pack) This Open-Source project provides detailed instruction to setup Alchemy API account and how to parse OpenSea transaction data using the Alchemy.

Below is the sample UI of how alchemy takes the smart contract address and parse information tracing the blockchain.

![alchemy UI](https://user-images.githubusercontent.com/92753818/206876003-4c8170a7-e712-4a1c-9a43-bbefbb84812a.png)

# How to start
For the ease of project isolation, all project dependency files were included in the `requirements.txt` 

```linux
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Once the setup is complete, run
```linux
python3 data_analysis.py
```

The output will be printed in the console.

# Note
The time to parse the entire transaction for an NFT project depends on the number of blocks that are linked to this project. To reduce the step of parsing data and prevent the exposure of the API key and the complexity to set up an alchemy account, I have provided the data used in this project inside `data/` directory. 