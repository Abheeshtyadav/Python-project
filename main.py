import qrcode

import sys



def generate_basic_qr():
    """Generates a standard black-and-white QR code."""
    print("\n--- Basic QR Code ---")
    data = input("Enter the URL or text for the QR code: ").strip()
    if not data:
        print("Data cannot be empty. Returning to menu.")
        return

    filename = input("Enter the output filename (e.g., my_qr.png): ").strip()
    if not filename:
        filename = "basic_qr.png"
    if not filename.endswith('.png'):
        filename += '.png'
        
    print("Generating...")
    img = qrcode.make(data)
    img.save(filename)
    print(f"Success! Basic QR code saved as '{filename}' in the current directory.")

def generate_custom_qr():
    """Generates a QR code with custom colors, size, and error correction."""
    print("\n--- Custom QR Code ---")
    data = input("Enter the URL or text for the QR code: ").strip()
    if not data:
        print("Data cannot be empty. Returning to menu.")
        return

    
    try:
        box_size = input("Enter box size (Press Enter for default: 10): ")
        box_size = int(box_size) if box_size else 10
        
        border = input("Enter border thickness (Press Enter for default: 4): ")
        border = int(border) if border else 4
    except ValueError:
        print("Invalid number entered. Using default sizes.")
        box_size = 10
        border = 4

    # Color customization
    fill_color = input("Enter QR code color (e.g., 'black', 'blue', '#FF0000' - default 'black'): ").strip() or "black"
    back_color = input("Enter background color (e.g., 'white', 'yellow' - default 'white'): ").strip() or "white"
    
    filename = input("Enter the output filename (e.g., custom_qr.png): ").strip()
    if not filename:
        filename = "custom_qr.png"
    if not filename.endswith('.png'):
        filename += '.png'

    # Setup QR Code object with High Error Correction (H)
    qr = qrcode.QRCode(
        version=1, # Auto-scales based on data length
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    print("Generating...")
    try:
        # Apply colors and generate image
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(filename)
        print(f"Success! Custom QR code saved as '{filename}' in the current directory.")
    except Exception as e:
        print(f"Error generating QR code. Please ensure your color names/hex codes are valid. Error details: {e}")

def main():
    """Main menu loop."""
    
    while True:
        print("\n" + "="*35)
        print("   🚀 ADVANCED QR CODE MAKER 🚀")
        print("="*35)
        print("1. Create a Basic QR Code (Fast)")
        print("2. Create a Custom QR Code (Colors & Size)")
        
        print("3. Exit")
        print("="*35)
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            generate_basic_qr()
        elif choice == '2':
            generate_custom_qr()

        elif choice == '3':
            print("\nExiting program. Have a great day!")
            sys.exit()
        else:
            print("\nInvalid choice. Please type a number between 1 and 4.")

if __name__ == "__main__":
    main()