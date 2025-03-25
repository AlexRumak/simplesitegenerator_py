import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple Site Generator")
    parser.add_argument('config', type=str, help='Path to the site.yml file')
    args = parser.parse_args()

    print(f"Using configuration file: {args.config}")
    print("Hello from the executable!")

if __name__ == "__main__":
    main()
