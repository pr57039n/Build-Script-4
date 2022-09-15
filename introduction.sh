#!/bin/bash

echo "Hello! This program will fetch information for cocktails using different scripts."
echo "For now, only the Drink information function will work."

PS3="Select an option (1-4)"
select i in DrinkInformation DrinkInstruction DrinkVideo Exit
do 
    case $i in
    DrinkInformation)
        python3 Cocktails.py
        break
        ;;
    DrinkInstruction)
        echo "Currently unavailable"
        ;;
    DrinkVideo)
        echo "Currently unavailable"
        ;;
    Exit)
        echo "Thank you for trying!"
        exit 0
        ;;
    *)
        echo "Invalid command."
        ;;
    esac
done