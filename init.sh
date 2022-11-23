solana config set --url http://api.devnet.solana.com
solana-keygen new -o ~/dev.json
solana config set --keypair ~/dev.json
cargo install sugar-cli
solana config set --url https://blue-white-log.solana-devnet.quiknode.pro/7385a1ab13d0333b3d529268ceb99e094bffae2d/
#https://docs.metaplex.com/developer-tools/sugar/guides/preparing-assets
cd /mnt/c/Users/18135/Desktop/SamurAi

cargo install spl-token-cli
spl-token create-token
7BPMi8StE2Pt4AHbsZzjP5B9RRfUXfZ2THuooUpFohGL

spl-token create-account 7BPMi8StE2Pt4AHbsZzjP5B9RRfUXfZ2THuooUpFohGL

spl-token mint 7BPMi8StE2Pt4AHbsZzjP5B9RRfUXfZ2THuooUpFohGL 100


sugar launch

