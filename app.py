# print("hello world")

# a:int = "muzaffar"
# print(a)


# print(dir(locals()['__builtins__']))

from typing import NoReturn
import sys

# ✅ Normal function - returns nothing (None)
def save_patient_record(name: str, age: int) -> None:
    print(f"📝 Patient record saved: {name}, Age: {age}")

# ❌ Emergency function - never returns (NoReturn)
def emergency_shutdown() -> NoReturn:
    print("🚨 Emergency detected! System shutting down.")
    sys.exit(1)  # Program ends here

# --- Test run ---

# Normal patient case
save_patient_record()  # Function runs and ends (returns None)

# Emergency case
response = input("❓ Is there an emergency? (yes/no): ")

if response.lower() == "yes":
    emergency_shutdown()  # Function runs, ends program here
else:
    print("✅ System running normally.")
