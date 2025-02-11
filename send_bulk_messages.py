import pywhatkit as kit
import time

# List of phone numbers in international format (Ensure correct country code)
numbers = [
    "+919212490944", "+919306810361", "+918210459958", "+917404875548", "+919153310960",
    "+919821555044", "+919971127892", "+919315912482", "+917079148143", "+919310300947",
    "+919991844265", "+917982057145", "+917217236447", "+917982416309", "+919810734862",
    "+917991474177", "+917011983734", "+919354729899", "+916387266267", "+919999909017",
    "+917056835684", "+918607257949", "+917042070261", "+919721751131", "+918708979288",
    "+919006094437", "+917982568223", "+917988370289", "+919105154493", "+919622986279",
    "+918102309830", "+918375966871", "+917877622436", "+919717044191", "+916393176635",
    "+916204937707", "+918708957125", "+916388723748", "+919311548217", "+919783389720",
    "+919034748823", "+918287949987", "+918969409090", "+919813544831", "+918579800222",
    "+918447936683", "+919997279639", "+918569934189", "+918608608295", "+918800235233",
    "+919351758872", "+918882806622", "+918368264910", "+919395977954", "+918920833544",
    "+919696709262", "+918595548687", "+919811989572", "+917065372634", "+919650664650"
]

message = "Hello! Please let me know. Are you seriously going to participate in the chess competition? Please confirm."

def send_whatsapp_messages():
    for number in numbers:
        try:
            formatted_number = number.strip()  # Ensure no extra spaces
            
            # Ensure number starts with '+'
            if not formatted_number.startswith("+"):
                formatted_number = "+" + formatted_number.lstrip("+")  # Remove extra '+'
            
            print(f"📩 Sending message to {formatted_number}...")
            kit.sendwhatmsg_instantly(formatted_number, message, wait_time=5, tab_close=True)
            print(f"✅ Message sent to {formatted_number}")
            time.sleep(5)  # Increased delay to prevent blocking
        except Exception as e:
            print(f"❌ Failed to send message to {formatted_number}: {e}")

# Run the function
send_whatsapp_messages()
