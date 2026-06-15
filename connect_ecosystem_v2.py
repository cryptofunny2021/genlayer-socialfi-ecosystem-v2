# connect_ecosystem_v2.py
# Test Script for GenLayer SocialFi Ecosystem v2.0

from genlayer import *

# All deployed contract addresses v2.0
CONTRACTS = {
    "interaction_hub": Address("0xbcC9Dbc141b1f3562237380c2f18700e36abAca6"),
    "reputation": Address("0x77f86b0D8A0230BD612F41F9c638d682f6aBc476"),
    "token": Address("0x698c060E742D37E4742aEf4d790ba1543325C15b"),
    "task": Address("0xBb6cac0BE2C46Eeb3f08191c754DdCBcfcBB096e"),
    "dispute": Address("0x119B813e24a42c085440269c174d504Ec339fa06")
}

def main():
    print("🔗 GenLayer SocialFi Ecosystem v2.0 - Test Connector")
    print("=" * 60)
    
    try:
        hub = gl.contract(CONTRACTS["interaction_hub"])
        print("✅ Connected to Interaction Hub successfully")
        
        print("\n📌 Registering a test interaction...")
        hub.record_interaction()
        
        print("🎉 Interaction registered successfully!")
        print("   → Reputation Score should increase by +10")
        print("   → Dynamic Token should increase by +5")
        print("\n✅ Ecosystem connection test completed!")
        
    except Exception as e:
        print("❌ Error during test:", str(e))

if __name__ == "__main__":
    main()
