import streamlit as st
import random as rd
import numpy as np

st.title("Rock Paper Scissors")
if st.button("Play"):
    st.write("Welcome to Rock Paper Scissors!")
def rps(user_choice):
    if user_choice == "rock":
        return "paper"
    elif user_choice == "paper":
        return "scissors"
    elif user_choice == "scissors":
        return "rock"

def rps_computer(computer_choice):
    if computer_choice == "rock":
        return "scissors"
    elif computer_choice == "paper":
        return "rock"
    elif computer_choice == "scissors":
        return "paper"

def rps_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "You win!"
    elif user_choice == "paper" and computer_choice == "rock":
        return "You win!"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "You win!"
    elif user_choice == "rock" and computer_choice == "paper":
        return "You lose!"
    elif user_choice == "paper" and computer_choice == "scissors":
        return "You lose!"
    elif user_choice == "scissors" and computer_choice == "rock":
        return "You lose!"

user_choice = st.selectbox("Choose your choice", ("rock", "paper", "scissors"))
computer_choice = rd.choice(["rock", "paper", "scissors"])

result = rps_result(user_choice, computer_choice)            
st.write(result)

if result == "You win!":
    st.write("You win!")
elif result == "You lose!":
    st.write("You lose!")
elif result == "It's a tie!":        
    st.write("It's a tie!")     