# Makefile

# Name of your main Python file
MAIN=src/main.py

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

# Run tests
test:
	python -m unittest discover -s tests

# Run Integration Tests
integration: build
	./integration.sh

# Clean up the build artifacts
clean:
	rm -rf build dist *.spec

.PHONY: all build run test integration clean