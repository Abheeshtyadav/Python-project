import qrcode


def generate_basic_qr():
    print("\n--- Basic QR Code ---")
    data = input("Enter the URL or text: ").strip()
    if not data:
        print("Data cannot be empty.")
        return

    filename = input("Enter filename (default: basic_qr.png): ").strip()
    if not filename:
        filename = "basic_qr.png"
    if not filename.endswith(".png"):
        filename += ".png"

    img = qrcode.make(data)
    img.save(filename)
    print(f"Saved to {filename}")


def generate_custom_qr():
    print("\n--- Custom QR Code ---")
    data = input("Enter the URL or text: ").strip()
    if not data:
        print("Data cannot be empty.")
        return

    try:
        box_size_input = input("Enter box size (default: 10): ").strip()
        box_size = int(box_size_input) if box_size_input else 10

        border_input = input("Enter border thickness (default: 4): ").strip()
        border = int(border_input) if border_input else 4
    except ValueError:
        print("Invalid number entered. Using defaults.")
        box_size = 10
        border = 4

    fill_color = input("Enter QR color (default 'black'): ").strip() or "black"
    back_color = input("Enter background color (default 'white'): ").strip() or "white"

    filename = input("Enter filename (default: custom_qr.png): ").strip()
    if not filename:
        filename = "custom_qr.png"
    if not filename.endswith(".png"):
        filename += ".png"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    try:
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(filename)
        print(f"Saved to {filename}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    name = "User"
    while True:
        print("\n" + "=" * 30)
        print(f"Welcome, {name}")
        print("=" * 30)
        print("a. Set name")
        print("1. Basic QR Code")
        print("2. Custom QR Code")
        print("3. Exit")
        print("=" * 30)

        choice = input("Select an option: ").strip()

        if choice == "a":
            entered_name = input("Enter your name: ").strip()
            if entered_name:
                name = entered_name
        elif choice == "1":
            generate_basic_qr()
        elif choice == "2":
            generate_custom_qr()
        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()