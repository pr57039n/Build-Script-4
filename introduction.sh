#!/bin/bash

echo "Hello! This program will fetch information for cocktails using different scripts."
echo "For now, only the Drink information function will work."

PS3="Select an option (1-4)"
select i in Drink_Information Drink_Instruction Drink_Video Exit
do 
    case $i in
    Drink_Information)
        python3 Cocktails.py
        break
        ;;
    Drink_Instruction)
        echo "Currently unavailable"
        ;;
    Drink_Video)
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
