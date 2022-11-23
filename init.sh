solana config set --url http://api.devnet.solana.com
solana-keygen new -o ~/dev.json
solana config set --keypair ~/dev.json
cargo install sugar-cli
solana config set --url <rpc url>
