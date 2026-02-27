import os
import subprocess

def build_app():
    print("🚀 Build process shuru hochche...")
    
    # C কোড কম্পাইল করার কমান্ড
    command = "gcc app.c -o my_first_app"
    
    try:
        # কমান্ড রান করা
        subprocess.check_call(command, shell=True)
        print("✅ Success! Tor app ekhon proshthut.")
        print("👉 Run korte likhbi: ./my_first_app")
    except:
        print("❌ Error! Code-e kothao bhul ache.")

if __name__ == "__main__":
    build_app()
  
