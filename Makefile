# Makefile

# Name of your main Python file
MAIN=main.py

# Name of the executable (without extension)
EXEC=main

# Default target: build the executable
all: build

# Build the executable using PyInstaller
build:
	pyinstaller --onefile $(MAIN)

# Run the generated executable from the dist folder
run: build
	./dist/$(EXEC)

# Clean up the build artifacts
clean:
	rm -rf build dist *.spec

.PHONY: all build run clean