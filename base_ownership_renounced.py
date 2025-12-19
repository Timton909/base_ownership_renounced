import requests, time

def ownership_renounced():
    print("Base — Ownership Renounced Detector (dev gives up control)")
    seen = set()

    while True:
        try:
            r = requests.get("https://api.dexscreener.com/latest/dex/pairs/base")
            for pair in r.json().get("pairs", []):
                addr = pair["pairAddress"]
                if addr in seen: continue

                age = time.time() - pair.get("pairCreatedAt", 0) / 1000
                if age > 600: continue  # skip old

                if pair.get("ownershipRenounced"):
                    token = pair["baseToken"]["symbol"]
                    print(f"OWNERSHIP RENOUNCED\n"
                          f"{token} — dev surrendered control\n"
                          f"Liq: ${pair['liquidity']['usd']:,.0f}\n"
                          f"https://dexscreener.com/base/{addr}\n"
                          f"→ No more tax changes, mint, or freeze\n"
                          f"→ True community token now\n"
                          f"{'RENOUNCED'*20}")
                    seen.add(addr)

        except:
            pass
        time.sleep(4.1)

if __name__ == "__main__":
    ownership_renounced()
